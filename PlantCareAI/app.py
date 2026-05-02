from flask import Flask, render_template, request, redirect, session, abort, flash
import tensorflow as tf
import numpy as np
import cv2
import os
import sqlite3
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from disease_info import disease_info

app = Flask(__name__)
app.secret_key = "secret"


# ================= DATABASE =================
def get_db():
    """Get a connection to the SQLite user database."""
    conn = sqlite3.connect("users.db")
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    """Initialize the users table and create default admin account."""
    conn = get_db()
    conn.execute("""CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )""")
    conn.commit()

    # Create default admin account if it doesn't exist
    existing = conn.execute("SELECT id FROM users WHERE username = ?", ("admin",)).fetchone()
    if not existing:
        conn.execute(
            "INSERT INTO users (username, password) VALUES (?, ?)",
            ("admin", generate_password_hash("1234"))
        )
        conn.commit()
    conn.close()


init_db()

# ✅ Load model
model = tf.keras.models.load_model("outputs/model.h5")

# ✅ Load class names
dataset_path = "dataset/PlantVillage"
class_names = sorted(os.listdir(dataset_path))


# ================= HELPERS =================
def get_disease_info(name):
    """Look up disease info with flexible key matching."""
    variants = [
        name,
        name.replace("___", "_"),
        name.replace("__", "_"),
        name.replace("_", "___"),
    ]

    for v in variants:
        if v in disease_info:
            return disease_info[v]

    # Return a fallback with all required fields
    return {
        "description": "No detailed information available for this condition.",
        "scientific_name": "Unknown",
        "severity": "Unknown",
        "hosts": "N/A",
        "transmission": "N/A",
        "humidity_risk": 0,
        "causes": [],
        "treatment": ["Consult a local agricultural extension service for guidance."],
        "prevention": []
    }


def get_severity(confidence):
    """Compute severity label from confidence score."""
    if confidence >= 0.9:
        return "Critical"
    elif confidence >= 0.7:
        return "High"
    elif confidence >= 0.5:
        return "Medium"
    else:
        return "Low"


def generate_scan_id():
    """Generate a short scan ID."""
    total = session.get("total", 0)
    return f"PH-{900 + total}"


# ================= LOGIN =================
@app.route("/", methods=["GET", "POST"])
def login():
    error = None

    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")

        conn = get_db()
        user = conn.execute("SELECT * FROM users WHERE username = ?", (username,)).fetchone()
        conn.close()

        if user and check_password_hash(user["password"], password):
            session["user"] = username
            session["total"] = session.get("total", 0)
            session["healthy"] = session.get("healthy", 0)
            session["diseased"] = session.get("diseased", 0)
            session["history"] = session.get("history", [])
            return redirect("/dashboard")
        else:
            error = "Invalid username or password"

    return render_template("login.html", error=error)


# ================= REGISTER =================
@app.route("/register", methods=["GET", "POST"])
def register():
    error = None
    success = None

    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")
        confirm = request.form.get("confirm_password", "")

        # Validation
        if not username or not password:
            error = "Username and password are required"
        elif len(username) < 3:
            error = "Username must be at least 3 characters"
        elif len(password) < 4:
            error = "Password must be at least 4 characters"
        elif password != confirm:
            error = "Passwords do not match"
        else:
            conn = get_db()
            existing = conn.execute("SELECT id FROM users WHERE username = ?", (username,)).fetchone()

            if existing:
                error = "Username already taken"
                conn.close()
            else:
                conn.execute(
                    "INSERT INTO users (username, password) VALUES (?, ?)",
                    (username, generate_password_hash(password))
                )
                conn.commit()
                conn.close()
                success = "Account created successfully! You can now log in."

    return render_template("register.html", error=error, success=success)


# ================= DASHBOARD =================
@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect("/")

    return render_template("dashboard.html",
        active_page="dashboard",
        total=session.get("total", 0),
        healthy=session.get("healthy", 0),
        diseased=session.get("diseased", 0),
        history=session.get("history", [])
    )


# ================= PREDICT =================
@app.route("/predict", methods=["POST"])
def predict():
    if "file" not in request.files:
        return redirect("/dashboard")

    file = request.files["file"]

    if file.filename == "":
        return redirect("/dashboard")

    os.makedirs("static", exist_ok=True)

    filepath = os.path.join("static", file.filename)
    file.save(filepath)

    img = cv2.imread(filepath)
    if img is None:
        os.remove(filepath)
        return redirect("/dashboard")
    img = cv2.resize(img, (224, 224)) / 255.0
    img = np.expand_dims(img, axis=0)

    pred = model.predict(img)
    index = np.argmax(pred)
    confidence = float(np.max(pred))

    prediction = class_names[index]

    # ✅ SAVE RESULT IN SESSION
    session["last_result"] = {
        "image": filepath,
        "prediction": prediction,
        "confidence": confidence
    }

    # ✅ UPDATE STATS
    session["total"] = session.get("total", 0) + 1

    if "healthy" in prediction.lower():
        session["healthy"] = session.get("healthy", 0) + 1
    else:
        session["diseased"] = session.get("diseased", 0) + 1

    # ✅ ADD TO HISTORY
    history = session.get("history", [])
    history.append({
        "id": generate_scan_id(),
        "image": filepath,
        "prediction": prediction,
        "confidence": confidence,
        "timestamp": datetime.now().strftime("%b %d, %Y • %I:%M %p"),
        "is_healthy": "healthy" in prediction.lower()
    })
    session["history"] = history

    return redirect("/result")


# ================= RESULT =================
@app.route("/result")
def result():
    if "user" not in session:
        return redirect("/")

    data = session.get("last_result")

    if not data:
        return redirect("/dashboard")

    prediction = data["prediction"]
    confidence = data["confidence"]
    info = get_disease_info(prediction)
    is_healthy = "healthy" in prediction.lower()

    return render_template("result.html",
        active_page="history",
        image_path=data["image"],
        prediction=prediction,
        confidence=confidence,
        info=info,
        is_healthy=is_healthy
    )


# ================= DETAILS =================
@app.route("/details")
def details():
    if "user" not in session:
        return redirect("/")

    data = session.get("last_result")

    if not data:
        return redirect("/dashboard")

    prediction = data["prediction"]
    confidence = data["confidence"]
    info = get_disease_info(prediction)
    is_healthy = "healthy" in prediction.lower()

    return render_template("details.html",
        active_page="history",
        disease=prediction,
        info=info,
        is_healthy=is_healthy,
        confidence=confidence,
        image_path=data.get("image", "")
    )


# ================= HISTORY =================
@app.route("/history")
def history():
    if "user" not in session:
        return redirect("/")

    total = session.get("total", 0)
    healthy_count = session.get("healthy", 0)
    diseased_count = session.get("diseased", 0)
    healthy_rate = (healthy_count / total * 100) if total > 0 else 0

    return render_template("history.html",
        active_page="history",
        total=total,
        healthy=healthy_count,
        diseased=diseased_count,
        healthy_rate=healthy_rate,
        history=session.get("history", [])
    )


# ================= VIEW HISTORY ITEM =================
@app.route("/history/<int:index>")
def view_history_item(index):
    if "user" not in session:
        return redirect("/")

    history = session.get("history", [])

    # History is displayed reversed (newest first), so convert display index to actual index
    actual_index = len(history) - 1 - index

    if actual_index < 0 or actual_index >= len(history):
        return redirect("/history")

    item = history[actual_index]

    # Set as last_result so result/details pages work
    session["last_result"] = {
        "image": item["image"],
        "prediction": item["prediction"],
        "confidence": item["confidence"]
    }

    return redirect("/result")


# ================= LOGOUT =================
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")


# ================= ERROR HANDLERS =================
@app.errorhandler(404)
def page_not_found(e):
    return render_template("error.html", code=404, message="Page Not Found", detail="The resource you're looking for doesn't exist or has been moved."), 404


@app.errorhandler(500)
def internal_error(e):
    return render_template("error.html", code=500, message="Internal Server Error", detail="Something went wrong on our end. Please try again."), 500


# ================= RUN =================
if __name__ == "__main__":
    app.run(debug=True)
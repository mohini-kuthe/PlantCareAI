# PlantCareAI — Setup & Run Guide

## 📦 What's in the Zip

```
PlantCareAI/
├── app.py                  # Flask backend (routes, model inference)
├── disease_info.py         # Disease database (15 plant conditions)
├── requirements.txt        # Python dependencies
├── outputs/
│   └── model.h5            # Trained CNN model (MobileNetV2)
├── model/
│   ├── train_model.py      # Model training script
│   └── predict.py          # CLI prediction script
├── templates/              # Jinja2 HTML templates
│   ├── base.html
│   ├── login.html
│   ├── register.html
│   ├── dashboard.html
│   ├── result.html
│   ├── details.html
│   ├── history.html
│   └── error.html
└── static/
    ├── style.css
    └── images/bg.jpg
```

> **Note:** The `dataset/` folder is NOT included in the zip (too large). You need it only if you want to retrain the model.

---

## 🚀 How to Run Locally

### Step 1: Extract the Zip
```
Extract PlantCareAI.zip to any folder, e.g. D:\PlantCareAI
```

### Step 2: Open Terminal
```bash
cd D:\PlantCareAI
```

### Step 3: Create Virtual Environment (Recommended)
```bash
python -m venv venv
venv\Scripts\activate
```

### Step 4: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 5: Add Dataset Folder
Create a `dataset/PlantVillage/` folder with the 15 class subfolders. The model needs this to map class names.

If you don't have the dataset, create empty folders:
```bash
mkdir dataset\PlantVillage
cd dataset\PlantVillage
mkdir Pepper__bell___Bacterial_spot
mkdir Pepper__bell___healthy
mkdir Potato___Early_blight
mkdir Potato___Late_blight
mkdir Potato___healthy
mkdir Tomato_Bacterial_spot
mkdir Tomato_Early_blight
mkdir Tomato_Late_blight
mkdir Tomato_Leaf_Mold
mkdir Tomato_Septoria_leaf_spot
mkdir Tomato_Spider_mites_Two_spotted_spider_mite
mkdir Tomato__Target_Spot
mkdir Tomato__Tomato_YellowLeaf__Curl_Virus
mkdir Tomato__Tomato_mosaic_virus
mkdir Tomato_healthy
cd ..\..
```

### Step 6: Run the App
```bash
python app.py
```

### Step 7: Open in Browser
```
http://127.0.0.1:5000
```

---

## 🔐 Default Login
| Username | Password |
|----------|----------|
| admin    | 1234     |

You can also create a new account via the **Create Account** link on the login page.

---

## ⚠️ Troubleshooting

| Issue | Fix |
|-------|-----|
| `ModuleNotFoundError: No module named 'flask'` | Run `pip install -r requirements.txt` |
| `FileNotFoundError: outputs/model.h5` | Make sure the `outputs/` folder with `model.h5` is in the project root |
| `FileNotFoundError: dataset/PlantVillage` | Create the dataset folder structure (Step 5 above) |
| `TensorFlow GPU warning` | This is normal on Windows — the app runs fine on CPU |
| Port 5000 already in use | Change the port: `app.run(debug=True, port=8080)` in `app.py` |

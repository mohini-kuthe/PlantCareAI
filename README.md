<div align="center">

# 🌿 PlantCareAI

**AI-powered plant disease detection — upload a leaf photo, get an instant diagnosis.**

![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-2.3%2B-000000?logo=flask)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.12%2B-FF6F00?logo=tensorflow&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-4.7%2B-5C3EE8?logo=opencv&logoColor=white)

</div>

---

## What it does

PlantCareAI uses a **MobileNetV2 CNN model** trained on the PlantVillage dataset to detect diseases in tomato, potato, and bell pepper leaves. Upload a photo — get back the disease name, confidence score, severity level, and exactly what to do about it.

---

## Features

- 📸 **Instant diagnosis** — upload any leaf image and get results in seconds
- 📊 **Dashboard** — tracks your total scans, healthy vs diseased breakdown
- 📜 **Scan history** — browse all past scans with timestamps
- 🧪 **Detailed info** — scientific name, causes, treatment steps, prevention tips
- 👤 **User accounts** — register/login with hashed passwords

---

## Supported Diseases (15 classes)

| Crop | Conditions |
|------|-----------|
| 🍅 Tomato | Bacterial Spot, Early Blight, Late Blight, Leaf Mold, Septoria Leaf Spot, Spider Mites, Target Spot, Yellow Leaf Curl Virus, Mosaic Virus, Healthy |
| 🥔 Potato | Early Blight, Late Blight, Healthy |
| 🫑 Bell Pepper | Bacterial Spot, Healthy |

---

## Project Structure

```
PlantCareAI/
├── app.py                  # Flask routes + model inference
├── disease_info.py         # Disease database (descriptions, treatments)
├── requirements.txt
├── outputs/
│   └── model.h5            # Pre-trained MobileNetV2 model
├── model/
│   ├── train_model.py      # Retrain the model
│   └── predict.py          # CLI prediction script
├── templates/              # HTML pages (login, dashboard, result, history...)
└── static/                 # CSS + images
```

---

## Getting Started

### 1. Clone & enter the project

```bash
git clone https://github.com/your-username/PlantCareAI.git
cd PlantCareAI
```

### 2. Create a virtual environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Create the dataset folder structure

The app needs this folder to map model outputs to class names. You don't need the actual images just to run it.

```bash
# Windows
mkdir dataset\PlantVillage
cd dataset\PlantVillage
mkdir Pepper__bell___Bacterial_spot Pepper__bell___healthy Potato___Early_blight Potato___Late_blight Potato___healthy Tomato_Bacterial_spot Tomato_Early_blight Tomato_Late_blight Tomato_Leaf_Mold Tomato_Septoria_leaf_spot Tomato_Spider_mites_Two_spotted_spider_mite Tomato__Target_Spot Tomato__Tomato_YellowLeaf__Curl_Virus Tomato__Tomato_mosaic_virus Tomato_healthy
cd ..\..
```

```bash
# macOS / Linux
mkdir -p dataset/PlantVillage/{Pepper__bell___Bacterial_spot,Pepper__bell___healthy,Potato___Early_blight,Potato___Late_blight,Potato___healthy,Tomato_Bacterial_spot,Tomato_Early_blight,Tomato_Late_blight,Tomato_Leaf_Mold,Tomato_Septoria_leaf_spot,Tomato_Spider_mites_Two_spotted_spider_mite,Tomato__Target_Spot,Tomato__Tomato_YellowLeaf__Curl_Virus,Tomato__Tomato_mosaic_virus,Tomato_healthy}
```

> Want to retrain the model? Download the full [PlantVillage dataset from Kaggle](https://www.kaggle.com/datasets/emmarex/plantdisease) and place the class folders inside `dataset/PlantVillage/`.

### 5. Run

```bash
python app.py
```

Open `http://127.0.0.1:5000` in your browser.

---

## Default Login

| Username | Password |
|----------|----------|
| `admin`  | `1234`   |

Or register a new account from the login page.

---

## Retraining the Model

```bash
python model/train_model.py
```

Saves the new model to `outputs/model.h5`. To test a single image via CLI:

```bash
python model/predict.py --image path/to/leaf.jpg
```

---

## Note

The `dataset/` folder is not included because it's too large. The `model.h5` file (trained model) is included in `outputs/`. If you want to retrain the model, download the PlantVillage dataset from Kaggle and run `model/train_model.py`.

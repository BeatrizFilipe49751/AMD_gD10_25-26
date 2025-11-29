# MedKnow Knowledge Discovery Prototype

**FINAL PROJECT – A**

**Subject:** AMD – *Aprendizagem e Mineração de Dados* | MLDM – *Machine Learning and Data Mining*

**Course:** MEIM | MEIC

---

## Project Goal

The purpose of this project is to explore the relationship between data, information, and knowledge, demonstrating how raw data can be transformed into useful insights through data mining and machine learning techniques.

In this scenario, the MedKnow medical center aims to analyze ophthalmology data collected over time to extract patterns supporting diagnosis and prescription.
The SoftKnow team (our group) developed a deployable prototype that fulfills both operational and strategic needs, by applying 1R, ID3, and Naive Bayes classifiers to the “lenses” dataset.

---

## Implemented Components

1. **Data Analysis & Assumptions** – based on `d01_lenses.xls`, assumptions were made about MedKnow’s operational workflow involving patients, doctors, and diseases.
2. **Database & Data Export** – implemented scripts to create, populate, and export data from a simulated relational database.
3. **Machine Learning Models** – implemented and trained three classification algorithms:
   * **One Rule (1R)** - custom implementation in Python
   * **ID3 Decision Tree**
   * **Naive Bayes**
4. **Evaluation & Comparison** – all models evaluated on accuracy and reliability to determine the best approach.
5. **Deployable Prediction Modules** – modular prediction scripts for each model, enabling MedKnow to classify new patient data without retraining.

---

## Project Structure

```
project-root/
├── docs/                           # Project report and EA diagram
├── artifacts/                      # Trained models, encoders, and test data
├── scripts/
│   ├── datasets/
│   │   ├── dataset.csv
│   │   └── dataset_3row_orange.tab
│   ├── _go00.bat                   # Create database
│   ├── _go01.bat                   # Create schema
│   ├── _go02.bat                   # Populate schema
│   ├── _go03.bat                   # Create view
│   ├── _go04.bat                   # Export data to CSV
│   └── ...
├── python/
│   ├── train_and_save.py           # Train 1R, ID3, and NB models
│   ├── evaluate_models.py          # Evaluate and compare model performance
│   ├── predictions/
│   │   ├── predict_1R.py           # Predict using trained 1R model
│   │   └── predict_classifiers.py  # Predict using trained ID3 and NB models
│   ├── utils/
│   │   ├── config.py               # Default paths (artifacts, datasets)
│   │   ├── preprocessing.py        # Data preprocessing (encoding, splitting)
│   │   ├── load_models.py          # Load trained models
│   │   └── transform_new_data.py   # Transform new samples for prediction
│   └── models/
│       ├── one_rule.py             # 1R algorithm implementation
│       ├── train_id3.py            # ID3 training
│       └── train_nb.py             # Naive Bayes training
└── README.md
```

---

## Setup Instructions

### Install Requirements

Ensure **Python 3.9+** is installed.

Install dependencies with:

```bash
pip install pandas scikit-learn numpy
```

---

## Database Initialization

The /scripts folder contains batch scripts to create and populate the MedKnow database.
Execute them in order:

```bash
.\_go00.bat
.\_go01.bat
.\_go02.bat
.\_go03.bat
.\_go04.bat
```

These scripts:
1. Create and initialize the database.
2. Create and populate the schema with sample data.
3. Create necessary views.
4. Export the dataset to `scripts/datasets/dataset.csv`.

---

## Model Training

To (re)train all models (1R, ID3, and Naive Bayes):

```bash
python -m python.train_and_save <target_column>
```

Example:
```bash
python -m python.train_and_save lenses
```

This script:
1. Load and preprocess the dataset.
2. Train all three models.
3. Saves models, encoders, and test sets in `/artifacts`.

---

## Model Evaluation

To evaluate all trained models:

```bash
python -m python.evaluate_models.py
```

Displays:
* Accuracy scores
* Confusion matrices
* Classification reports
* Execution times
* Comparison of all models

---

## Making Predictions (Deployment / MedKnow usage)

With the models trained and stored in /artifacts, MedKnow can use them directly for predictions, no retraining required.

Predict using 1R:

```bash
python -m python.predictions.predict_1R <path_to_csv>
```

Example:

```bash
python -m python.predictions.predict_1R new_lenses_data.csv
```

Output:
A DataFrame printed to console:

```
feature_1 | feature_2 | ... | 1R_prediction
```

Predict using ID3 and Naive Bayes:

```bash
python -m python.predictions.predict_classifiers <path_to_csv>
```

Output:
A DataFrame printed to console:

```
feature_1 | feature_2 | ... | ID3_prediction | NB_prediction
```

---

## Artifacts and Outputs

| File                       | Description                       |
| -------------------------- | --------------------------------- |
| `oner_model.pkl`           | Trained One Rule model            |
| `id3_model.pkl`            | Trained ID3 Decision Tree         |
| `nb_model.pkl`             | Trained Naive Bayes model         |
| `feature_encoders.pkl`     | Encoders for categorical features |
| `target_encoder.pkl`       | Encoder for target variable       |
| `X_test.csv`, `y_test.csv` | Test data for evaluation          |

---

## Authors

* Beatriz Filipe, 49751
* Ana Assis, 53537

**Technologies:** Python, PostgreSQL, Pandas, scikit-learn, Orange Data Mining

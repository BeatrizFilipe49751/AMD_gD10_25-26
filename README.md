# MedKnow Knowledge Discovery Prototype

**FINAL PROJECT – A**

**Subject:** AMD – *Aprendizagem e Mineração de Dados* | MLDM – *Machine Learning and Data Mining*

**Course:** MEIM | MEIC

---

## Project Goal

The purpose of this project is to **explore the relationship between data, information, and knowledge**, and to apply data-mining and machine learning techniques to transition from raw data to actionable insights.

In this specific scenario, the **MedKnow** medical center aims to extract useful patterns from historical ophthalmology data to support **diagnosis** and **prescription**.
The **SoftKnow** team (student group) developed this prototype as a deployable solution to analyze and classify patient data using **1R**, **ID3**, and **Naive Bayes** models.

---

## Implemented Components

1. **Data Analysis & Assumptions** – based on `d01_lenses.xls`, assumptions were made about MedKnow’s operational workflow involving patients, doctors, and diseases.
2. **Database Setup** – implemented relational schema and scripts to create, populate, and export the dataset automatically.
3. **Machine Learning Models** – implemented three algorithms:
   * **One Rule (1R)**
   * **ID3 Decision Tree**
   * **Naive Bayes**
4. **Evaluation & Comparison** – all models evaluated on accuracy and reliability to determine the best approach.

---

## Project Structure

```
project-root/
├── docs/                      # Project report and EA diagram
├── artifacts/                 # Trained models, encoders, and test data
├── scripts/
│   ├── datasets/
│   │   ├── dataset.csv
│   │   └── dataset_3row_orange.tab
│   ├── _go00.bat              # Create database
│   ├── _go01.bat              # Create schema
│   ├── _go02.bat              # Populate schema
│   ├── _go03.bat              # Create view
│   ├── _go04.bat              # Export data to CSV
│   └── ...
├── python/
│   ├── config.py              # Configuration paths and constants
│   ├── preprocessing.py       # Data preprocessing (encoding, splitting)
│   ├── train_and_save.py      # Train 1R, ID3, and NB models
│   ├── evaluate_models.py     # Evaluate and compare model performance
│   ├── predict_medknow.py     # Make predictions on unseen data
│   ├── load_models.py         # Load trained models for inference
│   └── models/
│       ├── one_rule.py
│       ├── train_id3.py
│       ├── train_nb.py
│       └── ...
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

To prepare and export the dataset, execute the batch scripts in the following order:

```bash
.\_go00.bat
.\_go01.bat
.\_go02.bat
.\_go03.bat
.\_go04.bat
```

These scripts will:
1. Create and initialize the database.
2. Create and populate the schema with sample data.
3. Create necessary views.
4. Export the dataset to `scripts/datasets/dataset.csv`.

---

## Model Training

To (re)train and save models:

```bash
cd python
python train_and_save.py <target_column> [optional_dataset_path]
```

Examples:

Use the default dataset defined in config.py:
```bash
cd python
python train_and_save.py lenses
```

Or specify a custom CSV file:
```bash
cd python
python train_and_save.py lenses ../scripts/datasets/custom_dataset.csv
```

This script:
* Loads and preprocesses the dataset.
* Trains 1R, ID3, and Naive Bayes models.
* Saves models, encoders, and test sets in `/artifacts`.

---

## Model Evaluation

To evaluate model accuracy and reliability:

```bash
cd python
python evaluate_models.py
```

This will display:
* Accuracy scores
* Confusion matrices
* Classification reports
* Execution times
* Comparison of all models

---

## Solution - Making Predictions (MedKnow usage)

With the models trained and stored in /artifacts, MedKnow can use them directly to predict new patient cases — no retraining required.
To classify new samples from a CSV file:

```bash
cd python
python predict_medknow.py <path_to_csv>
```

Example:

```bash
cd python
python predict_medknow.py new_samples.csv
```

Outputs predicted classes for each model:

```
feature_1 | feature_2 | ... | 1R_prediction | ID3_prediction | NB_prediction
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
| `X_test.csv`, `y_test.csv` | Test data used for evaluation     |

---

## Summary of Commands

| Task                | Command                                    |
| ------------------- | ------------------------------------------ |
| Initialize database | `.\_go00.bat → .\_go04.bat`                |
| Train models        | `python train_and_save.py <target_column>` |
| Evaluate models     | `python evaluate_models.py`                |
| Predict new data    | `python predict_medknow.py <csv>`         |

---

## Authors

* Beatriz Filipe, 49751
* *[Nome, nr]*

**Technologies:** Python, PostgreSQL, Pandas, scikit-learn, Orange Data Mining

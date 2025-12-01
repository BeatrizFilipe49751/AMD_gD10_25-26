# MedKnow & FungiData Knowledge Discovery Prototype

**FINAL PROJECT – A and A1**

**Subject:** AMD – *Aprendizagem e Mineração de Dados* | MLDM – *Machine Learning and Data Mining*

**Course:** MEIM | MEIC

---

## Project Goal

The purpose of this project is to explore the relationship between data, information, and knowledge, demonstrating how raw data can be transformed into actionable insights using data mining and machine learning techniques.

#### Scenario A – MedKnow:
The MedKnow medical center aims to analyze ophthalmology consultation data collected over time to extract patterns supporting diagnosis and prescription. The SoftKnow team (our group) developed a deployable prototype fulfilling operational and strategic needs, applying 1R, ID3, and Naive Bayes classifiers to the “lenses” dataset.

#### Scenario A1 – FungiData:
The FungiData institute challenges the team to classify mushrooms as edible or poisonous based on 22 categorical features. The dataset was downloaded from UCI Mushroom dataset
 and processed for Orange Data Mining.

---

## Project Structure

```
project-root/
├── docs/                           # Project report, ER diagram
├── artifacts/                      # Trained models, encoders, 1R output, test data
├── scripts/
│   ├── datasets/
│   │   ├── dataset.csv
│   │   ├── dataset_3row_orange.tab
│   │   ├── dataset_long_name_ORIGINAL.csv
│   │   └── dataset_long_name_PTS_INPUT_v01.tab
│   ├── _go00.bat                   # Create database
│   ├── _go01.bat                   # Create schema
│   ├── _go02.bat                   # Populate schema
│   ├── _go03.bat                   # Create view
│   ├── _go04.bat                   # Export CSV
│   └── ...
├── orange/
│   └── A1_workspace.ows            # Orange DM workflow for Mushroom dataset
├── python/
│   ├── train_and_save.py           # Train MedKnow models (1R, ID3, NB)
│   ├── evaluate_models.py          # Evaluate MedKnow models
│   ├── predictions/
│   │   ├── predict_1R.py           # 1R predictions for MedKnow
│   │   └── predict_classifiers.py  # ID3 and NB predictions for MedKnow
│   ├── utils/
│   │   ├── config.py               # Paths for datasets/artifacts
│   │   ├── preprocessing.py        # Encoding, splitting, transformation
│   │   ├── load_models.py          # Load trained models
│   │   └── transform_new_data.py   # Transform new input data
│   ├── models/
│   │   ├── one_rule.py             # 1R implementation
│   │   ├── train_id3.py            # ID3 implementation
│   │   └── train_nb.py             # Naive Bayes implementation
│   └── A1/
│       ├── dataset_transform.py    # CSV → .tab for Orange
│       └── generate_1r_output.py  # 1R output for Mushroom dataset
└── README.md
```

---

## Install Requirements

Ensure **Python 3.9+** is installed.

Install dependencies with:

```bash
pip install pandas scikit-learn numpy
```

---
## Setup Instructions - A

### Database Initialization

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

### Model Training

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

### Model Evaluation

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

### Making Predictions (Deployment / MedKnow usage)

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

## Setup Instructions - A1

### Dataset Transformation

Convert `dataset_long_name_ORIGINAL.csv` into Orange `.tab` format:

```bash
python -m python.A1.dataset_transform
```

Result saved to: `dataset_long_name_PTS_INPUT_v01.tab`

---

### Generate 1R Output

Run our 1R implementation on the mushroom dataset:

```bash
python -m python.A1.generate_1r_output class
```

Produces: `oneR_OUTPUT.txt` (per-value error statistics).

---

### Orange Workflow

Open the workspace: `orange/A1_workspace.ows`

This workspace includes: instance counts, class distribution, Decision Tree and Random Forest models, predictions using both classifiers.

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
| `oneR_OUTPUT.txt`          | 1R output for Mushroom dataset    |

---

## Authors

* Beatriz Filipe, 49751
* Ana Assis, 53537

**Technologies:** Python, PostgreSQL, Pandas, scikit-learn, Orange Data Mining

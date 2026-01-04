# SoftKnow: Market-Basket Analysis for We-Commerce

**FINAL PROJECT – B**

**Subject:** AMD – *Aprendizagem e Mineração de Dados* | MLDM – *Machine Learning and Data Mining*

**Course:** MEIM | MEIC

---

## Project Goal

This project addresses the challenge proposed by We-Commerce: generating business knowledge from large-scale e-commerce browsing data. Acting as SoftKnow, we analyze, model, and validate a complete data-mining pipeline that transforms raw event data into actionable knowledge using:
* SQL (PostgreSQL) for data aggregation and filtering
* Python for data transformation and automation
* Orange Data Mining for association rule discovery and visualization

The project follows the steps defined in the assignment items (1–9).

---

## Project Structure

```
├── docs
│   ├── zz_dataset_2012_01.basket               # Orange basket-format dataset
│   ├── zz_dataset_2012_01.tab                  # Tabular version of the basket dataset
│   ├── z_dataset_JAN_updated.csv               # Original dataset
│   ├── z_dataset_OUT.txt                       # Exported (transaction_id; product_id) pairs
│
├── orange
│   ├── report.html                             # Exported visual report from Orange
│   ├── workflow_associationrules.ows           # Orange workflow for association rule mining
│
├── python
│   ├── orange_Associate_example.py             # Controlled exploration of association rules
│   ├── _goPy_transform_v02.py                  # Data normalization and basket generation
│
└── scripts
    ├── 00_script_CREATE_DB.txt
    ├── 01_script_CREATE_SCHEMA.txt
    ├── 02_script_IMPORT_POPULATE_SCHEMA.txt
    ├── 03_script_CREATE_VIEW.txt
    ├── 04_script_EXPORT_DATA.txt
    ├── _go.bat
    ├── _go00.bat
    ├── _go01.bat
    ├── _go02.bat
    ├── _go03.bat
    ├── _go04.bat
```

---
## Setup Instructions

### Exercise 2 - Market-Basket Problem Formulation

**Goal:** Reformulate product navigation as a market-basket problem.
* Each session = transaction
* Each product_gui = item
* Association rules discover co-visited products

No execution required.

---

### Exercise 3 - Aggregated View of the Data

1. Create the PostgreSQL database:
```bash
.\_go00.bat
```

2. Create schema:
```bash
.\_go01.bat
```

3. Import dataset:
```bash
.\_go02.bat
```

4. Create aggregation views:
```bash
.\_go03.bat
```

Outputs
* Total number of events
* Total number of visitors (cookie_id)
* Distribution of:
    * number of sessions per visitor
    * number of events per session

---

### Exercise 4 - Dataset Reduction

**Goal:** Reduce computational complexity.

**Criteria:**
* Visitors with 5 ≤ number_of_sessions ≤ 30
* Remove useless product values:
    * 'open'
    * 'home' 
    * '/customer/account/login/'
    * '/customer/account/forgotpassword/'
    * 'display.category*homepage'
    * '/customer/account/'
    * '/customer/account/logoutsuccess/' 

**Execution:**
Handled automatically in: `v_export` view (defined in `03_script_CREATE_VIEW.txt`; executed via `.\_go03.bat`)

---

### Exercise 5 - Export Filtered Transactions

**Goal:** Generate `(TRANSACTION_ID, PRODUCT_ID)` file.

**Execution:**
```bash
.\_go04.bat
```

**Output:** `docs/z_dataset_OUT.txt`

This file contains (cookie_id; product_gui) pairs.

---

### Exercise 6 - Data Normalization and Basket Generation

**Goal:**
* Normalize product names
* Generate Orange .basket file and .tab file

**Execution:**
```bash
python python/_goPy_transform_v02.py
```

This script:
1. Removes accents
2. Converts to lowercase
3. Removes spaces and special characters
4. Generates .basket and .tab files

**Outputs:**
1. `docs/zz_dataset_2012_01.basket`
2. `docs/zz_dataset_2012_01.tab`

---

### Exercise 7 - Controlled Exploration of Association Rules

**Goal:** Generate marketing knowledge through controlled exploration of support and confidence thresholds.

**Execution:**
```bash
python python/orange_Associate_example.py <maxR>
```

This script:
1. Explores predefined support and confidence ranges
2. Enforces a maximum number of rules (maxR)
3. Retains only valid support-confidence combinations that produce a limited number of rules

---

### Exercise 8 - Graphical Market-Basket Analysis with Orange

**Goal:** Produce a visual report for We-Commerce.

**Orange workspace:** `orange/workflow_associationrules.ows`

Workflow contains:
* File (.basket)
* Data Table
* Frequent Itemsets
* Association Rules

Set parameters:
* Minimum Support: 4%
* Minimum Confidence: 75%

Inspect:
* Rule tables
* Metrics (support, confidence, lift, coverage)

**Export report:** `orange/report.html`

---

## Authors

* Beatriz Filipe, 49751
* Ana Assis, 53537

**Technologies:** Python, PostgreSQL, Pandas, Orange Data Mining

# Netflix Data Intelligence Platform 🎬📊

> **Auspify Technologies Data Science Internship Capstone Project**  
> An end-to-end data intelligence, content recommendation, and predictive classification platform built on the Netflix catalog dataset (8,789 titles).

[![Python 3.13](https://img.shields.io/badge/Python-3.13-blue.svg)](https://www.python.org/)
[![Scikit-Learn](https://img.shields.io/badge/scikit--learn-1.9.1-orange.svg)](https://scikit-learn.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-Backend-teal.svg)](https://fastapi.tiangolo.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## 📌 Executive Summary
This project satisfies the 4-week project-based Data Science Internship requirement at **Auspify Technologies**. It delivers four core analytical and machine learning tasks:
1. **Task 1 (Data Cleaning & Preprocessing):** Detection of hidden placeholders, missing-value treatment, duration extraction, date standardisation, and export of `netflix_clean.csv`.
2. **Task 2 (Exploratory Data Analysis):** 11 detailed analytical visualizations uncovering content distribution, country dominance, seasonal trends, and catalog aging.
3. **Task 3 (Content-Based Recommendation Engine):** Multi-attribute metadata soup with TF-IDF vectorization, linear kernel cosine similarity, and quantitative evaluation using **Jaccard Genre Overlap**.
4. **Task 5 (Supervised ML Classification):** Leakage-free classification predicting content `type` (Movie vs. TV Show) across 6 models (Logistic Regression, Random Forest, Linear SVM, Naive Bayes, Decision Trees, Gradient Boosting) with 5-fold Stratified CV and hyperparameter tuning.

---

## 📁 Repository Structure

```
Netflix_Data_Intelligence_Platform/
├── README.md                                  # Primary project overview & documentation
├── requirements.txt                            # Pinned Python package dependencies
├── .gitignore                                 # Git ignore rules (clean repository)
├── backend/
│   ├── data/
│   │   ├── raw/
│   │   │   └── Dataset.csv                    # Raw initial dataset (8,790 records)
│   │   └── processed/
│   │       └── netflix_clean.csv              # Production cleaned dataset (8,789 records, 16 features)
│   ├── notebooks/
│   │   ├── 01_data_cleaning.ipynb             # Task 1: Complete cleaning pipeline with before/after table
│   │   ├── 02_exploratory_analysis.ipynb      # Task 2: 11-chart EDA with written findings
│   │   ├── 03_recommendation_system.ipynb     # Task 3: Content-based engine & Jaccard evaluation
│   │   └── 04_classification_model.ipynb      # Task 5: 6-model classifier benchmark & interpretability
│   └── app/
│       ├── main.py                            # FastAPI entry point
│       ├── routes/                            # Modular API endpoints
│       └── services/                          # Analytics & recommendation services
└── documentation/
    ├── auspify_data_science_implementation_plan.md
    ├── findings.md                            # Comprehensive strategic business insights
    ├── methodology.md                         # Detailed mathematical & technical methodology
    ├── project_report.md                      # Formal capstone internship report
    └── screenshots/                           # Visual proof of completion
        ├── task1/                             # Cleaning summary charts
        ├── task2/                             # 11 EDA visualization figures
        ├── task3/                             # Recommender Jaccard evaluation plots
        └── task5/                             # Model comparison, confusion matrix, feature weights
```

---

## 🚀 Tasks Completed & Technical Highlights

### 🔹 Task 1: Data Cleaning & Preprocessing
- **Hidden Null Detection:** Uncovered that `director` (2,588 records) and `country` (287 records) contained `"Not Given"` string placeholders rather than standard nulls.
- **Title Validation:** Identified 1 title with value `"Unknown"`, which was cleanly dropped.
- **Duration Normalization:** Parsed mixed format (`"90 min"` vs. `"1 Season"`) into numeric `duration_value` and categorical `duration_unit`.
- **Temporal Engineering:** Converted `date_added` into `datetime64[us]` and extracted `year_added` and `month_added`.
- **Derived Features:** Engineered single-valued `main_country` and `primary_genre` for downstream modelling.
- **Output:** Clean `netflix_clean.csv` (8,789 rows × 16 columns) with zero nulls.

### 🔹 Task 2: Exploratory Data Analysis (EDA)
- **Catalog Mix:** Movies constitute **69.7%** (6,125 titles) vs. **30.3%** (2,664 titles) for TV Shows.
- **Geographic Production:** The United States (3,240), India (1,057), and the UK (637) form the top 3 production hubs.
- **Audience Focus:** **>60%** of content carries adult/mature ratings (`TV-MA`, `TV-14`, `R`).
- **Growth Patterns:** Additions surged aggressively from 2016 through 2019, peaking at over 2,000 additions per year.
- **Recency Distribution:** Over **74%** of the catalog was produced post-2015.
- **Runtime Standards:** Film durations center normally around **98–100 minutes**.
- **TV Longevity:** **67.2%** of television series consist of only **1 Season**.

### 🔹 Task 3: Content-Based Recommendation System
- **Metadata Soup Architecture:** Merges `type`, doubled `listed_in`, `director`, `main_country`, and `rating`.
- **Similarity Metric:** Scalable linear kernel on normalized TF-IDF feature matrices.
- **Evaluation:** Evaluated on benchmark titles (`Midnight Mass`, `Ganglands`, `Sankofa`, `Dick Johnson Is Dead`, `Blood & Water`) achieving **55–80% average Jaccard Genre Overlap** across Top-10 recommendations.
- **Comparative Analysis:** Proven superior in precision compared to naive genre-only matching.

### 🔹 Task 5: Machine Learning Classification Model
- **Target:** Predict `type` (`Movie` = 0, `TV Show` = 1).
- **Leakage Prevention:** Strictly eliminated `duration` and all duration-derived features.
- **Pipeline Architecture:** Scikit-Learn `ColumnTransformer` with `TfidfVectorizer` (genres), `OneHotEncoder` (ratings & countries), and `StandardScaler` (release years).
- **Model Benchmark:**
  - **Random Forest:** Accuracy: **87.8%**, F1-Score: **80.0%**
  - **Logistic Regression (Champion tuned):** Accuracy: **85.3%**, F1-Score: **78.4%**
  - **Linear SVM:** Accuracy: **85.4%**, F1-Score: **78.5%**
  - **Gradient Boosting:** Accuracy: **86.1%**, F1-Score: **77.1%**
- **Interpretability:** Model coefficients show strong positive weights for serialized indicators (`tv dramas`, `crime tv shows`) and negative weights for movie categories (`documentaries`, `dramas`, `children & family`).

---

## 🛠️ Installation & Reproduction Guide

### 1. Clone & Set Up Environment
```bash
git clone <your-github-repo-url>
cd Netflix_Data_Intelligence_Platform

# Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate        # On Windows: .venv\Scripts\activate

# Install required dependencies
pip install -r requirements.txt
```

### 2. Run Notebooks
All 4 Jupyter notebooks can be opened and run sequentially:
```bash
jupyter lab
```
1. `backend/notebooks/01_data_cleaning.ipynb`
2. `backend/notebooks/02_exploratory_analysis.ipynb`
3. `backend/notebooks/03_recommendation_system.ipynb`
4. `backend/notebooks/04_classification_model.ipynb`

---

## 👥 Auspify Technologies Internship Details
- **Program:** 4-Week Remote Data Science Internship
- **Company:** Auspify Technologies ([www.auspify.com](http://www.auspify.com))
- **Hashtags:** `#Auspify #AuspifyTechnologies #AuspifyInternship #AuspifyProjects`


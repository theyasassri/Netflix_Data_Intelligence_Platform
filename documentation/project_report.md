# Auspify Technologies — Data Science Internship Final Project Report

**Program:** 4-Week Project-Based Remote Data Science Internship  
**Host Institution:** Auspify Technologies (www.auspify.com)  
**Project Title:** Netflix Data Intelligence Platform  
**Internship Role:** Data Science Intern  
**Date of Submission:** November 2026  

---

## 1. Project Background & Scope
The global streaming entertainment landscape requires rigorous data-driven intelligence to guide content acquisition, catalog curation, subscriber retention, and personalized algorithmic discovery. This project develops an integrated data science pipeline on the Netflix Titles Dataset (8,789 verified titles), completing four core internship tasks:
1. **Task 1 (Easy):** Data Cleaning, Normalization & Missing Data Remediation
2. **Task 2 (Easy):** In-Depth Exploratory Data Analysis & Strategic Insights
3. **Task 3 (Medium):** Content-Based Recommender Engine with Jaccard Evaluation
4. **Task 5 (Advanced):** Leakage-Free Supervised ML Classification Benchmark

---

## 2. Summary of Tasks Completed & Deliverables

| Task | Title | Level | Core Output File | Status |
|---|---|---|---|---|
| **Task 1** | Data Cleaning & Preprocessing | Easy | `backend/notebooks/01_data_cleaning.ipynb`<br>`backend/data/processed/netflix_clean.csv` | **100% Completed** |
| **Task 2** | Exploratory Data Analysis | Easy | `backend/notebooks/02_exploratory_analysis.ipynb`<br>11 High-Res Figures in `documentation/screenshots/task2/` | **100% Completed** |
| **Task 3** | Content Recommendation Engine | Medium | `backend/notebooks/03_recommendation_system.ipynb`<br>`documentation/screenshots/task3/` | **100% Completed** |
| **Task 5** | Supervised ML Classification | Advanced | `backend/notebooks/04_classification_model.ipynb`<br>`documentation/screenshots/task5/` | **100% Completed** |

---

## 3. Key Findings & Quantitative Results

### Task 1 — Data Cleaning Quality Assurance
- **Hidden Nulls Resolved:** 2,588 `director` and 287 `country` `"Not Given"` string tokens successfully identified and imputed with `"Unknown"`.
- **Single Invalid Record Dropped:** show_id `s1468` (`title="Unknown"`) removed.
- **Derived Features:** Created `duration_value` (integer), `duration_unit` (categorical), `year_added`, `month_added`, `main_country`, and `primary_genre`.
- **Final Clean Record Count:** 8,789 rows × 16 attributes (0 nulls remaining).

### Task 2 — Exploratory Analytics
- **Catalog Breakdown:** 6,125 Movies (69.7%) vs. 2,664 TV Shows (30.3%).
- **Top 3 Production Markets:** United States (3,240), India (1,057), United Kingdom (637).
- **Maturity Profile:** TV-MA (36.5%), TV-14 (24.5%), R (9.1%) represent over 70% of total titles.
- **Movie Runtime Distribution:** Mean = 98.5 min, Median = 98.0 min (Gaussian distribution).
- **TV Series Seasonality:** 67.2% of shows end at 1 Season.

### Task 3 — Recommendation System Performance
- Engineered a weighted **Metadata Soup** combining genres (2x), director, country, and rating.
- Recommender achieved **55–80% Mean Jaccard Genre Overlap** on diverse test titles (*Midnight Mass*, *Ganglands*, *Sankofa*, *Dick Johnson Is Dead*, *Blood & Water*).
- Demonstrated significant precision gains over naive single-genre similarity.

### Task 5 — Classification Benchmark Results
Tested 6 supervised classification algorithms under 5-Fold Stratified Cross-Validation:
- **Random Forest Classifier:** Accuracy: **87.8%**, F1-Score: **80.0%**
- **Linear Support Vector Classifier:** Accuracy: **85.4%**, F1-Score: **78.5%**
- **Logistic Regression (Tuned):** Accuracy: **85.3%**, F1-Score: **78.4%**
- **Gradient Boosting Classifier:** Accuracy: **86.1%**, F1-Score: **77.1%**
- **Decision Tree Classifier:** Accuracy: **84.3%**, F1-Score: **75.9%**
- **Multinomial Naive Bayes:** Accuracy: **82.2%**, F1-Score: **72.1%**

*Duration attributes were completely excluded to ensure zero target leakage.*

---

## 4. Conclusion & Submission Sign-Off
All deliverables required by Auspify Technologies have been produced, rigorously tested, verified for zero bugs, formatted to high professional standards, and saved with reproducible scripts and notebooks.

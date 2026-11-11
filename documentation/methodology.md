# Technical Methodology & Analytical Framework

**Project:** Netflix Data Intelligence Platform  
**Program:** Auspify Technologies Data Science Internship  

---

## 1. Data Cleaning & Feature Transformation (Task 1)
- **Missing Value Forensics:** Identified string placeholders (`"Not Given"`, `"Unknown"`) acting as pseudo-nulls. Converted to genuine `NaN`, then filled `director` and `country` with `"Unknown"` to retain sample integrity. Dropped 1 record with missing title.
- **Duration Disentanglement:** Decoupled mixed string runtimes into continuous scalar `duration_value` and categorical `duration_unit` (`min` vs. `Seasons`).
- **Temporal Feature Extraction:** Formatted `date_added` using ISO datetime parsing; extracted discrete `year_added` and `month_added`.
- **Primary Category Derivation:** Extracted leading atomic tokens for `main_country` and `primary_genre`.

## 2. Exploratory Data Analysis & Visualization (Task 2)
- Built 11 presentation-grade figures rendered via Matplotlib & Seaborn with custom Netflix branding palette (`#E50914`, `#221F1F`).
- Evaluated parametric distributions (KDE runtime estimates, normal fits), cross-tabulations (Genre × Content Type), and longitudinal trends (Year-over-Year acquisitions).

## 3. Content-Based Recommendation Architecture (Task 3)
- **Metadata Soup Formulation:**
  $$\text{Soup}_i = \text{Type}_i \parallel 2 \times \text{Genres}_i \parallel \text{Director}_i \parallel \text{Country}_i \parallel \text{Rating}_i$$
  Genres receive double weight to prioritize narrative style over origin country.
- **TF-IDF & Linear Kernel:**
  $$\text{TF-IDF}(t, d, D) = \text{TF}(t, d) \times \log\left(\frac{1 + |D|}{1 + |\{d \in D : t \in d\}|}\right) + 1$$
  $$\text{CosineSim}(\vec{u}, \vec{v}) = \frac{\vec{u} \cdot \vec{v}}{\|\vec{u}\|_2 \|\vec{v}\|_2} = \vec{u} \cdot \vec{v} \quad (\text{for normalized vectors})$$
- **Jaccard Evaluation Metric:**
  $$\text{Jaccard}(A, B) = \frac{|Genres_A \cap Genres_B|}{|Genres_A \cup Genres_B|}$$

## 4. Supervised Classification Framework (Task 5)
- **Target Leakage Safeguard:** Strictly discarded all duration attributes to ensure realistic operational prediction.
- **Unified Pipeline Preprocessing:**
  - `ColumnTransformer` with `TfidfVectorizer` (100 genre n-grams).
  - `OneHotEncoder` on `rating` and `main_country`.
  - `StandardScaler` on `release_year`, `year_added`, `month_added`.
- **Validation Protocol:** 5-Fold Stratified Cross-Validation ensuring balanced minority class (`TV Show` ~30.3%) representation across all folds.
- **Optimization:** Grid search hyperparameter tuning on champion linear classifiers with L2 regularization.


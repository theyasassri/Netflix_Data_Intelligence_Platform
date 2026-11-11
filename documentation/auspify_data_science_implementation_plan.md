# Auspify Data Science Internship — Implementation Plan

**Program:** 4-week remote, project-based internship (Auspify Technologies)
**Dataset:** Netflix titles dataset (used by all 6 tasks)
**Requirement:** Complete **any 4 of the 6 tasks**
**Tools:** Python, Pandas, Matplotlib/Seaborn, Scikit-Learn, Jupyter, Excel (optional)

---

## 1. What the Document Says (Analysis)

### 1.1 Program rules
| Item | Detail |
|---|---|
| Duration | 4 weeks, remote, flexible schedule |
| Tasks offered | 6 (2 Easy, 2 Medium, 2 Advanced) |
| Tasks required | Any 4 |
| Dataset | Netflix (not attached to the PDF, so it must be sourced) |
| Certificate depends on | Successful task completion, proper submission, basic project verification |
| Guidelines | Meet deadlines, original/plagiarism-free work, organized folder per task, professional communication |

### 1.2 The six tasks at a glance
| # | Level | Task | Core output |
|---|---|---|---|
| 1 | Easy | Data Cleaning & Preprocessing | `netflix_clean.csv` + cleaning notebook |
| 2 | Easy | Exploratory Data Analysis | Charts + written insights |
| 3 | Medium | Recommendation System | Content-based recommender + evaluation |
| 4 | Medium | Trend Prediction | Time-series forecast of content growth |
| 5 | Advanced | ML Classification Model | Trained, compared classifiers |
| 6 | Advanced | Business Insights Dashboard | End-to-end project + dashboard + report |

### 1.3 Dependencies between tasks
```
Task 1 (clean data) ──► feeds Tasks 2, 3, 4, 5, 6
Task 2 (EDA)        ──► informs Tasks 4, 5, 6
Task 6              ──► reuses work from 1, 2, 5 (and optionally 3, 4)
```
**Key insight:** Task 1 is the foundation for everything else, so it must be done first and done well.

### 1.4 Submission requirements
- Project source code
- Screenshots of completed tasks
- GitHub repository link (if available)
- Demo video (optional)
- A submission form/portal will be shared separately

### 1.5 Evaluation criteria (as listed)
Task Completion, Code Quality, Website Responsiveness, User Interface Design, Creativity & Implementation, Professional Presentation, Project Functionality.

> Note: "Website Responsiveness" and "User Interface Design" look like generic template criteria. They are most relevant if you do **Task 6 (dashboard)**. For the other tasks, focus on code quality, clarity, and presentation.

### 1.5.1 Gaps and ambiguities to resolve
- The Netflix dataset file is **not included** in the PDF.
- No **exact deadline** or portal link is given.
- Task 5 doesn't say what to classify ("based on available features").
- Task 4's forecasting method is not specified.

Ask `support@auspify.com` about the deadline and dataset source if they are not shared separately.

---

## 2. Choosing Your 4 Tasks

### Recommended: Tasks 1, 2, 3, 5
- **Why:** Covers cleaning, EDA, NLP/recommendation, and supervised ML — the most portfolio-relevant range of skills. Task 1 and 2 are quick, leaving more time for 3 and 5.

### Alternatives
| Option | Tasks | Best if you want |
|---|---|---|
| A (recommended) | 1, 2, 3, 5 | Broad ML + NLP showcase |
| B | 1, 2, 4, 5 | Time series + classification |
| C | 1, 2, 3, 4 | Lower risk, no advanced tasks |
| D | 1, 2, 5, 6 | Strongest "end-to-end" story, but heavier |

> Task 6 is effectively a capstone that combines other tasks. Choose it only if you are comfortable with a dashboard tool (Streamlit, Plotly Dash, or Power BI).

**Tip:** If time allows, finishing a 5th task is a bonus, but the requirement is only 4. Quality beats quantity.

---

## 3. Setup (Day 1)

### 3.1 Environment
```bash
python -m venv venv
source venv/bin/activate          # Windows: venv\Scripts\activate
pip install pandas numpy matplotlib seaborn scikit-learn jupyter nltk statsmodels
# Optional, depending on chosen tasks:
pip install plotly streamlit prophet xgboost
```

### 3.2 Folder structure (guideline: organized folders per task)
```
auspify-data-science-internship/
├── README.md
├── requirements.txt
├── data/
│   ├── raw/netflix_titles.csv
│   └── processed/netflix_clean.csv
├── task1_data_cleaning/
│   ├── task1_cleaning.ipynb
│   └── screenshots/
├── task2_eda/
├── task3_recommendation/
├── task5_classification/
├── (task4_forecasting/)  (task6_dashboard/)   # only if chosen
└── reports/
```

### 3.3 Git setup
```bash
git init
git add . && git commit -m "Initial project structure"
# create GitHub repo, then:
git remote add origin <repo-url>
git push -u origin main
```
Commit after each task with clear messages (e.g. `Task 1: add cleaning notebook and clean dataset`).

### 3.4 Get the dataset
The standard public version is the Kaggle "Netflix Movies and TV Shows" dataset, with columns: `show_id, type, title, director, cast, country, date_added, release_year, rating, duration, listed_in, description`. Confirm with Auspify that this is the intended file, then place it in `data/raw/`.

---

## 4. Four-Week Timeline (Recommended Plan: Tasks 1, 2, 3, 5)

| Week | Focus | Deliverables |
|---|---|---|
| **1** | Setup + **Task 1** + start **Task 2** | Repo, clean dataset, cleaning notebook, screenshots |
| **2** | Finish **Task 2** + start **Task 3** | EDA notebook with charts and written findings; recommender features built |
| **3** | Finish **Task 3** + **Task 5** | Working recommender with evaluation; classification pipeline trained |
| **4** | Finish Task 5, polish, submit | README, screenshots, final cleanup, LinkedIn posts, portal submission |

Build in a **buffer of 2–3 days** at the end for fixes and submission issues.

---

## 5. Detailed Task Plans

### Task 1 (Easy) — Data Cleaning & Preprocessing
**Goal:** Produce a clean, analysis-ready dataset.

| Step | Actions |
|---|---|
| 1. Import | `pd.read_csv()`, inspect with `.head()`, `.info()`, `.shape`, `.describe(include='all')` |
| 2. Find missing/duplicates | `df.isnull().sum()`, missing % per column, `df.duplicated().sum()`, check duplicate `show_id`/`title` |
| 3. Handle nulls & formats | `director`, `cast`, `country` → fill with `"Unknown"` (or drop where justified); `rating` → fill/mode or `"Unrated"`; fix stray whitespace; standardize text case; fix rating values that look like durations (a known issue in this dataset) |
| 4. Transform columns | Parse `date_added` with `pd.to_datetime(..., errors='coerce')` → extract `year_added`, `month_added`; split `duration` into numeric value + unit (min vs Seasons); split multi-valued `listed_in`, `country`, `cast` into lists; create `main_country`, `primary_genre` |
| 5. Save | Export `netflix_clean.csv`; document every decision |

**Deliverables:** cleaning notebook, `netflix_clean.csv`, before/after summary table, screenshots.
**Done when:** No unintended nulls, correct dtypes, no duplicates, decisions explained in markdown cells.

---

### Task 2 (Easy) — Exploratory Data Analysis
**Goal:** Uncover trends and patterns.

| Step | Actions |
|---|---|
| 1. Structure & stats | Shape, dtypes, summary statistics, value counts |
| 2. Content by type | Movies vs TV Shows (count/pie or bar) |
| 3. Top countries & categories | Top 10 countries, top genres, top directors/actors, rating distribution |
| 4. Visualizations | Content added per year, release year distribution, movie duration histogram, TV seasons count, genre vs type heatmap, monthly additions |
| 5. Summarize | 5–8 clear written insights |

**Deliverables:** EDA notebook, 8–12 clean charts (titled, labeled axes), findings summary.
**Done when:** Every chart has a one-line takeaway and the final summary reads like a short report.

---

### Task 3 (Medium) — Recommendation System
**Goal:** Content-based recommender using titles and categories.

| Step | Actions |
|---|---|
| 1. Extract features | Combine `listed_in`, `description`, `cast`, `director` (and `type`) into one text "soup" column |
| 2. Text preprocessing | Lowercase, remove punctuation/stopwords (NLTK), optional lemmatization |
| 3. Similarity | `TfidfVectorizer` → `cosine_similarity` (or `linear_kernel`) |
| 4. Recommendations | Function `recommend(title, n=10)` using a title→index map; test on 5+ titles |
| 5. Evaluate | See below |

**Evaluating quality (no user ratings exist):** genre overlap (Jaccard) between a title and its recommendations, manual inspection of examples, comparison of feature combinations (description-only vs genre+cast+description), and a short discussion of limitations (cold start, no user behavior data).

**Deliverables:** notebook, `recommend()` function, example outputs, evaluation table.

---

### Task 4 (Medium) — Trend Prediction *(if chosen)*
1. Aggregate titles per `release_year` (and/or `year_added`), split by type.
2. Plot yearly trends; **exclude or flag the latest incomplete year**.
3. Build models: linear/polynomial regression baseline, ARIMA/SARIMA or Holt-Winters (`statsmodels`), optional Prophet.
4. Use a time-based holdout (last 3–5 years) and compare **MAE/RMSE**.
5. Forecast 3–5 years ahead with confidence intervals; interpret results and caveats (small sample, structural breaks like 2020).

---

### Task 5 (Advanced) — ML Classification Model
**Goal:** Train and compare classifiers.

**Choose a clear target (state it explicitly in the notebook):**
- Option 1: `type` (Movie vs TV Show)
- Option 2: `rating` grouped into categories (e.g. Kids / Teens / Adults)
- Option 3: Primary genre

> **Avoid target leakage.** If predicting `type`, do **not** use `duration` as a feature as it directly reveals the answer (minutes vs seasons). Use `description` (TF-IDF), `listed_in`, `country`, `release_year`, `rating`, `cast`/`director` presence, etc.

| Step | Actions |
|---|---|
| 1. Features | TF-IDF on text, one-hot/target encoding for categories, numeric features; `ColumnTransformer` + `Pipeline` |
| 2. Split | `train_test_split(test_size=0.2, stratify=y, random_state=42)` |
| 3. Train | Logistic Regression, Decision Tree, Random Forest, Naive Bayes, SVM, optionally XGBoost |
| 4. Evaluate | Accuracy, precision, recall, F1, confusion matrix, ROC-AUC (binary), 5-fold cross-validation |
| 5. Compare | Results table + bar chart; pick best model; light hyperparameter tuning (`GridSearchCV`) |

**Class imbalance:** Movies outnumber TV shows (~70/30) so report F1 alongside accuracy and consider `class_weight='balanced'`.

**Deliverables:** notebook, model comparison table, confusion matrix, feature-importance plot, conclusion.

---

### Task 6 (Advanced) — Business Insights Dashboard *(if chosen)*
1. Consolidate the analysis from Tasks 1–5.
2. Add a predictive component (classifier and/or forecast).
3. Build an interactive dashboard (Streamlit, Plotly Dash, or Power BI) with filters for type, country, genre, and year.
4. Write business recommendations (e.g. content-mix strategy, regional focus, release timing).
5. Produce a professional PDF/Markdown report and a short demo video.

---

## 6. Standard Workflow for Every Task
1. Re-read the task's 5 steps and turn them into notebook section headings.
2. Write code in small, commented cells; use markdown cells to explain *why*.
3. Keep results reproducible (`random_state=42`, relative file paths).
4. Take **clear screenshots** of key outputs (code + result) into the task's `screenshots/` folder.
5. Write a 5–10 line summary at the end of the notebook.
6. Commit to GitHub.
7. Post a short progress update (see section 9).

### Code quality checklist (maps to "Code Quality" criterion)
- [ ] Meaningful variable names, no dead code
- [ ] Functions for repeated logic
- [ ] Notebook runs top-to-bottom without errors (Restart & Run All)
- [ ] `requirements.txt` included
- [ ] Original work only (plagiarism-free)

---

## 7. Submission Checklist

- [ ] Source code (notebooks + any `.py` files) for **4 completed tasks**
- [ ] Screenshots of each completed task
- [ ] GitHub repository link (public, with a good README)
- [ ] Clean dataset and any outputs/reports
- [ ] Optional: demo video (3–5 min walkthrough)
- [ ] Submit through the portal/form Auspify shares
- [ ] Keep a copy of everything and the submission confirmation

### README structure
1. Project title and overview
2. Tasks completed (with links)
3. Dataset description
4. Key findings (3–5 bullets)
5. How to run
6. Tech stack
7. Screenshots

---

## 8. Mapping Work to Evaluation Criteria

| Criterion | How to score well |
|---|---|
| Task Completion | Cover all 5 steps of each chosen task, explicitly labeled |
| Code Quality | Clean, commented, reproducible notebooks |
| Website Responsiveness / UI Design | Only if doing Task 6; use a clean, filterable layout that works on mobile widths |
| Creativity & Implementation | Extra feature engineering, model comparison, thoughtful insights |
| Professional Presentation | Titled charts, written conclusions, tidy README, good screenshots |
| Project Functionality | Everything runs end-to-end; recommender and models return sensible output |

---

## 9. Professional Showcase (Optional but Encouraged)
Post progress on LinkedIn with screenshots/demos. Use hashtags: `#Auspify #AuspifyTechnologies #AuspifyInternship #AuspifyProjects`

Suggested posts: (1) Week 1 cleaning/EDA insights, (2) recommender demo, (3) model comparison results, (4) final wrap-up with GitHub link. Tag the company page `@auspify-technologies`.

---

## 10. Risks and How to Avoid Them

| Risk | Mitigation |
|---|---|
| Dataset not provided | Use Kaggle Netflix dataset; confirm with support |
| Missing deadline | Email `support@auspify.com`; plan to finish within 4 weeks anyway |
| Running out of time | Do Tasks 1–2 first (quick wins); keep buffer days |
| Target leakage in Task 5 | Exclude `duration` when predicting `type` |
| Inflated accuracy from imbalance | Report F1/confusion matrix |
| Messy notebooks | Restart & Run All before screenshots/submission |
| Plagiarism flags | Write your own code/commentary; cite any references |

---

## 11. Immediate Next Steps
1. Confirm which 4 tasks you will do (recommended: 1, 2, 3, 5).
2. Get the Netflix dataset and set up the repo/environment.
3. Complete **Task 1** and save `netflix_clean.csv`.
4. Start Task 2 using the clean dataset.

**Contact:** support@auspify.com · www.auspify.com · LinkedIn: @auspify-technologies

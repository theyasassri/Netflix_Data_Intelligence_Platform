import numpy as np
import pandas as pd
from typing import Dict, Any
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from .data_service import DataService

class PredictionService:
    _pipeline = None
    _is_trained = False

    @classmethod
    def train_or_load(cls):
        if cls._is_trained:
            return

        df = DataService.get_df()
        
        # Binary target: TV Show = 1, Movie = 0
        df['target'] = (df['type'] == 'TV Show').astype(int)

        feature_cols = ['listed_in', 'rating', 'main_country', 'release_year', 'year_added', 'month_added']
        X = df[feature_cols].copy()
        y = df['target'].copy()

        preprocessor = ColumnTransformer(
            transformers=[
                ('text', TfidfVectorizer(max_features=100, ngram_range=(1, 2)), 'listed_in'),
                ('cat', OneHotEncoder(handle_unknown='ignore', sparse_output=False), ['rating', 'main_country']),
                ('num', StandardScaler(), ['release_year', 'year_added', 'month_added'])
            ],
            remainder='drop'
        )

        cls._pipeline = Pipeline(steps=[
            ('preprocessor', preprocessor),
            ('classifier', LogisticRegression(class_weight='balanced', C=1.0, max_iter=1000, random_state=42))
        ])

        cls._pipeline.fit(X, y)
        cls._is_trained = True

    @classmethod
    def predict_content_type(
        cls,
        listed_in: str,
        rating: str = "TV-MA",
        main_country: str = "United States",
        release_year: int = 2021,
        year_added: int = 2021,
        month_added: int = 9
    ) -> Dict[str, Any]:
        cls.train_or_load()

        input_df = pd.DataFrame([{
            'listed_in': listed_in,
            'rating': rating,
            'main_country': main_country,
            'release_year': release_year,
            'year_added': year_added,
            'month_added': month_added
        }])

        proba = cls._pipeline.predict_proba(input_df)[0]
        prob_movie = float(proba[0])
        prob_tv = float(proba[1])

        pred_label = "TV Show" if prob_tv >= 0.5 else "Movie"
        confidence = max(prob_movie, prob_tv) * 100

        return {
            "predicted_type": pred_label,
            "probability_movie": round(prob_movie, 4),
            "probability_tv_show": round(prob_tv, 4),
            "confidence_pct": round(confidence, 2)
        }


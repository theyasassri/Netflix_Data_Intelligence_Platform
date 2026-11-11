import re
import numpy as np
import pandas as pd
from typing import List, Dict, Any, Optional
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
from .data_service import DataService

def clean_token(val: Any) -> str:
    if pd.isna(val) or val == 'Unknown':
        return ''
    return str(val).lower().replace(' ', '').replace(',', ' ')

class RecommendationService:
    _tfidf_matrix = None
    _vectorizer = None
    _indices = None
    _is_initialized = False

    @classmethod
    def initialize(cls):
        if cls._is_initialized:
            return
            
        df = DataService.get_df()
        
        # Build soup
        soup_type = df['type'].apply(clean_token)
        soup_director = df['director'].apply(clean_token)
        soup_country = df['main_country'].apply(clean_token)
        soup_rating = df['rating'].apply(clean_token)
        soup_genres = df['listed_in'].apply(lambda x: ' '.join([clean_token(g) for g in str(x).split(',')]))

        df['metadata_soup'] = (
            soup_type + ' ' +
            soup_genres + ' ' +
            soup_genres + ' ' +
            soup_director + ' ' +
            soup_country + ' ' +
            soup_rating
        ).str.strip()

        cls._vectorizer = TfidfVectorizer(stop_words='english', min_df=1, ngram_range=(1, 2))
        cls._tfidf_matrix = cls._vectorizer.fit_transform(df['metadata_soup'])
        cls._indices = pd.Series(df.index, index=df['title'].str.lower()).drop_duplicates()
        cls._is_initialized = True

    @classmethod
    def recommend(cls, title: str, n: int = 10) -> List[Dict[str, Any]]:
        cls.initialize()
        df = DataService.get_df()
        title_clean = title.strip().lower()

        if title_clean not in cls._indices:
            matches = cls._indices.index[cls._indices.index.str.contains(re.escape(title_clean))]
            if len(matches) == 0:
                return []
            title_clean = matches[0]

        idx = cls._indices[title_clean]
        sim_scores = linear_kernel(cls._tfidf_matrix[idx], cls._tfidf_matrix).flatten()
        top_indices = sim_scores.argsort()[::-1][1:n+1]

        results = []
        for i in top_indices:
            row = df.iloc[i]
            results.append({
                "title": row['title'],
                "type": row['type'],
                "primary_genre": row['primary_genre'],
                "director": row['director'],
                "main_country": row['main_country'],
                "release_year": int(row['release_year']),
                "similarity_score": round(float(sim_scores[i]), 4)
            })

        return results

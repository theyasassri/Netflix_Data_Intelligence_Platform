from dataclasses import dataclass, field
from typing import List, Optional, Dict, Any

@dataclass
class TitleItem:
    show_id: str
    type: str
    title: str
    director: str
    country: str
    date_added: str
    release_year: int
    rating: str
    duration: str
    listed_in: str
    duration_value: int
    duration_unit: str
    year_added: int
    month_added: int
    main_country: str
    primary_genre: str

@dataclass
class RecommendationRequest:
    title: str
    n_recommendations: int = 10

@dataclass
class RecommendationResult:
    title: str
    type: str
    primary_genre: str
    director: str
    main_country: str
    release_year: int
    similarity_score: float

@dataclass
class ClassificationRequest:
    listed_in: str
    rating: str = "TV-MA"
    main_country: str = "United States"
    release_year: int = 2021
    year_added: int = 2021
    month_added: int = 9

@dataclass
class ClassificationResult:
    predicted_type: str
    probability_movie: float
    probability_tv_show: float
    confidence_pct: float


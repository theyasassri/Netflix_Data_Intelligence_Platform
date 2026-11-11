from typing import Dict, Any, List
from .data_service import DataService

class AnalyticsService:
    @classmethod
    def get_catalog_overview(cls) -> Dict[str, Any]:
        df = DataService.get_df()
        type_counts = df['type'].value_counts().to_dict()
        total = len(df)
        
        return {
            "total_titles": total,
            "movies_count": type_counts.get("Movie", 0),
            "tv_shows_count": type_counts.get("TV Show", 0),
            "movie_percentage": round(type_counts.get("Movie", 0) / total * 100, 2),
            "tv_show_percentage": round(type_counts.get("TV Show", 0) / total * 100, 2),
            "unique_countries": int(df['main_country'].nunique()),
            "unique_primary_genres": int(df['primary_genre'].nunique()),
            "earliest_release_year": int(df['release_year'].min()),
            "latest_release_year": int(df['release_year'].max()),
        }

    @classmethod
    def get_top_countries(cls, limit: int = 10) -> List[Dict[str, Any]]:
        df = DataService.get_df()
        top = (
            df[df['main_country'] != 'Unknown']['main_country']
            .value_counts()
            .head(limit)
        )
        return [{"country": k, "count": int(v)} for k, v in top.items()]

    @classmethod
    def get_top_genres(cls, limit: int = 10) -> List[Dict[str, Any]]:
        df = DataService.get_df()
        top = df['primary_genre'].value_counts().head(limit)
        return [{"genre": k, "count": int(v)} for k, v in top.items()]

    @classmethod
    def get_ratings_breakdown(cls) -> List[Dict[str, Any]]:
        df = DataService.get_df()
        ratings = df['rating'].value_counts()
        return [{"rating": k, "count": int(v), "percentage": round(int(v)/len(df)*100, 2)} for k, v in ratings.items()]


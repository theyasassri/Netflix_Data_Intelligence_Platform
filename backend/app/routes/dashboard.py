from typing import Dict, Any
from ..services.analytics_service import AnalyticsService

def handle_get_dashboard_summary() -> Dict[str, Any]:
    overview = AnalyticsService.get_catalog_overview()
    top_countries = AnalyticsService.get_top_countries(limit=8)
    top_genres = AnalyticsService.get_top_genres(limit=8)
    ratings = AnalyticsService.get_ratings_breakdown()

    return {
        "status": "success",
        "overview": overview,
        "top_countries": top_countries,
        "top_genres": top_genres,
        "ratings": ratings[:6]
    }


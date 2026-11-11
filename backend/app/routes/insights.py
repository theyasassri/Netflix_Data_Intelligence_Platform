from typing import Dict, Any
from ..services.analytics_service import AnalyticsService

def handle_get_overview() -> Dict[str, Any]:
    return {
        "status": "success",
        "data": AnalyticsService.get_catalog_overview()
    }

def handle_get_top_countries(limit: int = 10) -> Dict[str, Any]:
    return {
        "status": "success",
        "data": AnalyticsService.get_top_countries(limit=limit)
    }

def handle_get_top_genres(limit: int = 10) -> Dict[str, Any]:
    return {
        "status": "success",
        "data": AnalyticsService.get_top_genres(limit=limit)
    }

def handle_get_ratings() -> Dict[str, Any]:
    return {
        "status": "success",
        "data": AnalyticsService.get_ratings_breakdown()
    }

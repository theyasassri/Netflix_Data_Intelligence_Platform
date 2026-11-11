from typing import Dict, Any
from ..services.recommendation_service import RecommendationService

def handle_get_recommendations(title: str, n: int = 10) -> Dict[str, Any]:
    if not title:
        return {"status": "error", "message": "Missing 'title' query parameter"}
    
    recs = RecommendationService.recommend(title=title, n=n)
    if not recs:
        return {
            "status": "not_found",
            "message": f"No recommendations found for title '{title}'. Try another title or substring."
        }
    
    return {
        "status": "success",
        "query_title": title,
        "count": len(recs),
        "data": recs
    }

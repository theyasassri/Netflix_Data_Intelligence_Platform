from typing import Dict, Any
from ..services.data_service import DataService

def handle_search_titles(query: str = "", content_type: str = "", limit: int = 20) -> Dict[str, Any]:
    titles = DataService.search_titles(query=query, content_type=content_type, limit=limit)
    return {
        "status": "success",
        "count": len(titles),
        "data": titles
    }

def handle_get_title(show_id: str) -> Dict[str, Any]:
    title = DataService.get_by_show_id(show_id)
    if not title:
        return {"status": "error", "message": f"Show ID '{show_id}' not found"}
    return {"status": "success", "data": title}

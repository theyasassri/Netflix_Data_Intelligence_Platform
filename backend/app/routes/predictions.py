from typing import Dict, Any
from ..services.prediction_service import PredictionService

def handle_classify_content(payload: Dict[str, Any]) -> Dict[str, Any]:
    listed_in = payload.get("listed_in", "")
    if not listed_in:
        return {"status": "error", "message": "Field 'listed_in' is required."}

    rating = payload.get("rating", "TV-MA")
    main_country = payload.get("main_country", "United States")
    release_year = int(payload.get("release_year", 2021))
    year_added = int(payload.get("year_added", 2021))
    month_added = int(payload.get("month_added", 9))

    result = PredictionService.predict_content_type(
        listed_in=listed_in,
        rating=rating,
        main_country=main_country,
        release_year=release_year,
        year_added=year_added,
        month_added=month_added
    )

    return {
        "status": "success",
        "input": {
            "listed_in": listed_in,
            "rating": rating,
            "main_country": main_country,
            "release_year": release_year
        },
        "prediction": result
    }

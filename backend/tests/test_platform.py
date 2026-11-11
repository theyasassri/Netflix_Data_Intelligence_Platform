"""
Unit tests for the Netflix Data Intelligence Platform.
Tests data integrity, analytics, recommender logic, and ML classifier.
Utilizes Python standard library unittest.
"""
import unittest
import sys
from pathlib import Path

backend_dir = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(backend_dir))

from app.services.data_service import DataService
from app.services.analytics_service import AnalyticsService
from app.services.recommendation_service import RecommendationService
from app.services.prediction_service import PredictionService

class TestNetflixPlatform(unittest.TestCase):
    def test_data_service_loaded(self):
        df = DataService.get_df()
        self.assertEqual(len(df), 8789)
        self.assertEqual(df.isnull().sum().sum(), 0)
        self.assertIn("primary_genre", df.columns)
        self.assertIn("main_country", df.columns)

    def test_data_search(self):
        results = DataService.search_titles(query="Midnight Mass", limit=1)
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]['title'], "Midnight Mass")
        self.assertEqual(results[0]['type'], "TV Show")

    def test_analytics_overview(self):
        overview = AnalyticsService.get_catalog_overview()
        self.assertEqual(overview['total_titles'], 8789)
        self.assertEqual(overview['movies_count'], 6125)
        self.assertEqual(overview['tv_shows_count'], 2664)
        self.assertGreater(overview['movie_percentage'], 69.0)

    def test_recommender(self):
        recs = RecommendationService.recommend(title="Midnight Mass", n=5)
        self.assertEqual(len(recs), 5)
        rec_titles = [r['title'] for r in recs]
        self.assertTrue(any("Haunting" in t for t in rec_titles))

    def test_classifier_tv_show(self):
        pred = PredictionService.predict_content_type(
            listed_in="TV Dramas, Crime TV Shows, International TV Shows",
            rating="TV-MA"
        )
        self.assertEqual(pred['predicted_type'], "TV Show")
        self.assertGreater(pred['probability_tv_show'], 0.8)

    def test_classifier_movie(self):
        pred = PredictionService.predict_content_type(
            listed_in="Documentaries, Feature Films",
            rating="PG-13"
        )
        self.assertEqual(pred['predicted_type'], "Movie")
        self.assertGreater(pred['probability_movie'], 0.7)

if __name__ == "__main__":
    unittest.main()

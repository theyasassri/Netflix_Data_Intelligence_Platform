import pandas as pd
from pathlib import Path
from typing import List, Dict, Any, Optional

DATA_PATH = Path(__file__).resolve().parent.parent.parent / "data" / "processed" / "netflix_clean.csv"

class DataService:
    _instance = None
    _df: Optional[pd.DataFrame] = None

    @classmethod
    def get_df(cls) -> pd.DataFrame:
        if cls._df is None:
            if not DATA_PATH.exists():
                raise FileNotFoundError(f"Clean dataset not found at {DATA_PATH}")
            cls._df = pd.read_csv(DATA_PATH)
        return cls._df

    @classmethod
    def search_titles(cls, query: str = "", content_type: str = "", limit: int = 20) -> List[Dict[str, Any]]:
        df = cls.get_df()
        filtered = df
        if content_type:
            filtered = filtered[filtered['type'].str.lower() == content_type.lower()]
        if query:
            filtered = filtered[filtered['title'].str.contains(query, case=False, na=False)]
        return filtered.head(limit).to_dict(orient="records")

    @classmethod
    def get_by_show_id(cls, show_id: str) -> Optional[Dict[str, Any]]:
        df = cls.get_df()
        match = df[df['show_id'] == show_id]
        if match.empty:
            return None
        return match.iloc[0].to_dict()


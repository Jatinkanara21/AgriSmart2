from pathlib import Path
from functools import lru_cache

MODEL_ROOT = Path(__file__).resolve().parents[3] / "ml" / "models"

@lru_cache
def load_crop_model():
    path = MODEL_ROOT / "crop_recommendation.joblib"
    if not path.exists():
        return None
    import joblib
    return joblib.load(path)

@lru_cache
def load_yield_model():
    path = MODEL_ROOT / "yield_prediction.joblib"
    if not path.exists():
        return None
    import joblib
    return joblib.load(path)

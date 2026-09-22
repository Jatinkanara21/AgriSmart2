import joblib

FEATURES = ["N", "P", "K", "temperature", "humidity", "ph", "rainfall"]

class CropRecommendationModel:
    def __init__(self, model_path: str):
        self.model = joblib.load(model_path)

    def predict(self, values: dict):
        row = [[values[name] for name in FEATURES]]
        prediction = self.model.predict(row)[0]
        probabilities = self.model.predict_proba(row)[0]
        confidence = float(max(probabilities))
        return {"crop": str(prediction), "confidence": confidence}

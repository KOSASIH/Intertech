from app.models.prediction_model import PredictionModel
from app.utils.preprocessing import preprocess_data

class PredictionService:
    @staticmethod
    def predict(data):
        preprocessed_data = preprocess_data(data)
        model = PredictionModel(model_path='path_to_model')
        prediction = model.predict(preprocessed_data)
        return prediction

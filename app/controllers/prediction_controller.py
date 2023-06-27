from flask import Blueprint, jsonify, request
from app.services.prediction_service import PredictionService

prediction_blueprint = Blueprint('prediction', __name__)

@prediction_blueprint.route('/predict', methods=['POST'])
def predict():
    data = request.json
    prediction = PredictionService.predict(data)
    return jsonify(prediction)

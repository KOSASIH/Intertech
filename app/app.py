from flask import Flask
from app.controllers.prediction_controller import prediction_blueprint

app = Flask(__name__)
app.register_blueprint(prediction_blueprint)

if __name__ == '__main__':
    app.run()

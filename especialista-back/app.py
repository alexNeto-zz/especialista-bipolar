from flask import Flask
from flask_cors import CORS

from api.test import test_blueprint
from bipolar.mania.mania_controller import mania_blueprint

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

app.register_blueprint(test_blueprint)
app.register_blueprint(mania_blueprint, url_prefix='/mania')

if __name__ == "__main__":
    app.run()

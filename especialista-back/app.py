from flask import Flask

from api.test import test_blueprint

app = Flask(__name__)

app.register_blueprint(test_blueprint)

if __name__ == '__main__':
    app.run()

from flask import Flask
from flask_sockets import Sockets

from api.test import test_blueprint
from bipolar.mania_engine import mania

app = Flask(__name__)
sockets = Sockets(app)

app.register_blueprint(test_blueprint)
sockets.register_blueprint(mania, url_prefix='/mania')

if __name__ == "__main__":
    from gevent import pywsgi
    from geventwebsocket.handler import WebSocketHandler

    server = pywsgi.WSGIServer(('', 5000), app, handler_class=WebSocketHandler)
    server.serve_forever()

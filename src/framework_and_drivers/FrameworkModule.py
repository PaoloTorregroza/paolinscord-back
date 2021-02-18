from flask_socketio import SocketIO
from flask import Flask
from settings import SECRET_KEY
from src.framework_and_drivers.libs.socketio_config import SocketioConfig
from src.framework_and_drivers.libs.flask_routes import api_blueprint
from src.framework_and_drivers.libs.mongo_config import MongoDatabase


class FrameworkModule:
    def __init__(self):
        self.app = Flask(__name__)
        self.app.config['SECRET_KEY'] = SECRET_KEY
        self.app.register_blueprint(api_blueprint)
        self.socketio = SocketIO(self.app, cors_allowed_origins="*")
        self.socketio_config = SocketioConfig(self.socketio)
        self.database = MongoDatabase()

    def runApp(self):
        self.socketio.run(self.app)

from flask_socketio import SocketIO


class SocketioConfig:
    def __init__(self, socketio: SocketIO):
        self.socketio = socketio
        self.config_socketio(self.socketio)

    def config_socketio(self, socketio: SocketIO):
        @socketio.on("testEvent")
        def handle_test_event(self, json, methods=["GET", "POST"]):
            print('received event: ' + str(json))
            self.socketio.emit(
                'my response',
                json,
                callback=self.message_received
            )

        def message_received():
            print("WOW")

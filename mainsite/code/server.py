import threading
import time

class Server:
    max_capacity = 0
    current = 0
    server = True

    @staticmethod
    def change_():

    @staticmethod
    def start():
        thread = threading.Thread(target=Server.reset_capacity)
        thread.daemon = True
        thread.start()

    @staticmethod
    def reset_capacity():
        while True:
            time.sleep(60)
            if Server.current > Server.max_capacity:
                Server.current = 0
                Server.server = False
            else:
                Server.current = 0
                Server.server = True

    @staticmethod
    def get_server_capacity():
        return Server.server

    @staticmethod
    def update_server():
        Server.current += 1

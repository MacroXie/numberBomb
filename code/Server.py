import threading
import time

class Server:
    def __init__(self, max_capacity_per_min):
        self.max_capacity = max_capacity_per_min
        self.current = 0
        self.server = True

        thread = threading.Thread(target=self.reset_capacity)
        thread.daemon = True
        thread.start()

    def reset_capacity(self):
        while True:
            time.sleep(60)
            if self.current > self.max_capacity:
                self.current = 0
                self.server = False
            else:
                self.current = 0
                self.server = True

    def get_server_capacity(self):
        return self.server

    def update_server(self):
        self.current += 1



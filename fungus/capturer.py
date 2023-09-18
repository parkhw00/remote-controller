
import threading

class Singleton:
    _instance = None
    _lock = threading.Lock()
    _user = 0

    def getInstance(self, *args, **kwargs):
        with self._lock:
            if not self._instance:
                self._instance = self(args, kwargs)
            self._user ++

        return self._instance

    def putInstance(self):
        with self._lock:
            self._user --
            if self._user == 0:
                del self._instance
                self._instance = None


class Capturer(Singleton):

    def __init__(self):
        pass

    def get(self):
        pass

    def put(self):
        pass

from threading import Lock, Thread

class DataBaseMeta(type):
    _instances = {}
    _lock: Lock = Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                # create instance and store it in _instances
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]

class DataBase(metaclass=DataBaseMeta):
    _value: str = None
    def __init__(self, value):
        self._value = value
    def getValue(self):
        return self._value
    def setValue(self, value):
        self._value = value
    def __str__(self):
        return self._value


# test code
def test_singleton(value):
    singleton = DataBase(value)
    print(singleton.getValue())

if __name__ == "__main__":
    print("If you see the same value, then singleton was reused (yay!)\n"
          "If you see different values, then 2 singletons were created (booo!!)\n\n"
          "RESULT:\n")
    process1 = Thread(target=test_singleton, args=("FOO",))
    process2 = Thread(target=test_singleton, args=("BAR",))
    process1.start()
    process2.start()
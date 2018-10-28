import abc


class InputImporter(abc.ABC):
    def __init__(self, interpreter):
        self._interpreter = interpreter

    @abc.abstractmethod
    def get_entries(self):
        pass

import abc


class InputImporter(abc.ABC):
    @abc.abstractmethod
    def get_entries(self):
        pass

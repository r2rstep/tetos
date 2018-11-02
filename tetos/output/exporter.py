import abc


class Exporter(abc.ABC):
    @abc.abstractmethod
    def export(self, entries: list):
        pass

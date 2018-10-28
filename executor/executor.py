from input_importer.importer_factory import get_importer


class Executor(object):
    def __init__(self, input_path):
        self._input = input_path
        self._importer = get_importer(self._input)

    def execute(self):
        entries = self._importer.get_text()

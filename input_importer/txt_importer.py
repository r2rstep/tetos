from input_importer.input_importer import InputImporter


class TxtImporter(InputImporter):
    def __init__(self, file):
        self._file_path = file

    def get_entries(self):
        with open(self._file_path) as f:
            return f.readlines()

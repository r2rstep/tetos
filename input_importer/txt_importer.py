from input_importer.input_importer import InputImporter


class TxtImporter(InputImporter):
    def __init__(self, file, interpreter):
        InputImporter.__init__(interpreter)
        self._file_path = file

    def get_entries(self):
        return self._file_path.readlines()

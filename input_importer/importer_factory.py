from input_importer.input_importer import InputImporter
from input_importer.txt_importer import TxtImporter


def get_importer(input_path) -> InputImporter:
    return TxtImporter(input_path)

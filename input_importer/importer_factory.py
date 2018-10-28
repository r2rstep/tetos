from input_importer.input_importer import InputImporter
from input_importer.txt_importer import TxtImporter
from interpreter.interpreter import Interpreter


def get_importer(input_path, interpreter: Interpreter) -> InputImporter:
    return TxtImporter(file, interpreter)

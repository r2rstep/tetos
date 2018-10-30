from input_importer.input_importer import InputImporter
from input_importer.importers import TxtImporter, HtmlImporter


def get_importer(input_path) -> InputImporter:
    if 'txt' == input_path.split('.')[-1]:
        importer = TxtImporter(input_path)
    else:
        importer = HtmlImporter(input_path)
    return importer

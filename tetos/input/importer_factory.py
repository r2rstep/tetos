from tetos.input.input_importer import InputImporter
from tetos.input.importers import TxtImporter, HtmlImporter
from tetos.utils.fetchers import fetch_html


def get_importer(input_path) -> InputImporter:
    if 'txt' == input_path.split('.')[-1]:
        importer = TxtImporter(input_path)
    else:
        importer = HtmlImporter(input_path, fetch_html)
    return importer

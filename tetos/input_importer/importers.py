from tetos.input_importer.input_importer import InputImporter
from utils.html_fetcher import fetch_html

import html2text


class HtmlImporter(InputImporter):
    def __init__(self, file):
        self._file_path = file

    def get_entries(self):
        htmls = fetch_html(self._file_path)
        text_maker = html2text.HTML2Text()
        # otherwise some text may end up in a new line
        text_maker.body_width = 0
        text_maker.ignore_emphasis = True
        text = []
        for html in htmls:
            text.extend([text_maker.handle(html)])
        return list(filter(None, (line.rstrip() for t in text for line in t.splitlines())))


class TxtImporter(InputImporter):
    def __init__(self, file):
        self._file_path = file

    def get_entries(self):
        with open(self._file_path) as f:
            return list(filter(None, (line.rstrip() for line in f)))

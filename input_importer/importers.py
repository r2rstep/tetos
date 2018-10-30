from input_importer.input_importer import InputImporter

import html2text


class HtmlImporter(InputImporter):
    def __init__(self, file):
        self._file_path = file

    def get_entries(self):
        with open(self._file_path, encoding='iso-8859-2') as html_file:
            html = html_file.read()
        text_maker = html2text.HTML2Text()
        # otherwise some text may end up in a new line
        text_maker.body_width = 0
        text_maker.ignore_emphasis = True
        text = text_maker.handle(html)
        return list(filter(None, (line.rstrip() for line in text.splitlines())))


class TxtImporter(InputImporter):
    def __init__(self, file):
        self._file_path = file

    def get_entries(self):
        with open(self._file_path) as f:
            return list(filter(None, (line.rstrip() for line in f)))

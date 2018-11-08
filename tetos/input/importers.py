from tetos.input.input_importer import InputImporter

import html2text


class HtmlImporter(InputImporter):
    def __init__(self, file, fetcher):
        self._file_path = file
        self._fetch_html = fetcher

    def get_entries(self):
        htmls = self._fetch_html(self._file_path)
        text_maker = html2text.HTML2Text()
        # otherwise some text may end up in a new line
        text_maker.body_width = 0
        text_maker.ignore_emphasis = True
        text = []
        for html in htmls:
            text.extend([text_maker.handle(html)])
        return list(filter(None, (line.rstrip() for t in text for line in t.splitlines())))


class TxtImporter(InputImporter):
    def __init__(self, file, fetcher):
        self._file_path = file
        self._fetch = fetcher

    def get_entries(self):
        f = self._fetch(self._file_path)
        return list(filter(None, (line.rstrip() for line in f)))

from exporter.exporter import Exporter
from utils.http import escape_http_special_characters


import webbrowser


class PlaylistConverterExporter(Exporter):
    def __init__(self):
        self._base_url = 'http://www.playlist-converter.net/#/freetext='
        self._encoded_newline = '%0A'

    def export(self, entries: dict):
        url = self._base_url
        for entry in entries:
            artist = escape_http_special_characters(entry['artist'])
            title = escape_http_special_characters(entry['title'])
            url += artist + ' - ' + title + self._encoded_newline
        url = url.rstrip(self._encoded_newline)
        webbrowser.open(url)

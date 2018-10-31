from exporter.exporter import Exporter
from utils.http_utils import encode_http_special_characters


import webbrowser


class PlaylistConverterExporter(Exporter):
    def __init__(self):
        self._base_url = 'http://www.playlist-converter.net/#/freetext='
        self._encoded_newline = '%0A'

    def export(self, entries: dict):
        url = self._base_url
        for entry in entries:
            artist = self._slash_workaround(entry['artist'])
            artist = encode_http_special_characters(artist)
            title = self._slash_workaround(entry['title'])
            title = encode_http_special_characters(title)
            url += artist + ' - ' + title + self._encoded_newline
        url = url.rstrip(self._encoded_newline)
        webbrowser.open(url)

    def _slash_workaround(self, s: str):
        # for some reason PlaylistConverter has problems with slashes, even http-encoded
        return s.replace('/', ' ')

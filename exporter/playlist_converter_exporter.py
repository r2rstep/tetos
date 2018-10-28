from exporter.exporter import Exporter


import webbrowser


class PlaylistConverterExporter(Exporter):
    def __init__(self):
        self._base_url = 'http://www.playlist-converter.net/#/freetext='

    def export(self, entries: dict):
        url = self._base_url + entries[0]['artist'] + '-' + entries[0]['title']
        webbrowser.open(url)

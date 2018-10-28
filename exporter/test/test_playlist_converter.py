from exporter.playlist_converter_exporter import PlaylistConverterExporter

from unittest.case import TestCase
from mock import patch


@patch('exporter.playlist_converter_exporter.webbrowser')
class TestPlaylistConverter(TestCase):
    def test_export(self, webbrowser):
        entries = [{'artist': 'artist',
                    'title': 'title'}]
        exporter = PlaylistConverterExporter()
        exporter.export(entries)
        webbrowser.open.assert_called_with('http://www.playlist-converter.net/#/freetext=artist-title')


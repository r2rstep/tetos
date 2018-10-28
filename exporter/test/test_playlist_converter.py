from exporter.playlist_converter_exporter import PlaylistConverterExporter

from unittest.case import TestCase
from mock import patch


@patch('exporter.playlist_converter_exporter.webbrowser')
class TestPlaylistConverter(TestCase):
    def test_export_single_entry(self, webbrowser):
        entries = [{'artist': 'artist',
                    'title': 'title'}]
        exporter = PlaylistConverterExporter()
        exporter.export(entries)
        webbrowser.open.assert_called_with('http://www.playlist-converter.net/#/freetext=artist - title')

    def test_export_multiple_entries(self, webbrowser):
        entries = [{'artist': 'Eminem',
                    'title': 'Kim'},
                   {'artist': 'Kanye West',
                    'title': 'Addiction'}]
        exporter = PlaylistConverterExporter()
        exporter.export(entries)
        webbrowser.open.assert_called_with('http://www.playlist-converter.net/#/freetext=Eminem - Kim'
                                           '%0AKanye West - Addiction')

    def test_export_entry_contains_http_special_character(self, webbrowser):
        entries = [{'artist': '@&rtist',
                    'title': '^title'}]
        exporter = PlaylistConverterExporter()
        exporter.export(entries)
        webbrowser.open.assert_called_with('http://www.playlist-converter.net/#/freetext=%40%26rtist - %5Etitle')


from tetos.exporter.playlist_converter_exporter import PlaylistConverterExporter

from unittest.case import TestCase
from mock import patch


@patch('tetos.exporter.playlist_converter_exporter.webbrowser')
class TestPlaylistConverter(TestCase):
    def test_single_entry(self, webbrowser):
        entries = [{'artist': 'artist',
                    'title': 'title'}]
        exporter = PlaylistConverterExporter()
        exporter.export(entries)
        webbrowser.open.assert_called_with('http://www.playlist-converter.net/#/freetext=artist - title')

    def test_multiple_entries(self, webbrowser):
        entries = [{'artist': 'Eminem',
                    'title': 'Kim'},
                   {'artist': 'Kanye West',
                    'title': 'Addiction'}]
        exporter = PlaylistConverterExporter()
        exporter.export(entries)
        webbrowser.open.assert_called_with('http://www.playlist-converter.net/#/freetext=Eminem - Kim'
                                           '%0AKanye West - Addiction')

    def test_entry_contains_http_special_character(self, webbrowser):
        entries = [{'artist': '@&rtist',
                    'title': '^title'}]
        exporter = PlaylistConverterExporter()
        exporter.export(entries)
        webbrowser.open.assert_called_with('http://www.playlist-converter.net/#/freetext=%40%26rtist - %5Etitle')

    def test_entry_contains_slash(self, webbrowser):
        entries = [{'artist': 'AC/DC',
                    'title': 'Hells Bells'}]
        exporter = PlaylistConverterExporter()
        exporter.export(entries)
        webbrowser.open.assert_called_with('http://www.playlist-converter.net/#/freetext=AC DC - Hells Bells')


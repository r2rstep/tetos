from tetos.output.spotify_exporter import SpotifyExporter

from unittest import TestCase
from mock import Mock, patch


class TestSpotifyExporter(TestCase):
    def test_init(self):
        s = SpotifyExporter('art_st')

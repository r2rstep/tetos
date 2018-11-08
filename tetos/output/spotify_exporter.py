from tetos.output.exporter import Exporter

import spotipy
import spotipy.util as spotify_util
import spotipy.oauth2 as spotify_auth


class SpotifyExporter(Exporter):
    def __init__(self, username):
        self._user_token = spotify_util.prompt_for_user_token(username,
                                                              'playlist-modify-private',
                                                              redirect_uri='http://localhost/')
        self._spotify = spotipy.Spotify(self._user_token,
                                        True,
                                        spotify_auth.SpotifyClientCredentials(),
                                        'http://10.158.100.120:8080',
                                        60)

    def export(self, entries: list):
        return entries

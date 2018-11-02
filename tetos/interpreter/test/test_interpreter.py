from tetos.interpreter.interpreter_factory import get_druh_slawek_interpreter

from unittest.case import TestCase


class TestDruhSlawek(TestCase):
    def setUp(self):
        self.interpreter = get_druh_slawek_interpreter()

    def test_one_artist(self):
        text = 'GEORGIA GIBBS / I Want You To Be My Baby (re-edit) [Key Of Keys (7")]'
        expected = {'artist': 'GEORGIA GIBBS',
                    'title': 'I Want You To Be My Baby',
                    'extra_title': 're-edit',
                    'edition': 'Key Of Keys (7")'}
        self.assertEqual(expected, self.interpreter.interpret(text))

    def test_two_artists(self):
        text = "ANTHONY JOSEPH f/ Len 'Boogsie' Sharpe / Sans Souci (Totem) [Heavenly Sweetness (LP)]"
        expected = {'artist': 'ANTHONY JOSEPH',
                    'other_artist': "Len 'Boogsie' Sharpe",
                    'title': 'Sans Souci',
                    'extra_title': 'Totem',
                    'edition': 'Heavenly Sweetness (LP)'}
        self.assertEqual(expected, self.interpreter.interpret(text))

# -*- coding: utf-8 -*-
"""
:copyright: Nokia Networks
:author: Artur Stepniak
:contact: I_UTE_CORE_5G@internal.nsn.com
"""
from tetos.input.importer_factory import get_importer

from unittest import TestCase
from mock import patch


class TestGetImporter(TestCase):
    @patch('tetos.input.importer_factory.TxtImporter', autospec=True)
    @patch('tetos.input.importer_factory.fetch_plain_file')
    def test_txt_importer(self, fetch, importer):
        path = '/path/to/file.txt'
        self.assertEqual(importer.return_value, get_importer(path))
        importer.assert_called_with(path, fetch)

    @patch('tetos.input.importer_factory.HtmlImporter', autospec=True)
    @patch('tetos.input.importer_factory.fetch_html')
    def test_html_importer_remote_file(self, fetch, importer):
        path = 'http://path/to/file'
        self.assertEqual(importer.return_value, get_importer(path))
        importer.assert_called_with(path, fetch)

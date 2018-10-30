# -*- coding: utf-8 -*-
"""
:copyright: Nokia Networks
:author: Artur Stepniak
:contact: I_UTE_CORE_5G@internal.nsn.com
"""
from input_importer.importer_factory import get_importer

from unittest import TestCase
from mock import patch


class TestGetImporter(TestCase):
    @patch('input_importer.importer_factory.TxtImporter', autospec=True)
    def test_txt_importer(self, importer):
        path = '/path/to/file.txt'
        self.assertEqual(importer.return_value, get_importer(path))
        importer.assert_called_with(path)

    @patch('input_importer.importer_factory.HtmlImporter', autospec=True)
    def test_html_importer(self, importer):
        path = '/path/to/file'
        self.assertEqual(importer.return_value, get_importer(path))
        importer.assert_called_with(path)

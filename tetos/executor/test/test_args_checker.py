from tetos.executor.args_checker import check_args

from unittest import TestCase
from mock import Mock


class TestArgsChecker(TestCase):
    def test_incorrect_input(self):
        args = Mock(input_path=['/path'])
        with self.assertRaisesRegex(ValueError, 'Path should begin with http:// or https:// or ftp:// '
                                                'or file:// for a local file'):
            check_args(args)

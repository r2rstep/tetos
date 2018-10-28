from executor.executor import Executor
from input_importer.input_importer import InputImporter
from interpreter.interpreter import Interpreter

from unittest.case import TestCase
from mock import Mock, patch


@patch('executor.executor.get_importer', autospec=True)
@patch('executor.executor.get_druh_slawek_interpreter', autospec=True)
@patch('executor.executor.PlaylistConverterExporter', autospec=True)
class TestExecutor(TestCase):
    def test_executor(self, exporter, get_interpreter, get_importer):
        file_path = ['/path/to/file']
        args = Mock(input_path=file_path)

        importer = Mock(spec_set=InputImporter)
        get_importer.return_value = importer

        interpreter = Mock(spec_set=Interpreter)
        get_interpreter.return_value = interpreter

        executor = Executor(args)

        importer.get_entries.return_value = 'artist - title'
        interpreter.interpret.return_value = [{'artist': 'artist', 'title': 'title'}]

        executor.execute()

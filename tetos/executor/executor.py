from tetos.input.importer_factory import get_importer
from tetos.processing.interpreter_factory import get_druh_slawek_interpreter
from tetos.output.playlist_converter_exporter import PlaylistConverterExporter
from tetos.executor.args_checker import supported_protocols

import os


class Executor(object):
    def __init__(self, args):
        path = args.input_path.pop()
        if not any(path.startswith(protocol) for protocol in supported_protocols):
            path = self._convert_local_file_path(path)
        self._input = path
        self._importer = get_importer(self._input)
        self._interpreter = get_druh_slawek_interpreter()
        self._exporter = PlaylistConverterExporter()

    def execute(self):
        input_entries = self._importer.get_entries()
        entries = self._interpret(input_entries)
        self._exporter.export(entries)

    def _convert_local_file_path(self, s: str):
        return 'file://' + os.path.abspath(s)

    def _interpret(self, input_entries):
        entries = []
        for entry in input_entries:
            interpreted_entry = self._interpreter.interpret(entry)
            if interpreted_entry:
                entries.append(interpreted_entry)

        return entries

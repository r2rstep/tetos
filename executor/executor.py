from input_importer.importer_factory import get_importer
from interpreter.interpreter_factory import get_druh_slawek_interpreter
from exporter.playlist_converter_exporter import PlaylistConverterExporter


class Executor(object):
    def __init__(self, args):
        self._input = args.input_path.pop()
        self._importer = get_importer(self._input)
        self._interpreter = get_druh_slawek_interpreter()
        self._exporter = PlaylistConverterExporter()

    def execute(self):
        input_entries = self._importer.get_entries()
        entries = self._interpret(input_entries)
        self._exporter.export(entries)

    def _interpret(self, input_entries):
        entries = []
        for entry in input_entries:
            interpreted_entry = self._interpreter.interpret(entry)
            if interpreted_entry:
                entries.append(interpreted_entry)

        return entries

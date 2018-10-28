import re


class Interpreter(object):
    def __init__(self, patterns):
        self._search_patterns = patterns

    def interpret(self, text: str):
        match = None
        for pattern in self._search_patterns:
            match = re.search(pattern, text)
            if match:
                break

        entry = None
        if match:
            entry = match.groupdict()
            if 'extra_title' in entry:
                entry['extra_title'] = self._get_raw_title(entry['extra_title'])
            if 'edition':
                entry['edition'] = self._get_raw_edition(entry['edition'])

        return entry

    def _get_raw_title(self, title: str):
        return self._get_raw_str(title, '(', ')')

    def _get_raw_str(self, s: str, l_char: str, r_char: str):
        return s.lstrip(l_char).rstrip(r_char)

    def _get_raw_edition(self, edition: str):
        return self._get_raw_str(edition, '[', ']')

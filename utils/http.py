def encode_http_special_characters(s: str):
    special_chars = {'<': '%3C', '>': '%3E', '#': '%23', '%': '%25',
                     '{': '%7B', '}': '%7D', '|': '%7C', '\\': '%5C',
                     '^': '%5E', '~': '%7E', '[': '%5B', ']': '%5D',
                     '`': '%60', ';': '%3B', '/': '%2F', '?': '%3F',
                     ':': '%3A', '@': '%40', '=': '%3D', '&': '%26',
                     '$': '%24'}
    trans_table = s.maketrans(special_chars)
    return s.translate(trans_table)

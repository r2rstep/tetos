from tetos.interpreter.interpreter import Interpreter


def get_druh_slawek_interpreter() -> Interpreter:
    artist = '?P<artist>.+'
    other_artist = '?P<other_artist>.+'
    title = '?P<title>.+'
    extra_title = '?P<extra_title>\(.+\)'
    edition = '?P<edition>\[.+\]'
    druh_slawek_patterns = [r'({artist}) f/ ({other_artist}) / ({title}) ({extra_title}) ({edition})'
                            .format(artist=artist,
                                    other_artist=other_artist,
                                    title=title,
                                    extra_title=extra_title,
                                    edition=edition),
                            r'({artist}) f/ ({other_artist}) / ({title}) ({edition})'.format(artist=artist,
                                                                                             other_artist=other_artist,
                                                                                             title=title,
                                                                                             edition=edition),
                            r'({artist}) / ({title}) ({extra_title}) ({edition})'.format(artist=artist,
                                                                                         title=title,
                                                                                         extra_title=extra_title,
                                                                                         edition=edition),
                            r'({artist}) / ({title}) ({edition})'.format(artist=artist,
                                                                         title=title,
                                                                         edition=edition)]
    return Interpreter(druh_slawek_patterns)

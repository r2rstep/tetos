import glob


supported_protocols = ['http://', 'https://', 'ftp://']


def check_args(args):
    path = args.input_path[0]
    if not any(path.startswith(protocol) for protocol in supported_protocols):
        if not glob.glob(path):
            raise ValueError('Path format incorrect or local file does not exist. Path should begin with '
                             '{supported_protocols} for remote files'
                             .format(supported_protocols=' or '.join(supported_protocols)))

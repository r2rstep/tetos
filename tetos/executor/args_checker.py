supported_protocols = ['http://', 'https://', 'ftp://', 'file://']


def check_args(args):
    path = args.input_path.pop()
    if not any(path.startswith(protocol) for protocol in supported_protocols):
        raise ValueError('Path should begin with {} for a local file'.format(' or '.join(supported_protocols)))

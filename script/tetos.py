from executor.executor import Executor

import argparse


if __name__ is '__main__':
    args_parser = argparse.ArgumentParser()
    args_parser.add_argument('input_path', nargs=1)
    args = args_parser.parse_args()
    Executor(args)

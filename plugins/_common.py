import argparse
import logging


def get_args(parser=None):
    if not parser:
        parser = argparse.ArgumentParser(description="irc bot plugin")
    parser.add_argument("-i", "--host", default="127.0.0.1", help="host to connect to")
    parser.add_argument("-p", "--port", default=7003, help="port to connect to")
    return parser.parse_args()


def get_logger():
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)-15s %(levelname)-8s %(filename)s:%(lineno)d %(message)s")
    return logging.getLogger()

import sys


def signal_handler(sig, frame):
    print("process canceled by user (Ctrl+C). exiting...")
    sys.exit(0)

import signal

import subprocess
from utils.signal_handler import signal_handler
from utils.banner import banner
from utils.arguments_parser import args
from utils.zip_checker import check_zip
from utils.wordlist_parser import wordlist_parser
from utils.zip_cracker import brute_force
import sys
from pathlib import Path


def init():
    signal.signal(signal.SIGINT, signal_handler)
    subprocess.run(["clear"])
    print(banner)
    print("\nPress CTRL+C to cancel")

    input_zip_path = Path(str(args.input))
    password_list_path = Path(str(args.passlist))

    if check_zip(input_zip_path):
        password_list = wordlist_parser(password_list_path)
        if brute_force(passlist=password_list, zip_path=input_zip_path):
            print("Brute force attack succeeded.")
        else:
            print("Brute force attack failed.")
            sys.exit(1)
    else:
        sys.exit(0)

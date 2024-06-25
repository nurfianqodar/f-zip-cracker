import sys
import time


def wordlist_parser(path: str) -> list:
    print("checking wordlist file...")
    time.sleep(1)
    try:
        with open(path, encoding="latin-1", mode="r") as words:
            wordlist = words.readlines()
            print("wordlist is valid")
            time.sleep(1)
            print("preparing wordlist...")
            time.sleep(1)
            return [word.strip() for word in wordlist]
    except FileNotFoundError:
        print("wordlist file not found!")
        sys.exit(1)
    except Exception as e:
        print(f"an error occurred while reading the wordlist: {e}")
        sys.exit(1)

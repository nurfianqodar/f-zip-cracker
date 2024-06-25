from zipfile import ZipFile, BadZipFile, LargeZipFile
from colorama import Fore, Style
import sys
import time


def check_zip(path: str) -> bool:
    print("checking zip file...")
    time.sleep(1)
    try:
        with ZipFile(file=path, allowZip64=True) as zf:
            zf.testzip()
    except RuntimeError as err:
        if "password required" in str(err).lower():
            print(
                Fore.GREEN
                + "✓ zip file is valid and protected, running brute force"
                + Style.RESET_ALL
            )
            time.sleep(1)
            return True
        else:
            print(f"runtime error occurred: {err}")
            sys.exit(1)
    except BadZipFile:
        print("zip file is invalid")
        sys.exit(1)
    except FileNotFoundError:
        print("zip file not found")
        sys.exit(1)
    except LargeZipFile:
        print("zip file is too large to be processed")
        sys.exit(1)
    except Exception as e:
        print(f"an error occurred: {e}")
        sys.exit(1)

    print("zip file is not protected, there is nothing to crack.")
    sys.exit(0)

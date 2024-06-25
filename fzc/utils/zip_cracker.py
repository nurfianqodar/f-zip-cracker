from zipfile import ZipFile
from colorama import Fore
import sys
import math
import time


def brute_force(passlist: list, zip_path: str) -> bool:
    print("start cracking...\n\n\n")
    time.sleep(1)
    with ZipFile(zip_path, allowZip64=True) as zf:
        password_counter = 0
        for pw in passlist:
            try:
                password_counter += 1
                password_in_percent = math.floor(password_counter / len(passlist) * 100)

                sys.stdout.write(
                    f"trying {password_counter} password from {len(passlist)} passwords -> {password_in_percent}% \r"
                )
                sys.stdout.flush()

                zf.setpassword(pwd=pw.encode("utf-8"))
                if zf.testzip() is None:
                    print(
                        f"\n\n\n✓ cracked with password: [  {Fore.GREEN+pw+Fore.RESET}  ]\n\n\n"
                    )
                    return True
            except RuntimeError:
                continue
            except Exception as e:
                continue
    print("failed to crack the zip file with provided passwords.")
    return False

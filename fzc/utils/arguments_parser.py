from argparse import ArgumentParser
import argcomplete


parser = ArgumentParser()
parser.add_argument(
    "-i", "--input", type=str, help="Input: path/to/zipfile.zip", required=True
)
parser.add_argument(
    "-l",
    "--passlist",
    type=str,
    help="Password list: path/to/passwordlist",
    required=True,
)

argcomplete.autocomplete(parser)
args = parser.parse_args()

print(args)

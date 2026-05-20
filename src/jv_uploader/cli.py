import argparse
from .batch import upload_all_jv
from .pipeline import process_jv_file
from dotenv import load_dotenv
load_dotenv()

def main():
    parser = argparse.ArgumentParser(description="JV Upload Pipeline")
    sub = parser.add_subparsers(dest="cmd")

    s1 = sub.add_parser("upload-one")
    s1.add_argument("--file", required=True)

    s2 = sub.add_parser("upload-all")
    s2.add_argument("--root", required=True)

    args = parser.parse_args()

    if args.cmd == "upload-one":
        process_jv_file(args.file)

    elif args.cmd == "upload-all":
        upload_all_jv(args.root)

from argparse import ArgumentParser
from pathlib import Path

from formats.google import read_google_contacts


def start():
    parser = ArgumentParser()
    parser.add_argument("file")
    args = parser.parse_args()
    main(Path(args.file))


def main(file: Path):
    contacts = read_google_contacts(file)
    for contact in contacts:
        print("=====================================")
        print("Name: " + contact.name)
        print("Emails:")
        for data in contact.emails:
            print(f"- {data[1]} ({data[0]})")
        print("Phone Numbers:")
        for data in contact.phone_numbers:
            print(f"- {data[1]} ({data[0]})")
        print("Groups:")
        for group in contact.groups:
            print(f"- {group}")

if __name__ == "__main__":
    start()
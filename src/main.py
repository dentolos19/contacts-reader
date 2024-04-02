from argparse import ArgumentParser
from pathlib import Path

from formats.google import read_google_contacts
from formats.outlook import read_outlook_contacts


def start():
    parser = ArgumentParser()
    parser.add_argument("file")
    parser.add_argument("--format", default="google")
    args = parser.parse_args()
    main(Path(args.file), args.format)


def main(path: Path, type: str):
    contacts = []

    if type == "google":
        contacts = read_google_contacts(path)
    elif type == "outlook":
        # contacts = read_outlook_contacts(path)
        pass
    else:
        raise ValueError(f"Invalid format: {type}")

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
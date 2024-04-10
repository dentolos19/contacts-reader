import csv
from pathlib import Path


class OutlookContact:
    def __init__(self, row: list[str], headers: list[str]):
        # TODO: Implement this
        pass


def read_outlook_contacts(path: Path):
    if not path.exists() or not path.is_file():
        raise FileNotFoundError(f"This file is invalid: {path}")
    contacts: list[OutlookContact] = []
    with open(path, newline="") as file:
        reader = csv.reader(file)
        headers = next(reader)
        for row in reader:
            contacts.append(OutlookContact(row, headers))
    return contacts
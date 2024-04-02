import csv
import re
from pathlib import Path


class GoogleContact:
    def __init__(self, row: list[str], headers: list[str]):
        self.name = row[0]
        self.given_name = row[1]
        self.family_name = row[3]
        self.birthday = row[14]
        self.gender = row[15]
        self.notes = row[25]
        self.photo = row[27]
        self.groups = row[28].split(" ::: ")
        # After column 35, the data is dynamic. So we need the headers to identify what kind it is.
        dynamic_data = row[28:] # Gets values after 28th index
        dynamic_data_headers = headers[28:] # Gets headers after 28th index

        self.emails = []
        self.phone_numbers = []

        for index, header in enumerate(dynamic_data_headers):
            # Matches email columns
            if re.match(r"E-mail \d - Type", header) and re.match(r"E-mail \d - Value", dynamic_data_headers[index + 1]):
                type = dynamic_data[index]
                value = dynamic_data[index + 1]
                # To avoid adding empty values
                if not type or not value:
                    continue

                # If there are values with the same type, they are separated by " ::: "
                emails = value.split(" ::: ")
                for email in emails:
                    self.emails.append((type, email))

            # Matches phone number columns
            elif re.match(r"Phone \d - Type", header) and re.match(r"Phone \d - Value", dynamic_data_headers[index + 1]):
                type = dynamic_data[index]
                value = dynamic_data[index + 1]
                # To avoid adding empty values
                if not type or not value:
                    continue

                # If there are values with the same type, they are separated by " ::: "
                phone_numbers = value.split(" ::: ")
                for phone_number in phone_numbers:
                    self.phone_numbers.append((type, phone_number))

            # TODO: Handle address columns
            # TODO: Handle organization columns

def read_google_contacts(path: Path):
    if not path.exists() or not path.is_file():
        raise FileNotFoundError(f"This file is invalid: {path}")
    contacts: list[GoogleContact] = []
    with open(path, newline='') as file:
        reader = csv.reader(file)
        headers = next(reader)
        for row in reader:
            contacts.append(GoogleContact(row, headers))
    return contacts
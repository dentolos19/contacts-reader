import csv

from formats.google import GoogleContact

contacts: list[GoogleContact] = []

with open("public/contacts.csv", newline='') as csvfile:
    reader = csv.reader(csvfile)
    headers = next(reader)
    for row in reader:
        contacts.append(GoogleContact(row, headers))

for contact in contacts:
    print(contact.name)
    print(contact.emails)
    print(contact.phone_numbers)
    print()
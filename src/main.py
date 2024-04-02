from formats.google import read_google_contacts

contacts = read_google_contacts("public/test.csv")

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
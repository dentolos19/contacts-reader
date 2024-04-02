import re


class GoogleContact:
    def __init__(self, row: list[str], headers: list[str]):
        self.name = row[0]
        self.given_name = row[1]
        self.family_name = row[3]
        self.birthday = row[14]
        self.groups = row[28].split(" ::: ")
        # After column 35, the data is dynamic. So we need the headers to identify what kind it is.
        dynamic_data = row[28:]
        dynamic_data_headers = headers[28:]

        self.emails = []
        self.phone_numbers = []

        for header in dynamic_data_headers:
            index = dynamic_data_headers.index(header)

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

            # TODO: Handle addresses
            # TODO: Handle organizations
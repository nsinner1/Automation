import re


def open_file(file):
    with open(file, "r") as f:
        return f.read().lower()


def get_emails(file):
    opened = open_file(file)
    regex = r'\S+@\S+'
    emails = re.findall(regex, opened)
    emails = list(dict.fromkeys(emails))
    # print(emails)
    return emails


def get_phone_numbers(file):
    opened = open_file(file)
    regex = r'(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})'
    phone_numbers = re.findall(regex, opened)
    phone_numbers = list(dict.fromkeys(phone_numbers))
    # print(phone_numbers)
    return phone_numbers


def store_info(info, file):
    info.sort()
    sorted_files = open_file(file).split('\n')

    with open(file, "a+") as f:
        for data in info:
            if data in sorted_files:
                return False
            else:
                f.write(data + '\n')


email_data = get_emails('assets/potential-contacts.txt')

phone_data = get_phone_numbers('assets/potential-contacts.txt')

store_info(email_data, 'assets/emails.txt')
store_info(phone_data, 'assets/phone_numbers.txt')


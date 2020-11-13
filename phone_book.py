import re
import csv

with open("phonebook_raw.csv") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

new_contacts_list = []

for contact in contacts_list:
    new_contact = list()
    pattern = re.compile(r'([a-z]+)?(\+7\s*|8\s*)\(?(\d\d\d)\)?[- ]?(\d\d\d)?[- ]?(\d\d)[- ]?(\d\d)\s*\(?(['
                         r'а-я]+)?(\.\s*\d+)?\)?')
    phones = pattern.sub(r'\1 +7(\3)\4-\5-\6 \7\8', contact[5])
    contact[5] = phones
    full_name_str = ",".join(contact[:3])
    result = re.findall(r'(\w+)', full_name_str)
    while len(result) < 3:
        result.append('')
    new_contact += result
    new_contact.append(contact[3])
    new_contact.append(contact[4])
    new_contact.append(contact[5])
    new_contact.append(contact[6])
    new_contacts_list.append(new_contact)

phone_book = dict()

for contact in new_contacts_list:

    if contact[0] in phone_book:
        contact_value = phone_book[contact[0]]
        for i in range(len(contact_value)):
            if contact[i]:
                contact_value[i] = contact[i]
    else:
        phone_book[contact[0]] = contact

with open("phonebook.csv", "w") as f:
    data_writer = csv.writer(f, delimiter=',')
    data_writer.writerows(list(phone_book.values()))

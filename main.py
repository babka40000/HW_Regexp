from pprint import pprint
import csv
import re

if __name__ == '__main__':
    with open("phonebook_raw.csv") as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)

    good_contact_list = [contacts_list[0]]

    for contacts_row in contacts_list:
        if contacts_row != contacts_list[0]:
            contact_row_tmp = contacts_row[0] + ' ' + contacts_row[1] + ' ' + contacts_row[2]
            good_contact_row = []
            res = re.split('\s+', contact_row_tmp)
            good_contact_row.append(res[0])
            if len(res) >= 2:
                good_contact_row.append(res[1])
            if len(res) >= 3:
                good_contact_row.append(res[2])

            good_contact_row.append(contacts_row[3])
            good_contact_row.append(contacts_row[4])

            pattern = "\+?[7|8]\s?\(?([0-9][0-9][0-9])\)?\s?[-]?([0-9][0-9][0-9])[-]?([0-9][0-9])[-]?([0-9][0-9])\s?\(?\,?(доб. )?([0-9][0-9][0-9][0-9])?\)?"
            res = re.sub(pattern, r"+7(\1)\2-\3-\4 \5\6", contacts_row[5])
            good_contact_row.append(res)

            good_contact_row.append(contacts_row[6])

            merge = False

            for contact_row_temp in good_contact_list:
                if contact_row_temp[0] == good_contact_row[0] and contact_row_temp[1] == good_contact_row[1]:
                    merge = True
                    for count in range(3, len(contact_row_temp)):
                        if good_contact_row[count] != '':
                            contact_row_temp[count] = good_contact_row[count]
            
            if not merge:
                good_contact_list.append(good_contact_row)
                
    with open("phonebook.csv", "w") as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(good_contact_list)


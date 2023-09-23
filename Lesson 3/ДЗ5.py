import json
import csv
import re

with open('traders.txt', 'r') as ttt:
    line = [int(i) for i in ttt]

with open('traders.json', 'r') as tjs:
    text_from_traders = json.load(tjs)

traders = [i for i in text_from_traders if int(i['inn']) in line]

with open('traders.csv', 'w', newline='') as tsv:
    text = csv.writer(tsv, delimiter=';')
    text.writerow(['INN', 'OGRN', 'ADDRESS'])
    for i in traders:
        text.writerow([i['inn'], i['ogrn'], i['address']])

# Напишите регулярное выражение для поиска email-адресов в тексте.

# Для этого напишите функцию, которая принимает в качестве аргумента текст в виде строки
# и возвращает список найденных email-адресов или пустой список, если email-адреса не найдены.

# Найдите все email-адреса в дата-сете и соберите их в словарь,
# где ключом будет выступать ИНН опубликовавшего сообщение («publisher_inn»),
# а в значении будет хранится множество set() с email-адресами.

# Сохраните собранные данные в файл «emails.json».

expression_email = re.compile(r'\b[0-9a-zA-Z.-_]+@[0-9a-zA-Z.-_]+\.[a-zA-Z]+\b')


def emails(text):
    all_emails = []
    for i in text:
        all_emails.append(re.findall(expression_email, i['msg_text']))
    return all_emails


with open("1000_efrsb_messages.json", "r") as efrsb:
    text_from_efrsb = json.load(efrsb)

print(emails(text_from_efrsb))

dict_emails = {text_from_efrsb[i]['publisher_inn']: set(emails(text_from_efrsb)[i]) for i in range(len(text_from_efrsb)) if len(emails(text_from_efrsb)[i]) != 0}

with open('emails.json', "w") as ejs:
    json.dump(dict_emails, ejs)
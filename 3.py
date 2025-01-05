import re
import csv

PATH = 'task3.txt'
PATH_OUT = 'task3_out.csv'


def find_date(text):
    res = re.findall(r"\d{4}-\d\d-\d\d", text)
    return res

def find_www(text):
    res = re.findall(r'http[s]?://[a-zA-Z -]{1,}?[.]?'+
                     r'[0-9a-zA-Z -]{1,}[.]\w{1,}/', text)
    return res

def find_email(text):
    res = re.findall(r'[0-9a-z]{1,}+@'+
                     r'[a-zA-Z0-9.-]+\.[a-z]{,4}',text)
    return res

def find_name(text):
    res = re.findall(r'[a-zA-Z]{1,}',text)
    return res

with open(PATH, 'r') as f:
   text3 = f.read()
res_date = find_date(text3)
text3 = re.sub(r"\d{4}-\d\d-\d\d",' ', text3)
res_www = find_www(text3)
text3 = re.sub(r'http[s]?://[a-zA-Z -]{1,}?[.]?'+
                     r'[0-9a-zA-Z -]{1,}[.]\w{1,}/',' ', text3)
res_email = find_email(text3)
text3 = re.sub(r'[0-9a-z]{1,}+@'+
                     r'[a-zA-Z0-9.-]+\.[a-z]{,4}',' ',text3)
res_name = find_name(text3)
text3 = re.sub(r'[a-zA-Z]{1,}',' ',text3)
res_id =[i for i in range(1, 10001)]

with open('task3-out.csv', 'w', newline='', encoding='utf-8') as out:
    writer = csv.writer(out)
    writer.writerow(['ID', 'Name', 'Email', 'URL',
                     'Date of registration'])
    for row in zip(res_id, res_name, res_email, res_www, res_date):
        writer.writerow(row)



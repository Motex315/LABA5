import re

PATH = 'task1-en.txt'
PATH_OUT_E = 'task1-out_e.txt'
PATH_OUT_NUM = 'task1-out_num.txt'


def end_e(text):
    res_e = re.findall(r'\w{1,}e ', str(text))
    return res_e

def brackets_num(text):
    res_num = re.findall(r'\([0-9]*\)', str(text))
    return res_num

with open(PATH) as text, open(PATH_OUT_E, 'w') as out_e:
    text_e =''
    for line in text:
        res_e = end_e(line)
        for i in range(len(res_e)):
            text_e=text_e+res_e[i]+', '
    out_e.write(text_e[0:len(text_e)-2])

with open(PATH) as text, open(PATH_OUT_NUM, 'w') as out_num:
    text_num =''
    for line in text:
        res_num = brackets_num(line)
        for i in range(len(res_num)):
            text_num=text_num+res_num[i]+', '
    out_num.write(text_num[0:len(text_num)-2])
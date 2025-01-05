import re

PATH = 'task2.html'
PATH_OUT = 'task2_out.txt'

def img_sizes(text):
    res = re.findall(r'[0-9]{1,}x[0-9]{1,}', str(text))
    return res

with open(PATH, encoding='utf-8') as text, open(PATH_OUT, 'w', encoding='utf-8') as out:
    sizes = ''
    for line in text:
        res = img_sizes(line)
        print(res)
        if str(res) != '[]':
            out.write(str(res))
        


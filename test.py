#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import pandas
from bs4 import BeautifulSoup
#import requests

with open("mirea_09_03_01.html", "r") as  page:
    parser = BeautifulSoup(page, 'lxml')


fio = []
doc = []
agreement = []
campus = []
exam = []
table = parser.find_all("tr")[1:]
i = 0

for row in table:
    i+=1
    col = row.find_all("td")
    fio.append(col[1].string.strip())
    doc.append(col[2].string.strip())
    agreement.append(col[3].string.strip())
    campus.append(col[4].string.strip())
    exam.append(col[7].string.strip())
    sys.stdout.write('\r'+"#"*(50*i//len(table)))
print("\n[+] Table parsed")

frame = {"fio":fio,
         "doc":doc,
         "agreement":agreement,
         "campus":campus,
         "exam":exam}

df = pandas.DataFrame(frame)
with open('test.html', 'w') as _:
    _.write(df.to_html())

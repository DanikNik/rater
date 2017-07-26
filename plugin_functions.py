#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
import pandas
from bs4 import BeautifulSoup
import requests

with open('urls.txt', 'r') as _:
    url_list = _.readlines()

def parse_table_mirea(page):
    parser = BeautifulSoup(page)
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
        try:
            campus.append(col[4].string.strip())
            fio.append(col[1].string.strip())
            doc.append(col[2].string.strip())
            agreement.append(col[3].string.strip())
            exam.append(col[7].string.strip())
        except:
            pass
        sys.stdout.write('\r' + "#"*(70*i//len(table)))
    print("\n[+]Table parsed")
    frame = {"fio":fio,
            "doc":doc,
            "agreement":agreement,
            "campus":campus,
            "exam":exam}
    df = pandas.DataFrame(frame)
    return(df)

if __name__ == '__main__':
    for url in url_list:
        page = requests.get(url).text
        tag = BeautifulSoup(page).find('h1').text.split('\n')[1][:8]
        print('parsing table ' + tag)
        data = parse_table_mirea(page)
        data.to_csv('tables/' + str(tag) + '_mirea.csv')

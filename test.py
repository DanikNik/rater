#!/usr/bin/python3
# -*- coding: utf-8 -*-

import pandas

frame = pandas.read_csv('tables/01.03.02_mirea.csv')
hashtable = []

for fio in frame['fio']:
    hashtable.append([fio, hash(fio)])

def sorting(list_):
    return list_[1]

hashtable.sort(key=sorting)

def bin_search(table, credentials):
    print(hash(credentials))
    left_border = 0
    right_border = len(lst)
    while right_border - left_border > 1:
        index = (left_border + right_border) // 2
        if hash(credentials) < table[index][1]:
            right_border = index
        else:
            left_border = index
    return left_border if table[left_border][0] == credentials else None

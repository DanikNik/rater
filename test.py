#!/usr/bin/python3
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
#import requests

with open("input_tables/mpei_01_03_02.html", "r") as  page:
    parser = BeautifulSoup(page, 'lxml')

tables = parser.find_all('table')
print(len(tables))

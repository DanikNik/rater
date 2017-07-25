#!/usr/bin/python3

import pandas
from bs4 import BeautifulSoup

def gen_mirea_table(source):
        mirea_dataframe = pandas.read_html('{}.html'.format(source), header=0)[0]
        print('[+]Table {} loaded'.format(source))
        mirea_dataframe.drop([list(mirea_dataframe)[0], list(mirea_dataframe)[4], list(mirea_dataframe)[5], list(mirea_dataframe)[6]], 1, inplace=True)
        print('[+]Table {} formated'.format(source))
        return(mirea_dataframe)

mirea_dataframe_09_03_01 = gen_mirea_table('mirea_09_03_01')
#mirea_dataframe_09_03_02 = gen_mirea_table('mirea_09_03_02')

#df = pandas.DataFrame()
#k = 0
#print('[+]Output DataFrame initialized')

#for i in range(len(mirea_dataframe_09_03_01['ФИО'])):
#    fio = mirea_dataframe_09_03_01['ФИО'][i]
#    if fio in mirea_dataframe_09_03_02['ФИО'].values:
#        k+=1
#        print('[+]Found collision', k)
#        row = mirea_dataframe_09_03_01.loc[mirea_dataframe_09_03_01['ФИО']==fio]
#        df = df.append(row, ignore_index=True)

with open('rater', 'w') as _:
    _.write(mirea_dataframe_09_03_01.to_string())
    print('[+]Output file generated')

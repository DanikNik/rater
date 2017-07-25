#!/usr/bin/python3

import pandas
import plugin_functions

mirea_dataframe_09_03_01 = plugin_functions.parse_table_mirea('mirea_09_03_01')
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

#!bin/python
import pandas
frame = pandas.read_html('raw_pages/mpei_01_03_02.html', header=0)[3]
frame.drop([list(frame)[1], list(frame)[2], list(frame)[3], list(frame)[4], list(frame)[6]], 1, inplace=True)
frame.drop(0, 0, inplace=True)
#frame.rename(axis=1)
with open('test.html', 'w') as _:
    _.write(frame.to_html())

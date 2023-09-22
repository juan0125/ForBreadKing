import pandas as pd
import csv
import linecache
import os
from datetime import datetime


## read file
path = r'D:\1_DX엔지니어링팀\50_src\ForBreadKing\data'
readFilename = path + "\example.csv"
print('read file name : ', readFilename)

## create temp file name
curTime = datetime.today().strftime("%Y%m%d%H%M%S")
writeFilename = path + '\\' + curTime + 'tmp.csv'
print('write file name : ', writeFilename)

## start read original file
cntSkipFirstLine = 1
cntSkipMidLine = 2
curReadLine = 0
cntReadLine = 10 ## How many lines would you like to read?

rf = open(readFilename, 'r', encoding='CP949')
## For skip first couple of line
for _ in range(cntSkipFirstLine):
    next(rf)
while True:
    line = rf.readline()
    if '*/' in line:
        ## For writing column info
        wf = open(writeFilename, 'w')
        wf.write(prevLine)
        columns = prevLine.strip().split(',') # remove newline and parsing

        ## For writing data 
        for _ in range(cntSkipMidLine):
            next(rf)
        while curReadLine < cntReadLine:
            line = rf.readline()
            #print('write')
            wf.write(line)
            curReadLine += 1
        break
    prevLine = line
rf.close()
wf.close()

## For handle new cvs file.
df = pd.read_csv(writeFilename, skiprows=1,names=columns)
print('new csv original data')
print(df)

checkColumn = 'item1'
checkCharList = ['count', 'camera', '1930000']
filtered_df = df[ df[checkColumn].str.contains('|'.join(checkCharList)) ]

print('new csv filtered data')
print(filtered_df)

os.remove(writeFilename)
print('deleted tmp file : ', writeFilename)
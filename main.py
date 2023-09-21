import pandas as pd
import csv
import linecache
from datetime import datetime

## read file
path = r'D:\1_DX엔지니어링팀\50_src\ForBreadKing\data'
readFilename = path + "\example.csv"

## create temp file name
curTime = datetime.today().strftime("%Y%m%d%H%M%S")
writeFilename = path + '\\' + curTime + 'tmp.csv'

## start read original file
rf = open(readFilename, 'r', encoding='CP949')
iterator = 0
start = 0
cntReadLine = 20 ## How many lines would you like to read?
while True:
    line = rf.readline()
    iterator += 1
    if '*/' in line:
        ## For writing column info
        wf = open(writeFilename, 'w')
        wf.write(prevLine)

        ## For writing data 
        while iterator < cntReadLine:
            line = rf.readline()
            print('write')
            wf.write(line)
            iterator += 1
        break
    prevLine = line
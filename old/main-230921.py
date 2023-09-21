import pandas as pd
import csv
import linecache

# filename = os.getcwd() + r'\data\example.csv'
filename = r"D:\1_DX엔지니어링팀\50_src\ForBreadKing\data\example.csv"

f = open(filename,'r',encoding='CP949')
reader = csv.reader(f)

### For reading header information
iterator = 0
start = 0
#end = 0
for line in reader:
    iterator += 1
    #print(line) ## For debug
    if '*/' in line[0]: #if */ line, escape this for loop.
        start = iterator
        break

### For reading column
columnLine = linecache.getline(filename,iterator-1)
#print(line) ## For debug

columns = columnLine.strip().split(',') # remove newline and parsing
print(columns)

### For reading data
df = pd.read_csv(filename, skiprows=start, names=columns)
print(df)
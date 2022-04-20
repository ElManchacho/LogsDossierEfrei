import csv
from pathlib import Path
from sqlite3 import paramstyle
import pandas as pd
import os
from os import listdir
from os.path import isfile, join
import csv

folder = '..\\Logs\\'

headers = []

rows = []

indexes = []

for file in os.listdir(folder):
    if file.split('.')[1] == 'csv':
        indexes.append(file)
        file = open(folder+file)
        csvreader=csv.reader(file)
        fileHeaders = ""
        fileHeaders = next(csvreader)
        for header in fileHeaders:
            newHeaders = header.replace('\"','').split(';')
            if(newHeaders!=headers):
                headers = newHeaders
        for row in csvreader:
            parsedRow = []
            if row.__len__() == 1:
                parsedRow += row[0].split(';')
            else:
                slices = ""
                for rowSlice in row:
                    slices += rowSlice+','
                parsedRow += slices.split(';')
            rows.append(parsedRow)
df1 = pd.DataFrame(rows,
                   index=indexes,
                   columns=headers)
print(df1)

df1.to_excel("../Excel/ConcatenatedLogs.xlsx")  

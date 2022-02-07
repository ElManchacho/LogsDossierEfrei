import sys
import time
import random
import csv
import datetime
from csv import unix_dialect
from os import listdir
from os.path import isfile, join

if __name__ == '__main__' :

    folder = '../Logs/'

    logs = [
            f for f in listdir(folder) 
                if isfile(
                    join(folder, f)
                    )
                ]

    toRemove = []
    count = 0

    for log in logs :
        split2 = log.split(".",1)
        extension = split2[1]
        if (extension!='csv'):
            toRemove.append(log)
        count +=1

    for log in toRemove:
        logs.remove(log)
    
    dateTemp = ""

    lastDate ="0-00-00"

    lastLogName = ""

    lastLogs = []

    #lastLogName = logs[len(logs)-1]

    for log in logs:

        dateTemp = log.split("_",1)
        dateTemp = dateTemp[1].split("_",1)[1]
        dateTemp = dateTemp.split(".",1)[0]

        if lastDate < dateTemp:
            lastDate = dateTemp
            lastLogName = log
            lastLogs = [log]
        
        elif lastDate == dateTemp:
            lastLogs.append(log)

    

    for log in lastLogs :

        lastlog = {}

        with open(folder+log, newline='') as csvfile:
            reader = csv.DictReader(csvfile, dialect=unix_dialect)
            for row in reader:
                lastlog = row

        print("\nNombre de logs enregistrés")

        print(len(logs))
        
        print("\nLog visionné : " + log)

        print("\nActivité à la dernière date enregistrée - Le " + lastlog["Date"] + " : \n" + lastlog["ActivityDescription"] + "\n")

        print("\nLe dernier 'à faire' en date : ")

        print(lastlog["TodoTomorrow"])

        print("\nWarnings")

        print(lastlog["ImportantTasks"]+"\n")
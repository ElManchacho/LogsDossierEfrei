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
    

    lastLogName = logs[len(logs)-1]

    lastlog ={}

    with open(folder+lastLogName, newline='') as csvfile:
        reader = csv.DictReader(csvfile, dialect=unix_dialect)
        for row in reader:
            lastlog = row

    print("Nombre de logs enregistrés")

    print(len(logs))

    print("\nActivité à la dernière date enregistrée")

    print("Le " + lastlog["Date"] + " : \n" + lastlog["ActivityDescription"] + "\n")

    print("\nLe dernier 'à faire' en date : ")

    print(lastlog["TodoTomorrow"])

    print("\nWarnings")

    print(lastlog["ImportantTasks"]+"\n")
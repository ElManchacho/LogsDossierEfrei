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
    print("Nombre de logs enregistrés : ")

    logs = [
            f for f in listdir(folder) 
                if isfile(
                    join(folder, f)
                    )
                ]
    
    lastLogName = logs[len(logs)-1]

    with open(folder+lastLogName, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(row)

    print("\nDernière date enregistrée : ")

    

    print("\nLe dernier 'à faire' en date : ")

    print(logs[len(logs)-1])

    print("\nWarnings : ")
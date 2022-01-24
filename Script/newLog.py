from posixpath import split
import sys
import time
import random
import csv
import datetime
from tkinter import *
from csv import unix_dialect
from os import listdir
from os.path import isfile, join

def newTextArea(title:str="TextArea"):

    info = []

    window = Tk()

    window.title(title)

    text = Text(window,
                bg="light grey",
                font=("black",25),
                height=8,
                width=20,
                padx=20,
                pady=20)

    text.pack()

    def submit():

        inputText = text.get("1.0",END)

        info.append(inputText)

        return inputText, window.destroy()

    buttonSubmit = Button(window, text = "Submit", command = submit)

    buttonSubmit.pack()

    window.mainloop()

    return info

if __name__ == '__main__' :

    folder = '../Logs/'

    print("Nouvelle entrée 'log_id_date' EFREI pour mémoire : ")

    dateNow = datetime.datetime.today()

    id = 0 # incrémenter pour chaque logs de la même journée

    logs = [
            f for f in listdir(folder) 
                if isfile(
                    join(folder, f)
                    )
                ]

    for log in logs :
        info=[]
        split1 = log.split("_",2)
        split2 = split1[2].split(".",1)
        split1.pop(2)
        split2.pop(1)
        info = split1 + split2
        if str(dateNow.date())==info[2]:
            id += 1


    headers = ["Date","ActivityDescription","TodoTomorrow","ImportantTasks"]


    print("\n\nWhat did you do today ?\n")

    activityDesc = newTextArea("What did you do today ?")[0]


    print("\n\nWhat will you do tomorrow ?\n")

    toDoTomorrow =  newTextArea("What will you do tomorrow ?")[0]


    print("\n\nImportant tasks for tomorrow ?\n")
    
    importantTasks = newTextArea("Important tasks for tomorrow ?")[0]


    dataList = [[dateNow,activityDesc.replace('\n',''),toDoTomorrow.replace('\n',''),importantTasks.replace('\n','')]]

    with open(folder+'log_'+str(id)+'_'+str(dateNow.date())+'.csv', 'w', newline='') as f:
        writer = csv.writer(f,dialect=unix_dialect)
        csvHeaders = []
        for header in headers :
            csvHeaders.append(header)
        writer.writerows([csvHeaders])
        writer.writerows(dataList)
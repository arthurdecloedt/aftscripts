import csv
from os import listdir

filearr=listdir("csv")

profiles=[]


for filename in filearr:

    file = open("csv/"+filename,"r")
    filelines=file.readlines()
    del(filelines[0])
    for line in filelines:
        linefull=

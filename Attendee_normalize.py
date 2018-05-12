
import csv

gegevens = open("/Users/arthurdecloedt/Downloads/attaft.csv","r")
gegevensLST = gegevens.readlines()

title=2
first_name=3
last_name=4
mail=5
home_addres1=17
home_addres2=18
city=19
state = 20
zip=21
country=22
age=23
interesse=24
faculty=25
facultyifother=26
phase=27
phaseifother=28
connection=29
connectionifother=30
newsletters=31


names=("title","first_name","last_name","mail","home_addres1","home_addres2","city","state",'zip','country','age','interesse','faculty','facultyifother','phase','phaseifother',
       'connection','connectionifother','newsletters')

namelist=[]
namelist.append(names)
i=0

first=True
for row in gegevensLST:
       if first:
              first=False
              continue
       rij = row.split(",")
       rijnuttig=(rij[title],rij[first_name],rij[last_name],rij[mail],rij[home_addres1],rij[home_addres2],rij[city],rij[state],
       rij[zip],rij[country],rij[age],rij[interesse],rij[faculty],rij[facultyifother],rij[phase],rij[phaseifother],rij[connection],rij[connectionifother],rij[newsletters])
       namelist.append(rijnuttig)

with open("exp.csv","w") as exp:
       writer=csv.writer(exp)
       writer.writerows(namelist)
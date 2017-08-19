gegevens = open("/Users/arthurdecloedt/Downloads/gegevens2.csv","r")

gegevensLST=gegevens.readlines()

del(gegevensLST[0])

for line in gegevensLST:


    personlist=line.split(",")

    name1=personlist[0]
    name2=personlist[1]
    name = personlist[0] + " " + personlist[1]
    function = personlist[2]
    aftmail = personlist[3]

    tel = personlist[4]
    tel=tel.replace("+","00")

    vcf= open("contacts/"+name1+name2+".vcf","w")
    exf=open("contacts/example.vcf")
    ex=exf.read()
    ex=ex.replace("FNAME",name1)
    ex=ex.replace("LNAME",name2)
    ex=ex.replace("NAME",name)
    ex=ex.replace("FUNCTION",function)
    ex=ex.replace("MAILAD",aftmail)
    ex=ex.replace("NUMBER",tel)
    vcf.write(ex)
    vcf.flush()
    vcf.close()
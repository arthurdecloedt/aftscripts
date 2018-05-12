gegevens = open("/Users/arthurdecloedt/Downloads/Gegeve.csv",encoding='utf8')

print(gegevens)

gegevensLST=gegevens.readlines()

del(gegevensLST[0])

for line in gegevensLST:
    sigf = open("/Users/arthurdecloedt/Downloads/SignatureAFT.htm", "r")
    sig = sigf.read()

    personlist=line.split(",")

    name=personlist[0]+" "+personlist[1]
    function=personlist[2]
    aftmail=personlist[3]
    tel=personlist[4]
    if personlist[8].find("linkedin"):
        linkedin=personlist[9]
    else:
        try:
            linkedin=personlist[10]
        except Exception:
            linkedin=""
    print(name)
    print("linkedin"+linkedin)
    persfile=open("./sig/"+name+".html","w")

    sig=sig.replace("NAME",name)
    sig=sig.replace("FUNCTION",function)
    sig=sig.replace("MAIL",aftmail)
    sig=sig.replace("NUMBER",tel)
    sig=sig.replace("LINKEDIN",linkedin)
    persfile.write(sig)
    persfile.flush()
    persfile.close()
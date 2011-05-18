fp = open('contactos.csv','r')
i=1
res = []
ctactgr1 = {
    "pk":1,
    "model":"contacts.contactgroup",
    "fields":{"name": "Refugio", "description":""}
}
ctactgr2 = {
    "pk":2,
    "model":"contacts.contactgroup",
    "fields":{"name": "Institucional","description":""}
}
res.append(ctactgr1)    
res.append(ctactgr2)    

for line in fp.readlines():
    palabras = line.partition(',')
    gr = int(palabras[1].strip())
    ctact = {
        "pk":i,
        "model":"contacts.contact",
        "fields":{"last_name": "", "name": "", "email": palabras[0],"grupo":gr}
    }
    res.append(ctact)
    i+=1
    
print res

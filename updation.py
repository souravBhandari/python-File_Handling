
file=open("bank.dat","r")
dta=file.read()
records=dta.split("\n")
records=records[:-1]
id=input("enter id ")
for record in records:
    values=record.split(";")
    if (values[0]==id):
        #deposie amounnt
        amt=int(input("enter new amount"))
        values[3]=int(values[3])+amt
        records.remove(record)
    pos=records.index(record)
    records[pos]=values[0]+";"+values[1]+";"+values[2]+";"+str(values[3])

file=open("bank.dat","w")
for record in records:
    file.write(record+"\n") 
file.close()
    

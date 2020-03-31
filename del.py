file=open("bank.dat","r")
dta=file.read()
records=dta.split("\n")
records=records[:-1]
id=input("enter id which u want to del")
for record in records:
    values=record.split(";")
    if (values[0]==id):
        records.remove(record)
file=open("bank.dat","w")
for record in records:
    file.write(record+"\n") 
file.close()
    

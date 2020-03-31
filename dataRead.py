file=open("bank.dat","r")
dta=file.read()
records=dta.split("\n")
records=records[:-1]
for record in records:
    values=record.split(";")
    print("id :"+values[0])
    print("name :"+values[1])
    print("address:"+values[2])
    print("balance :"+values[3])
file.close()
    

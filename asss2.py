'''Develop a Bank software with following features:

1. Operator should be able to create new accounts.
2. Operator should be able to access individual account.
3. Operator should be able to search customer account and make deposits into it.
4. Operator should be able to search any customer account and close it's account.
5. Operator should be able to view all customer accounts.


def CreateAccount():
 ..

def SearchAccount():
 ..

def Deposit():
 ..

def Withdrawl():
 ..
 '''
def filee():
        file=open("Acc.dat","r")
        dta=file.read()
        records=dta.split("\n")
        records=records[:-1]
        id=input("enter id ")
        for record in records:
            values=record.split(",")
            if (values[0]==id):
def CreateAccount():

    file=open("Acc.dat","a")
    id=input("enter id")
    name=input("enter name")
    address=input("enter address")
    balance=input("enter balanced")
    file.write(id+","+name+","+address+","+balance+"\n")
    file.close()

def Deposit():
        filee()
        #deposie amounnt
            amt=int(input("enter amount to be deposit"))
            values[3]=int(values[3])+amt
            records.remove(record)
        pos=records.index(record)
        records[pos]=values[0]+";"+values[1]+";"+values[2]+";"+str(values[3])

    file=open("Acc.dat","w")
    for record in records:
        file.write(record+"\n") 
    file.close()
 

def Withdrawl():
            filee()
            amt=int(input("enter amount for withdrawl"))
            values[3]=int(values[3])+amt
            records.remove(record)
        pos=records.index(record)
        records[pos]=values[0]+";"+values[1]+";"+values[2]+";"-str(values[3])

    file=open("bank.dat","w")
    for record in records:
        file.write(record+"\n") 
    file.close()

def SearchAccount():
            filee()
            values=record.split(",")
            print("id :"+values[0])
            print("name :"+values[1])
            print("address:"+values[2])
            print("balance :"+values[3])
    file.close()

while(1):
    print("1: CreateAccount\n2: SearchingAccount\n3: deposite\n4: withdrawl\n0: Exit")
    ch=int(input("enter choice:"))
    if(ch==1):
       CreateAccount()
    if(ch==2): 
        SearchAccount()
    if(ch==3):
        Deposite()
    if(ch==4):
        Withdrawl()
    else:
        exit(0)

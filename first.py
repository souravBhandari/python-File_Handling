n=input("enter file name")
f=open(n,"w") # mode uh want to open the file
name=input("enter name")
f.write(name+"\n")
age=int(input("enter age"))
age=str(age)
f.write(age+"\"n)
f.close
print(f)
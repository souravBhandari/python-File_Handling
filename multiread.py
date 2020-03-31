f=open("student.dat","r")
data=f.read()
records=data.split("\n")
records=records[:-1]
print(records)
for record in records:
    recordata=record.split(",")

    print("id:",recordata[0])
    print("name:",recordata[1])
    print("course:",recordata[2])
    print("fees:",recordata[3])
f.close()
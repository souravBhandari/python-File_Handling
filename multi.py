file=open("student.dat","a")

id=input("enter id:")
name=input("enter ur name:")
course=input("enter course")
fees=input("enter fees")
# saving in woe-col format
file.write(id+","+name+","+course+","+fees+"\n")     
file.close()
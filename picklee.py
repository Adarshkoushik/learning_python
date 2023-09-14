import pickle,student
f=open("student.dat","wb")
s=student.Student(1,"Adarsh",99)
pickle.dump(s,f)
f.close()
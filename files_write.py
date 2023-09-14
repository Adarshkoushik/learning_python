f=open("myFile.txt","w")
print("Type # when you are done")
s=''
while s != '#':
    s=input()
    f.write(s+"\n")
f.close()
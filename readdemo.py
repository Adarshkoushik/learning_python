f=open("sample.txt","r")
print(f.read())     #Reads entire file
f.seek(0)           #moving cursor back to the 0th location
print(f.readline()) #Reads single line
print(f.readlines()) #Returns list of data in file


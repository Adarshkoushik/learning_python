f=open("sample.txt","w+")
f.write("Python is fun \n")  
f.writelines(['Python \n','DRF \n','Django \n','Docker \n']) #writing list to file
print('Cursor is at',f.tell())
f.seek(0)
print(f.read())
f.close()
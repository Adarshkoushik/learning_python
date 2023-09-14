import re
str = "Take up 1 one idea.one 23 idea at 45 a time 22-12-2033"
res=re.search(r'o\w\w',str)  #return string starting with o and followed by 2 chars
print(res.group())

res=re.findall(r'o\w\w',str)  #return list starting with o and followed by 2 chars
print(res)

res=re.match(r'o\w\w',str)  #return string starting with o and followed by 2 chars
print(res)

res=re.split(r'\d+',str)
print(res)

res=re.sub(r'one','two',str)
print(res)

res=re.findall(r'\d{1,2}-\d{1,2}-\d{4}',str)
print(res)

res=re.findall(r'o\w+',str)  #return list starting with o and followed by 2 chars
print(res)



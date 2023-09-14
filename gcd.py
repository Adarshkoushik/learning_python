def gcd(n1,n2):
    if n1>n2:
        smallnumber=n2
    else:
        smallnumber=n1
    
    for i in range(1,smallnumber+1):
        if n1%i==0 and n2%i==0:
            res=i
        #print(res,"res is")
    return res

ans=gcd(24,36)
print(ans)
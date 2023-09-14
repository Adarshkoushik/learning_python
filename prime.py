n=int(input("Enter a number to check if it is prime or not: "))
temp=False
if(n > 1):
    for i in range(2,n):
        if(n%i==0):
            temp=True
            break
if(temp):
    print(n, "is not prime number")
else:
    print(n,"is a prime number")
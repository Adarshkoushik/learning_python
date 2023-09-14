try:
    f=open("myfile","w")
    a,b=[int(x) for x in input("Enter two numbers:").split()]
    c=a/b
    print(c)
    f.write("Writing the value %d to file"%c)
except ZeroDivisionError:
    print("Division by zero not possible")
    print("Please enter non zero number")
finally:
    print("Inside finally block")
    f.close()

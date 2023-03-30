a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
c=input("Enter + , - , * , /,**")
if c=='+':
    if (a==56 and b==9):
        print("Sum is 77")

    else:
        print("Sum is ",a+b)
elif c=='-' :
    if (a==56 and b==6):
        print("Difference is 10")

    else :
        print("Difference is ",a-b)
elif c=='*':
    if (a==45 and b==3):
        print("Product is 555")
    else:
        print("Product is",a*b)
elif c=='/':
    if (a==56 and b==6):
        print("Division is 4")
    else:
        print("Division is ",a/b)
elif c=='**':
    print(b,"Power of",a,a**b)
else:
    print("Wrong Choice")
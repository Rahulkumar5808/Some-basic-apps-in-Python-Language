print("Enter your choice")
i=input("S for Stone , W for Water and G for Gun")
l=["S","W","G"]
import random
a=random.choice(l)
if( i =="g" or i=="G"):
    print("Computer choice is ", a)
    if(a=="S"):
        print("You wins and computer loose")
    elif(a=="W"):
        print("Computer wins and you loose")
    else:
        print("Tie")
elif(i=="w" or i=="W"):
    print("Computer choice is ",a)
    if (a == "G"):
        print("You wins and computer loose")
    elif (a == "S"):
        print("Computer wins and you loose")
    else:
        print("Tie")
elif(i=="S" or i=="s"):
    print("Computer choice is ",a)
    if (a == "W"):
        print("You wins and computer loose")
    elif (a == "G"):
        print("Computer wins and you loose")
    else:
        print("Tie")
else:
    print("Wrong Choice")
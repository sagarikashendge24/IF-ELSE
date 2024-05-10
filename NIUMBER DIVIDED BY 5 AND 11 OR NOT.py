user=int(input("ENTER THE NUMBER"))
if user%5==0:
    print("IT IS DIVIDED BY 5")
elif user%11==0:
    print("IT IS DIVIDED BY 11")
elif user%5==0 and user%11==0:
    print("IT IS DIVIDED BY BOTH")
else:
    print("NONE")
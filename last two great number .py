a=int(input("ENTER 1ST NUMBER"))
b=int(input("ENTER 2ND NUMBER"))
c=int(input("ENTER 3RD NUMBER"))
d=int(input("ENTER 4TH NUMBER"))
if a>b and a>c and a>d:
    if b>c and b>d:
        print("GREATER NUMBER IS",a,b) 
    elif c>b and c>d:
        print("GREATER NUMBER IS",a,c) 
    elif d>b and d>c:
        print("GREATER NUMBER IS",a,d)
if b>a and b>c and b>d:
    if a>c and a>d:
        print("GREATER NUMBER IS",b,a)
    elif c>a and c>d:
        print("GREATER NUMBER IS",b,c)
    elif d>c and d>a:
        print("GREATER NUMBER IS",b,d)  
if c>a and c>b and c>d:
    if a>d and a>b:
        print("GREATER NUMBER IS",c,a)
    elif b>d and b>a:
        print("GREATER NUMBER IS",c,b)
    elif d>a and d>b:
       print("GREATER NUMBER IS",c,d)
if d>a and d>b and d>c:
    if a>c and a>b:
        print("GREATER NUMBER IS",d,a)
    elif b>c and b>a :
        print("GREATER NUMBER IS",d,b)
    elif c>a and c>b:
        print("GREATER NUMBER IS",d,c)
else:
    print("ALL NUMBERS ARE EQUAL")                                                                  
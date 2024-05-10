x=10
y=20
z=30
if x==10:
    if y==20:
        print("End of nested if block")
    else:
        print("End of nested if else block")
elif y==20:
    print("Elif block") 
    if z==30:
        print("End of nested elif block")
    else :
        print("End of nested if else block")           
a=int(input("ENTER YOUR AGE"))
b=input("ENTER SEX MALE M OR FEMALE F")
c=input("MARITAL STATUS YES OR NO")
if b=="F":
    print("YOU WILL WORK IN URBAN AREA")
elif b=="M" and a>=20 and a<=40:
    print("YOU CAN WORK ANYWHERE")
elif b=="M" and a>=40 and a<=60:
    print("YOU WILL WORK ONLY IN URBAN AREA")
else:
    print("ERROR")
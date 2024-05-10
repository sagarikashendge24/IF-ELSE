yr=int(input("ENTER THE YEAR"))
if yr%4==0:
    if yr%100!=0:
        print("ENTERED YEAR IS LEAP YEAR")
    else :
        print("ENTERED YEAR IS NOT LEAP YEAR")
else:
    if yr%400==0:
        print("ENTERED YEAR IS LEAP YEAR")
    else:
        print("ENTERED YEAR IS NOT LEAP YEAR")

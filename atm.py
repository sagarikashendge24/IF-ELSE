print("WELCOME")
card=input("PLEASE INSERT YOUR CARD")
if card == chipside:
    print("TRANSACTION IS IN PROCESS")
    lang=input("SELECT THE LANGUAGE ")
    if lang==english or lang==hindi or lang==marathi:
        print("INPROCESS")
        pin=int(input("ENTER THE PIN"))
        pin1=2724
        if pin==pin1:
            print("INPROCESS")
            acc=input("TYPE OF ACCOUNT")
            if acc=="SAVING ACCOUNT" or "CURRENT ACCOUNT":
                print("INPROCESS")
                amt=int(input("ENTER THE AMOUNT TO BE WIDRAWAL")
                 if 10000>amt:
                    print("TRANSACTION IS IN PROCESS")
                    print("PLEASE COLLECT YOUR CASH")
                    rec=input("DO YOU WANT RECEPIT")
                    if rec==yes:
                        print("TAKE THE RECIPIT")
                        print("THANK YOU FOR BANKING WITH US")
                    else:
                        print("YOU ARE HELPING TO SAVE TREES") 
                else:
                    print("CASH CANNOT BE WIDRAWAL MORE THAN 10000 AT ONE TIME")  
            else:
                print("CORRECT THE ACCOUNT TYPE")   
        else:
            print("PLEASE ENTER THE CORRECT PIN") 
    else:
        print("ENTER THE CORRECT LANGUAGE ")    
else:
    print("PLEASE INSRE YOUR CARD AGAIN")                           

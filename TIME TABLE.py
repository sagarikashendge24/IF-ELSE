day=input("ENTER THE DAY")
meal=input("ENTER THE TIME MEAL TIME")
if day=="MONDAY":
    if meal=="BREAKFAST":
        print("POORI SABZI")
        if meal=="LUNCH":
            print("SAMBAR RICE")
            if meal=="DINNER":
                print("CHIKEN RICE")
                if day=="TUESDAY" :
                    if meal=="BREAKFAST":
                        print("POHA") 
                        if meal=="LUNCH":
                                 print("RAJMA RICE")
                            if meal=="DINNER":
                                print("ROTI SABZI")
                            else:
                                 print("PLEASE ENTER CORRECT DAY OR MEAL")
                        else:
                            print("PLEASE ENTER CORRECT DAY OR MEAL")
                    else:
                        print("PLEASE ENTER CORRECT DAY OR MEAL")  
                else:
                    print("PLEASE ENTER CORRECT DAY OR MEAL")  
            else:
                print("PLEASE ENTER CORRECT DAY OR MEAL")       
        else:
            print("PLEASE ENTER CORRECT DAY OR MEAL")
    else:
        print("PLEASE ENTER CORRECT DAY OR MEAL")   
else:
    print("PLEASE ENTER CORRECT DAY OR MEAL")
            
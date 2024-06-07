def seperetor(x):
    if 0<= x <= 20:
        if 0<= x <= 9.9 :
            print("Fail")
        elif 10 <= x <= 15:
            print("Good")
        elif 15 < x <= 18:
            print("very Good")  
        elif 18 < x <=20:
            print("excellent")     

    else :
        print("Invalid Grade")

seperetor(10)        
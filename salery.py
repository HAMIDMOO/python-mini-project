salery=[100, 50]

def Calculate_Salery(x):
    Monthly_salery=0
    overtime_salery = 0
    Surplus_salary = 0
    y=0
    if x <= 160:
        Monthly_salery= x* salery[0]
        print("Monthly_salery = ",Monthly_salery)
    else:
         y=abs(160-x)
         if y < 40:
             Monthly_salery= 160* salery[0]
             overtime_salery= y* salery[1]
             print("Monthly_salery :",Monthly_salery)
             print("overtime_salery :",overtime_salery)

         else:
                Monthly_salery= 160* salery[0]
                overtime_salery= 40* salery[1] 
                Surplus_salary= x-(160+40) 
                print("Monthly_salery :",Monthly_salery)
                print("overtime_salery :",overtime_salery)
                print("Surplus_salary :",Surplus_salary)


         

Calculate_Salery(800)


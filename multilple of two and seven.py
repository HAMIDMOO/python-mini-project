def multiple_two_seven(x):
    if x%2==0 :
        if x%7==0:
            print("This number is a multiple of two and seven")
        else:   print("This number is not a multiple of two and seven") 
    else:
        print("This number is not a multiple of two and seven")

multiple_two_seven(int(input("Enter a number : ")))
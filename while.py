ifUserAnswered = False

while ifUserAnswered == False:
    answer = input("What is your age?: ")

    if answer:
        if answer.isdecimal():
            ifUserAnswered = True
            print("Your age is : %s" % answer )
        else:
            print("Your answer is wrong!")
        
        
    

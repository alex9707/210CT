#Function continues through dividing the user input each time then subtracting one.
#This will continue until one is reached or the number is found to be prime.

def primenumbers(number,value):
    if value<=1:
        print("False")
    else:
        if number%value==0:
            print("True")
        else:
            if value>=1:
                value=value-1
                primenumbers(number,value)
            else:
                print("False")

number=int(input("Enter an integer: "))
value=number-1
primenumbers(number,value)

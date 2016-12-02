#Function uses a for loop based on user input until a square value larger than the input is reached
#The value previous to this is then calculcated and printed as the highest perfect square

def perfectsquare(number):
    for i in range(1,number,1):
        ii=int(i)
        iii=ii*ii
        if iii>number:
            value=ii-1
            print(value)
            break

number=int(input("Please enter number: "))
perfectsquare(number)

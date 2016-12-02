def perfectsquare(number):
#The function perfect square has variable number defined
    for i in range(1,number,1):
#For loop is used in the range of 1 to the given user input
        ii=int(i)
#i is converted to an integer so it can be multiplied
        iii=ii*ii
#The integer ii is multiplied by itself
        if iii>number:
#When iii becomes larger than the user input the if statement will be used
            value=ii-1
#One will be subtracted from ii
            print(value)
#This will find the value needed which will then be printed
            break
#The loop will then break

number=int(input("Please enter number: "))
#Requests user input and converts to integer
perfectsquare(number)
#The function perfectsquareiscalled

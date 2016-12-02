def trailingzeros(number):
#function to calculate trailing zeros with variable number defined
    answer=1
#Will be used times with the input number
    while number>0:
#while loop will iterate until the base case of zero is reached
        answer=answer*number
#For each iteration the number will times by the defined answer eventually reaching the factorial number
        number=number-1
#For each iteration number will decrease towards the base case of zero
    print(answer)
#The factorial number will be printed
    stranswer=str(answer)
#factorial number is then converted to a string
    countzeros(stranswer)
#The function countzeros is then called

def countzeros(stranswer):
#Function to calculate number of trailing zeros
    count=stranswer.rstrip('0')
#This will remove the last zeros from the string
    value=len(stranswer)-len(count)
#The length of the original factorial is compared to the new new string to calculate the number of trailing zeros
    print(value)
#The number of trailing zeros is printed

number=int(input("Please enter input: "))
#Requests input from the user and converts to an integer
trailingzeros(number)
#The function trailingzeros is called

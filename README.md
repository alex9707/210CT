import random #Imports the random module which is used in the function shuffle

def shuffle(numbers1): #Takes input from the user
    for i in range(1,9,1): #Used a for loop to continue until the list is empty
            number=random.choice(numbers1) #Takes a random number from the list
            print(number) #This number is then printed
            numbers1.remove(number) #The number is then removed from the list so there is no duplicate

numbers=input("Enter 8 numbers to be shuffled: ")
#Will provide an input for the user to enter the values of the list
numbers1=list(numbers)
#Created the list from the input
shuffle(numbers1)
#Calls the function shuffle

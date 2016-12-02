#Imports the random module which is used in the function shuffle
import random

#The function iterates through the list picking a random number each time
def shuffle(numbers):
    for i in range(1,len(numbers)+1,1):
            number=random.choice(numbers)
            print(number)
            numbers.remove(number)

numbers=[]
userinput=input("Please enter list of numbers: ")
inputsplit=userinput.split(",")
for l in inputsplit:
    ll=int(l)
    numbers.append(ll)
shuffle(numbers)

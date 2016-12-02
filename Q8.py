#The function will run through each if statement removing each vowel as it runs through
#The output will print the string without any vowels

def vowels(stringinput):
    if "a" in stringinput:
        stringinput=stringinput.replace("a","")
    if "e" in stringinput:
        stringinput=stringinput.replace("e","")
    if "i" in stringinput:
        stringinput=stringinput.replace("i","")
    if "o" in stringinput:
        stringinput=stringinput.replace("o","")
    if "u" in stringinput:
        stringinput=stringinput.replace("u","")
    print(stringinput)
    
stringinput=input("Enter string: ")
vowels(stringinput)

#A for loop is used to iterate through the string
#It iterates from back to front appending each word to a new list as it goes through
#This results in the output being the original string reversed
def reverse(string,emptylist):
    for i in range(len(string)-1,0,-1):
        emptylist.append(string[i])
    emptylist.append(string[0])
    output=' '.join(emptylist)
    print(output)

#Asks for input which is then split between each space and passed into the function reverse
emptylist=[]
stringunsplit=input("Enter a string")
string=stringunsplit.split(' ')
reverse(string,emptylist)

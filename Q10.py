#Sequence breaks up list when it descends
#The list will then be compared to the previous longest list
#For loop is used which will finish when the list has been run through

def Sequence(L):
    originallist=[]
    longlist=[]
    iteration=1
    lengthL=len(L)
    for a in L:
        aa=int(a)
        if iteration==lengthL:
            originallist.append(a)
            if len(longlist)<len(originallist):
                longlist=originallist
        else:
            if aa<int(L[iteration]):
                originallist.append(a)
            else:
                originallist.append(a)
                if len(longlist)<len(originallist):
                    longlist=originallist
                originallist=[]
        iteration=iteration+1
    return(longlist)

L=[]
userinput=input("Please enter list of numbers: ")
inputsplit=userinput.split(",")
for l in inputsplit:
    ll=int(l)
    L.append(ll)
print(Sequence(L))

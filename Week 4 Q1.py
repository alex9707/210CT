#The binarysearch function will use input for high and low boundaries
#The list of numbers will then be checked to see if it is within the boundary
#If the any of the numbers in the list are in this boundary it wil be printed that there is a number in this boundary

def binarysearch(L, Low, High):
    for i in L:
        Length=len(L)
        ii=int(i)
        iii=ii-1
        value1=int(L[iii])
        if value1>=Low and value1<=High:
            print("There is a value in the list in the given boundaries!")
            break
        else:
            if ii==Length:
                print("There is no value in the list in the given boundaries!")
                break

LL=input("Please enter list of numbers: ")
Lo=input("Please enter lowest boundary: ")
Hig=input("Please enter highest boundary: ")
L=list(LL)
Low=int(Lo)
High=int(Hig)
binarysearch(L, Low, High)

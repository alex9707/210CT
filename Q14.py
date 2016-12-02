class Graph:
    #__init__ is used to create the empty dictionary that is used in other functions
    def __init__(self):
        self.dictionary={}

    #Edge function used to add edges
    #For loop used to iterate through nodes in dictionary to find correct nodes
    #Once found the nodes and their connections are added to the dictionary
    #Nodes and their connections are then printed
    def edge(self, firstnode, secondnode):
        for i in range(1, len(self.dictionary)):
            listkeys=list(self.dictionary.keys())
            node1=int(firstnode)
            node2=int(secondnode)
            if node1==listkeys[i] or node2==listkeys[i]:
                self.dictionary[node1].append(node2)
                self.dictionary[node2].append(node1)
                break
        lengthdictionary=len(self.dictionary)
        for i in range(1, lengthdictionary+1):
            print(i, " : ", self.dictionary[i])

    #This function adds the nodes and edges to the dictionary
    def addtodictionary(self, key, value):
        self.dictionary[key]=value

    #Function uses depth first search to find optimum path
    #Uses if statements and a for loop to append nodes into the list emptylist
    #This list is then printed
    def depthfirstsearch(self, iteration, end, start=True):
        if start==True:
            start=iteration
        emptylist.append(start)
        if start==end:
            print("Using depth first search the path is:", emptylist)
        for i in self.dictionary[start]:
            if i not in emptylist:
                self.depthfirstsearch(iteration, end, i)

    #While loop is used to continue iterations to find optimum path
    #Within while loop the for loops will append the path to the list emptylist
    def breadthfirstsearch(self, startingnode, endnode):
        value = []
        emptylist.append(startingnode)
        dictionarylength=len(self.dictionary[startingnode])
        while True:
            for a in range(1, dictionarylength+1):
                comparison=self.dictionary[startingnode][a-1]
                if comparison==endnode:
                    emptylist.append(endnode)
                    print("Using breadth first search the path is:",emptylist)
                    return
                else:
                    if comparison!=emptylist:
                        emptylist.append(comparison)
            for b in range(0,2):
                if emptylist[b]!=value[b]:
                    break
        
#Calls functions and passes nodes and connections to the functions
if __name__ == '__main__':
    g=Graph()
    g.addtodictionary(1, [2,4])
    g.addtodictionary(2, [3,4])
    g.addtodictionary(3, [1])
    g.addtodictionary(4, [2])
    g.edge(3,4)
    emptylist=[]
    g.depthfirstsearch(1,3)
    emptylist=[]
    g.breadthfirstsearch(1,2)

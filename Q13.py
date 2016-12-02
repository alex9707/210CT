class Graph:
    def __init__(self):
        self.dictionary={}

    def edge(self, node11, node22):
        trueorfalse=False
        for i in range(1, len(self.dictionary)):
            listkeys=list(self.dictionary.keys())
            node1=int(node11)
            node2=int(node22)
            if node1==listkeys[i] or node2==listkeys[i]:
                self.dictionary[node1].append(node2)
                self.dictionary[node2].append(node1)
                trueorfalse=True
                break
        lengthdictionary=len(self.dictionary)
        for i in range(1, lengthdictionary+1):
            print(i, " : ", self.dictionary[i])

    def addtodictionary(self, key, value):
        self.dictionary[key]=value

if __name__ == '__main__':
    g=Graph()
    g.addtodictionary(1, [2])
    g.addtodictionary(2, [3,4])
    g.addtodictionary(3, [1])
    g.addtodictionary(4, [2])
    g.edge(3,4)

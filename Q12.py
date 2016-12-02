class BinTreeNode(object):
    def __init__(self, value):
        self.value=value
        self.left=None
        self.right=None

def tree_insert( tree, item):
    if tree==None:
        tree=BinTreeNode(item)
    else:
        if(item < tree.value):
            if(tree.left==None):
                tree.left=BinTreeNode(item)
            else:
                tree_insert(tree.left,item)
        else:
            if(tree.right==None):
                tree.right=BinTreeNode(item)
            else:
                tree_insert(tree.right,item)
    return tree

def postorder(tree):
    if(tree.left!=None):
        postorder(tree.left)
    if(tree.right!=None):
        postorder(tree.right)
    print(tree.value)

#Function uses a while loop to iterate through until the end of the tree is reached
#Nodes in the list will be moved into the stack
#Pop is used to remove the nodes from the stack
#The function will then print the tree in order
def in_order(tree):
    a=True
    treestack=[]
    while a==True:
        if tree!=None:
            treestack.append(tree)
            tree=tree.left
        else:
            lengthstack=len(treestack)
            if lengthstack>=1:
                tree=treestack.pop()
                print(tree.value)
                tree=tree.right
            else:
                a=False

if __name__ == '__main__':
    t=tree_insert(None,6);
    tree_insert(t,10)
    tree_insert(t,5)
    tree_insert(t,2)
    tree_insert(t,3)
    tree_insert(t,4)
    tree_insert(t,11)
    in_order(t)

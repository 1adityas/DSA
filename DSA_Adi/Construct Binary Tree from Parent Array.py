'''
# A node structure
class Node:
    # A utility function to create a new node
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
'''
#https://practice.geeksforgeeks.org/problems/construct-binary-tree-from-parent-array/0/?track=DSASP-Tree&batchId=155#
def createTree(parent,n):
    # your code here
    a=parent
    obj=Node(a[0])
    d={}
    
    c=0
    for i in a:
        obj=Node(c)
        if i==-1:
            root=obj
            
        if d.get(i)!=None:
            d[i].append(obj)
        else:
            # print(obj.key)
            d[i]=[]
            d[i].append(obj)
        c+=1
    
    return(Constr_bt(d,root))
    #returns root of constructed binary tree 
        
def Constr_bt(d,root):
    l=[]
    l.append(d[-1][0])
    while len(l)!=0:
        a=l.pop()
        k=a.key
        if d.get(k):
            if len(d[k])==1:
                a.left=d[k][0]
                l.append(d[k][0])
            elif len(d[k])==2:
                a.left=d[k][0]
                a.right=d[k][1]
                l.append(d[k][0])
                l.append(d[k][1])
    return root
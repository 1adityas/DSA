#from gfg
def isSubTree(T1, T2):#take input root node of both trees 
    if T2 ==None :
        return True
    if T1 ==None :
        return False 
    a1,a2,aa1,aa2=[],[],[],[]
    inorder(T1,a1)
    preorder(T1,a2)
    inorder(T2,aa1)
    preorder(T2,aa2)
    s1=''.join(map(str, a1))
    s2=''.join(map(str, a2))
    ss1=''.join(map(str, aa1))
    ss2=''.join(map(str, aa2))
    # print(s1,s2,ss1,ss2,s1.find(ss1),s2.find(ss2))
    if s1.find(ss1)!=-1 and s2.find(ss2)!=-1:return True
    else:return False
    
def inorder(root,a):
    if root:
        a.append(root.data)
        inorder(root.left,a)
        inorder(root.right,a)
    else:
        a.append(-1) 
#append -1 to distinguish the NULL values, important to identify the structure of tree
def preorder(root,a):
    if root:
        preorder(root.left,a)
        a.append(root.data)
        preorder(root.right,a)
    else:
        a.append(-1) 
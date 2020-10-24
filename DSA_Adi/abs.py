#its done in O(n)
#https://practice.geeksforgeeks.org/problems/top-view-of-binary-tree/1#
from collections import defaultdict 
def topView(root):#takes input as tree root 
    m=defaultdict(int)
    traverse(root, m, 0,0)
    mn = 100000
    mx = -100000
     
    for key,value in m.items():
        if mx < key:
            mx = key
        if mn > key:
            mn = key
    i = mn
    while i <= mx:
        print (m[i][0],end = " ")
        i = i+1

def traverse(root, m, hd,level):
    if not root:
        return 
    if hd in m:
        if level < m[hd][1]:
            m.update( {hd : [root.data,level] })
    else:
        m[hd] = [root.data,level]

    traverse(root.left, m, hd-1,level+1)
    traverse(root.right,m, hd+1, level+1)
    

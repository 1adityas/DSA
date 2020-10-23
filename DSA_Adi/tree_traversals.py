#all traversal code
class Node: 
    def __init__(self,val): 
        self.left = None
        self.right = None
        self.val = val
    
class b_tree():
    def __init__(self,root):
        self.root=Node(root)
        
    def InOrderTrav(self,next):
        if next:
            self.InOrderTrav(next.left)
            print(next.val)
            self.InOrderTrav(next.right)
        
    def PreOrderTrav(self,next):
        if next:
            print(next.val)
            self.PreOrderTrav(next.left)
            self.PreOrderTrav(next.right)
        
    def PostOrderTrav(self,next):
        if next:
            self.PostOrderTrav(next.left)
            self.PostOrderTrav(next.right)
            print(next.val)
        
tree=b_tree(1)
tree.root.left = Node(2) 
tree.root.right = Node(3)
tree.root.left.left=Node(4)
tree.root.left.right=Node(5)
tree.root.right.left=Node(6)
tree.root.right.right=Node(7)

'''call any traversal on tree'''
# tree.PreOrderTrav(tree.root)
# tree.InOrderTrav(tree.root)
# tree.PostOrderTrav(tree.root)
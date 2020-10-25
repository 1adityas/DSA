#User function Template for python3

#https://practice.geeksforgeeks.org/problems/level-order-traversal-in-spiral-form/1#
'''
Level order in spiral form traversal
class Node:
    def init(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
#usign stack
# your task is to complete this function
# function should print the level order traversal of the binary tree in spiral order
# Note: You aren't required to print a new line after every test case
def findSpiral(root):
    s1=[]
    s2=[]
    s2.append(root)
    if root==None:return []
    while len(s1) or  len(s2):
        if len(s1):
            for i in range(len(s1)):
                pr=s1.pop()
                print(pr.data,end=" ")
                if pr.left:s2.append(pr.left)
                if pr.right:s2.append(pr.right)
        if len(s2):
            for i in range(len(s2)):
                pr=s2.pop()
                # print(s2)
                print(pr.data,end=" ")
                if pr.right:s1.append(pr.right)
                if pr.left:s1.append(pr.left)
    return []
    
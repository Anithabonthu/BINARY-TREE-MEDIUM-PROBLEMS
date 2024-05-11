#!/usr/bin/env python
# coding: utf-8

# In[2]:


class Node: 
    def __init__(self,v): 
        self.left=None 
        self.data=v 
        self.right=None 

class BinaryTree: 
    def __init__(self): 
        self.root=None 
    def create_root(self,value): 
        newnode = Node(value) 
        self.root=newnode 
        self.create_child(newnode) 

    def create_child(self,parent): 
        enq=input("is left child available for %d press y/n: "%parent.data).lower()
        if enq=='y': 
            lc=int(input("enter left child for %d: " %parent.data)) 
            parent.left=Node(lc) 
            self.create_child(parent.left) 
        enq=input("is right child available for %d:  press y/n: "%parent.data).lower()
        if enq=='y': 
            rc=int(input("enter right child for %d: " %parent.data)) 
            parent.right=Node(rc) 
            self.create_child(parent.right) 
def printTree(l):
    for i in l:
        for j in i:
            print(j,end=" ")
        print()
def paths(root):
    ans=[]
    rstack=[]
    dfs(root,ans,rstack)
    return ans
def dfs(root,ans,rstack):
    rstack.append(root.data)
    if root.left:
        dfs(root.left,ans,rstack)
    if root.right:
        dfs(root.right,ans,rstack)
    if not(root.left or root.right):
        ans.append(rstack[:])
    rstack.pop()
bt=BinaryTree() 
while True: 
    print("1.Create Tree 2.Exit") 
    ch=int(input("Enter choice: ")) 
    if ch==1: 
        rt = int(input("Enter root:")) 
        bt.create_root(rt) 
    elif ch==2: 
        break
l=paths(bt.root)
printTree(l)


# In[ ]:





# In[ ]:





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
def evaluateTree(root):
    val=dfs(root)
    if val==1:
        return True
    return False      
def dfs(node):
    if not node.left and not node.right:
        return node.data
    l=dfs(node.left)
    r=dfs(node.right)
    if node.data==3:
        if l==1 and r==1:
            return 1
        else:
            return 0
    if node.data==2:
        if l==0 and r==0:
            return 0
        else:
            return 1
        return node.data
bt=BinaryTree() 
while True: 
    print("1.Create Tree 2.exit") 
    ch=int(input("Enter choice: ")) 
    if ch==1: 
        rt = int(input("Enter root:")) 
        bt.create_root(rt) 
    elif ch==2: 
        break
print(evaluateTree(bt.root))


# In[ ]:





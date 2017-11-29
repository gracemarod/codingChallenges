"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)
"""


def levelOrder(root):
    h = height(root)
    
    for i in range(1,h+1):
        givenLevel(root,i)

def givenLevel(root,i):
    if root == None:
        return
    if i == 1:

        print root.data,
    else:
        
        givenLevel(root.left,i-1)
        givenLevel(root.right,i-1)
        
def height(root):
    if root == None:
        return 0
    else:
        return max(height(root.left),height(root.right))+1


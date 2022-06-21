class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None



def inorder(root):
    if root is not None:
        
        inorder(root.left)

        
        print(str(root.key) + "->", end=' ')

        
        inorder(root.right)



def insert(node, key):

    
    if node is None:
        return Node(key)

   
    if key < node.key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)

    return node


# Find the inorder successor
def minValueNode(node):
    current = node

   
    while(current.left is not None):
        current = current.left

    return current



def deleteNode(root, key):

    
    if root is None:
        return root

   
    if key < root.key:
        root.left = deleteNode(root.left, key)
    elif(key > root.key):
        root.right = deleteNode(root.right, key)
    else:
        
        if root.left is None:
            temp = root.right
            root = None
            return temp

        elif root.right is None:
            temp = root.left
            root = None
            return temp

       
        temp = minValueNode(root.right)

        root.key = temp.key

      
        root.right = deleteNode(root.right, temp.key)

    return root


root = None
root = insert(root, 86)
root = insert(root, 35)
root = insert(root, 12)
root = insert(root, 16)
root = insert(root, 75)
root = insert(root, 10)
root = insert(root, 14)
root = insert(root, 49)
root = insert(root, 69)
print("Inorder traversal: ", end=' ')
inorder(root)

print("\nDelete 69")
root = deleteNode(root, 69)
print("Inorder traversal: ", end=' ')
inorder(root)
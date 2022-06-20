class newNode:


	def __init__(self, data):
		self.key= data
		self.left = None
		self.right = self.parent = None


def insert(root, key):


	newnode = newNode(key)

	x = root


	y = None

	while (x != None):
		y = x
		if (key < x.key):
			x = x.left
		else:
			x = x.right
	

	if (y == None):
		y = newnode


	elif (key < y.key):
		y.left = newnode


	else:
		y.right = newnode


	return y


def Inorder(root) :

	if (root == None) :
		return
	else:
		Inorder(root.left)
		print( root.key, end = " " )
		Inorder(root.right)
						

if __name__ == '__main__':


	root = None
	root = insert(root, 69)
	insert(root, 34)
	insert(root, 21)
	insert(root, 46)
	insert(root, 72)
	insert(root, 69)
	insert(root, 89)


	Inorder(root)


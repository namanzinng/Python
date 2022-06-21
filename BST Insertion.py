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
		print(root.key, end = " " )
		Inorder(root.right)
						

if __name__ == '__main__':



	root = None
	root = insert(root, 50)
	insert(root, 30)
	insert(root, 20)
	insert(root, 40)
	insert(root, 70)
	insert(root, 60)
	insert(root, 80)


	Inorder(root)


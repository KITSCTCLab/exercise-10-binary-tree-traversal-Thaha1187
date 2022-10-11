class BinaryTreeNode:
    
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None


def insert(root, new_value) -> BinaryTreeNode:
      """If binary search tree is empty, make a new node, declare it as root and return the root.
        If tree is not empty and if new_value is less than value of data in root, add it to left subtree and proceed recursively.
        If tree is not empty and if new_value is >= value of data in root, add it to right subtree and proceed recursively.
        Finally, return the root.
        """
   # Write your code here
        if self.data:
            if data<self.data:
                if self.left is Null:
                    self.left = BinaryTreeNode(data)
                else:
                    self.left.append(data)
            else if(data>self.data):
                if self.right is Nill:
                    self.right = BinaryTreeNode(data)
                 else:
                    self.right.append(data)
         else:
            self.data = data


def inorder(root) -> None:
        # Write your code here
        def inorderTraversal(self, root):
            res = []
            if root:
                res = self.inorderTraversal(root.left)
                res.append(root.data)
                res = res + self.inorderTraversal(root.right)
        return res


 def preorder(root) -> None:
        # Write your code here
        def PreorderTraversal(self, root):
            res = []
            if root:
                res.append(root.data)
                res = res + self.PreorderTraversal(root.left)
                res = res + self.PreorderTraversal(root.right)
            return res


def postorder(root) -> None:
        # Write your code here
      def PostorderTraversal(self, root):
            res = []
            if root:
                res = self.PostorderTraversal(root.left)
                res = res + self.PostorderTraversal(root.right)
                res.append(root.data)
            return res


# Do not change the following code
input_data = input()
flag = True
root = None
for item in input_data.split(', '):
    if flag is True:
        root = insert(None, int(item))
        flag = False
    else:
        insert(root, int(item))
inorder(root)
print()
preorder(root)
print()
postorder(root)

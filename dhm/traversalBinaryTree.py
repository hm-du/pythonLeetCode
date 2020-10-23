# 二叉树遍历

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left,self.right = None, None
         

# 前序遍(Pre-order):根-左-右
def preorder(self, root):
    
    if root:
        self.traverse_path.append(root.val)
        self.preorder(root.left)
        self.preorder(root.right)

# 中序遍历(In-order):左-根-右
def inorder(self, root):
    
    if root:
        self.inorder(root.left)
        self.traverse_path.append(root.val)
        self.inorder(root.right)

#后序遍历(Post-order):左-右-根
def postorder(self, root):
    
    if root:
        self.postorder(root.left)
        self.postorder(root.right)
        self.traverse_path.append(root.val)
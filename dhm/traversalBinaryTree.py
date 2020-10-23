# ����������

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left,self.right = None, None
         

# ǰ���(Pre-order):��-��-��
def preorder(self, root):
    
    if root:
        self.traverse_path.append(root.val)
        self.preorder(root.left)
        self.preorder(root.right)

# �������(In-order):��-��-��
def inorder(self, root):
    
    if root:
        self.inorder(root.left)
        self.traverse_path.append(root.val)
        self.inorder(root.right)

#�������(Post-order):��-��-��
def postorder(self, root):
    
    if root:
        self.postorder(root.left)
        self.postorder(root.right)
        self.traverse_path.append(root.val)
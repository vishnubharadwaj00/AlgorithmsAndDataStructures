class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: TreeNode, lessthan=float('inf'), largerthan=float('-inf')) -> bool:
        if not root:
            return True
        if root.val<=largerthan or root.val>=lessthan:
            return False
        return self.isValidBST(root.left,min(root.val,lessthan),largerthan) and self.isValidBST(root.right,lessthan,max(largerthan,root.val))
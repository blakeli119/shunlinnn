# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
        """
        :type val: int
        :type left: TreeNode or None
        :type right: TreeNode or None
        """
class Solution(object):
    def insert(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode(inserted node)
        """
        if val <= root.val:
            if root.left is not None:
                return Solution().insert(root.left,val)
            else:
                root.left=TreeNode(val)
                return root.left
        else :
            if root.right is not None:
                return Solution().insert(root.right,val)
            else:
                root.right=TreeNode(val)
                return root.right
        
    def delete(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: TreeNode(the root of new completed binary search tree) (cannot search())
        """
    def search(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: TreeNode(searched node)
        """
        if root.val==target:
            return root
        elif target<root.val:
            return Solution().search(root.left,target)
        elif target>root.val:
            return Solution().search(root.right,target)
        else:
            return None
        
    def modify(self, root, target, new_val):
        """
        :type root: TreeNode
        :type target: int
        :type new_val: int
        :rtype:TreeNode(the root of new completed binary search tree) (cannot search())
        """

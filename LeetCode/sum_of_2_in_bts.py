class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def build(self, i, values):        
        root = TreeNode(values[i])
        #print(values[i])
        
        if 2*i + 1 < len(values) and values[2*i + 1] is not None:
            root.left = self.build(2*i + 1, values)

        if 2*i + 2 < len(values) and values[2*i + 2] is not None:
            root.right = self.build(2*i + 2, values)

        return root


class Solution(object):
    def visit(self, root, k, diff):
        if root.left is not None:
            if self.visit(root.left, k, diff):
                return True
        
        if len(diff) > 0 and root.val > diff[0]:
            return False
        
        for i in diff:
            if root.val == i:
                return True
        
        if root.val <= (k / 2.):
            diff.append(k - root.val)
        
        if root.right is not None:
            if self.visit(root.right, k, diff):
                return True
        
        return False
    
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        return self.visit(root, k, [])


if __name__ == '__main__':
    tree_values = [5, 3, 6, 2, 4, None, 7]
    root = TreeNode(0).build(0, tree_values)

    s = Solution()
    print(s.findTarget(root, 9))

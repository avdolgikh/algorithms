from tree_utils import *

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        output = []

        if root is not None:
            stack = [root]

            while len(stack) > 0:            
                root = stack.pop()
                output.append(root.val)

                if root.right is not None:
                    stack.append(root.right)

                if root.left is not None:
                    stack.append(root.left)

        return output


if __name__ == '__main__':
    tree_values = [1, None, 2, 3]
    root = TreeNode(0).build(0, tree_values)
    s = Solution()
    print(s.preorderTraversal(root))

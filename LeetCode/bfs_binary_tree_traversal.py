from tree_utils import *
from collections import deque

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        output = []

        if root is not None:
            q = deque()
            q.append(root)

            level = 0
            nodes = 1
            absent_child_nodes = 0
            level_result = []

            while len(q) > 0:
                root = q.popleft()
                level_result.append(root.val)
                nodes -= 1
                
                if root.left is not None:
                    q.append(root.left)
                else:
                    absent_child_nodes += 1

                if root.right is not None:
                    q.append(root.right)
                else:
                    absent_child_nodes += 1

                if nodes == 0:
                    level += 1
                    nodes = 2 ** level - absent_child_nodes
                    absent_child_nodes = 2 * absent_child_nodes
                    output.append(level_result)
                    level_result = []

        return output


if __name__ == '__main__':
    tree_values = [1,2,None,3,None,4,None,5]
    root = TreeNode(0).build(0, tree_values)
    s = Solution()
    print(s.levelOrder(root))

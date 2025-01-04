# https://www.educative.io/module/page/8q5JgjuzjGkprAwQG/10370001/5742435646570496/6190644206501888

from binary_tree import TreeNode


def diameter_of_binaryTree(root):
    def dfs(node):
        """Returns the height of the current node and updates the diameter."""
        if not node:
            return 0  # Base case: Height of a null node is 0
        
        left_height = dfs(node.left)  # Height of the left subtree
        right_height = dfs(node.right)  # Height of the right subtree
        
        # Update the diameter (path through this node)
        nonlocal diameter
        diameter = max(diameter, left_height + right_height)
        
        # Return the height of this node
        return max(left_height, right_height) + 1

    diameter = 0
    dfs(root)
    return diameter



if __name__ == "__main__":
    for tree in [
        None,
        [],
        [1, [2], [3, None, [4]]],
        [1, [2], [3, [4], [5, None, [6]]]],
        [5, [3, [2], [4]], [7, [6], [8]]],
        [
            10,
            [6, [3, [1], [4]], [8, [7], [9]]],
            [14, [12], [16]]
        ],
    ]:
        root = TreeNode.build_tree(tree)
        print(f"{root} --> {diameter_of_binaryTree(root)}")

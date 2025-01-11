# https://www.educative.io/module/page/8q5JgjuzjGkprAwQG/10370001/5742435646570496/6084660293271552


from binary_tree import TreeNode


def max_path_sum(root):
    def dfs(node):
        if not node:
            return 0

        # Calculate maximum branch sums for left and right subtrees
        left_branch_sum = dfs(node.left)
        right_branch_sum = dfs(node.right)

        # Update the global max path sum
        nonlocal max_sum
        max_sum = max(
            max_sum,
            left_branch_sum + node.data,
            node.data,
            node.data + right_branch_sum,
            left_branch_sum + node.data + right_branch_sum,
        )

        # Return the maximum branch sum including the current node
        return max(
            node.data,
            left_branch_sum + node.data,
            right_branch_sum + node.data,
        )

    max_sum = float("-inf")
    dfs(root)
    return max_sum


if __name__ == "__main__":
    for tree in [
        None,
        [],
        [1, [2], [3, None, [4]]],
        [1, [2], [3, [4], [5, None, [6]]]],
        [100, [50, [25], [75]], [200, None, [350]]],
        [-100, [-50, [-25], [-75]], [-200, None, [-350]]],
        [5, [3, [2], [4]], [7, [6], [8]]],
        [
            10,
            [6, [3, [1], [4]], [8, [7], [9]]],
            [14, [12], [16]]
        ],
    ]:
        root = TreeNode.build_tree(tree)
        print(f"{root} --> {max_path_sum(root)}")

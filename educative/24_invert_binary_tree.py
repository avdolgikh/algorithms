# https://www.educative.io/module/page/8q5JgjuzjGkprAwQG/10370001/5742435646570496/6294914914320384

from binary_tree import TreeNode


# Preorder DFS
def mirror_binary_tree(root):
    if root:
        stack = [root]

        while stack:
            node = stack.pop()
            node.left, node.right = node.right, node.left
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

    return root


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
        print(f"{root} --> {mirror_binary_tree(root)}")
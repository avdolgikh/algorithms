# https://www.educative.io/module/page/8q5JgjuzjGkprAwQG/10370001/5742435646570496/5614777407373312


from collections import deque
from binary_tree import TreeNode


def is_symmetric(root):
    if not root:
        return True

    queue = deque([(root.left, root.right)])
    while queue:
        left, right = queue.popleft()
        if not left and not right:
            continue
        if not left or not right or left.data != right.data:
            return False
        queue.append((left.left, right.right))
        queue.append((left.right, right.left))

    return True


if __name__ == "__main__":
    for tree in [
        None,
        [],
        [1],
        [1, [2]],
        [1, [2], [3, None, [4]]],
        [1, [2], [3, [4], [5, None, [6]]]],
        [1, [2, [3], [4]], [2, [4], [3]]],
    ]:
        root = TreeNode.build_tree(tree)
        print(f"{root} --> {is_symmetric(root)}")

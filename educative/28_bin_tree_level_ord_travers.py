# https://www.educative.io/module/page/8q5JgjuzjGkprAwQG/10370001/5742435646570496/6218683262959616


from collections import deque
from binary_tree import TreeNode


def level_order_traversal(root):
    if not root:
        return "None"

    result = []
    q = deque([root])

    while q:
        level_size = len(q)  # Number of nodes in the current level
        level_nodes = []

        for _ in range(level_size):
            node = q.popleft()
            level_nodes.append(str(node.data))

            # Enqueue child nodes
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        # Append this level's nodes to the result
        result.append(", ".join(level_nodes))

    return " : ".join(result)


# def level_order_traversal(root):
#     if not root:
#         return "None"

#     result = []
#     cur_level = 0
#     q = deque([(root, cur_level)])

#     while q:
#         node, level = q.popleft()

#         # Add a separator for a new level
#         if level > cur_level:
#             cur_level = level
#             result.append(" : ")
#         elif result:  # Add a comma separator for the same level
#             result.append(", ")

#         # Append the current node's data
#         result.append(str(node.data))

#         # Enqueue children with incremented level
#         if node.left:
#             q.append((node.left, level + 1))
#         if node.right:
#             q.append((node.right, level + 1))

#     return ''.join(result)



if __name__ == "__main__":
    for tree in [
        None,
        [],
        [1],
        [1, [2]],
        [1, [2], [3, None, [4]]],
        [1, [2], [3, [4], [5, None, [6]]]],
        [1, [2, [3], [4]], [2, [4], [3]]],
        [150, [32, [12]], [200, [172], [250]]],
    ]:
        root = TreeNode.build_tree(tree)
        print(f"{root} --> {level_order_traversal(root)}")

# https://www.educative.io/module/page/8q5JgjuzjGkprAwQG/10370001/5742435646570496/5672567198973952


from binary_tree import TreeNode


def serialize(root):
    stream = []

    if not root:
        return stream
    
    def dfs(node):
        if node:
            stream.append(node.data)
            dfs(node.left)
            dfs(node.right)
        else:
            stream.append(None)

    dfs(root)
    return stream


def deserialize(stream):
    if not stream:
        return None
    
    stream_iter = iter(stream)
    
    def dfs():
        value = next(stream_iter)
        if value is None:
            return None
        node = TreeNode(value)
        node.left = dfs()
        node.right = dfs()
        return node

    return dfs()


if __name__ == "__main__":
    for tree in [
        None,
        [],
        [1, [2], [3, None, [4]]],
        [1, [2], [3, [4], [5, None, [6]]]],
        [100, [50, [25], [75]], [200, None, [350]]],
        [5, [3, [2], [4]], [7, [6], [8]]],
        [
            10,
            [6, [3, [1], [4]], [8, [7], [9]]],
            [14, [12], [16]]
        ],
    ]:
        root = TreeNode.build_tree(tree)
        stream = serialize(root)
        root_des = deserialize(stream)
        print(f"{root} --> {root_des}")

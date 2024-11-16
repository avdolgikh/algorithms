class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def build(self, i, values):        
        root = TreeNode(values[i])
        
        if 2*i + 1 < len(values) and values[2*i + 1] is not None:
            root.left = self.build(2*i + 1, values)

        if 2*i + 2 < len(values) and values[2*i + 2] is not None:
            root.right = self.build(2*i + 2, values)

        return root
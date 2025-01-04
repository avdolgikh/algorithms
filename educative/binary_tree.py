class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_left(self, child):
        """Add a left child to the node."""
        self.left = child

    def add_right(self, child):
        """Add a right child to the node."""
        self.right = child

    def __repr__(self):
        """Return a concise or detailed representation based on the tree's size."""
        return str(self.to_nested_list())

    @staticmethod
    def build_tree(data):
        """Builds a binary tree from a nested list or tuple, allowing None and single nodes."""
        if not data:
            return None  # Handle empty or None input

        # Create the root node with the first value
        root = TreeNode(data[0])

        # Add the left child if data[1] exists and is not None
        if len(data) > 1 and data[1] is not None:
            root.add_left(TreeNode.build_tree(data[1]))

        # Add the right child if data[2] exists and is not None
        if len(data) > 2 and data[2] is not None:
            root.add_right(TreeNode.build_tree(data[2]))

        return root

    def to_nested_list(self):
        """Converts a binary tree back to a nested list representation."""
        result = [self.data]
        if self.left:
            result.append(self.left.to_nested_list())
        elif self.right:  # Include `None` if there's only a right child
            result.append(None)
        if self.right:
            result.append(self.right.to_nested_list())
        return result

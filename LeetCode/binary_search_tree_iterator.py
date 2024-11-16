from tree_utils import *

class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.current_node = root
        self.stack = []

    def next(self):
        """
        @return the next smallest number
        :rtype: int
        """        
        while self.current_node is not None:
            self.stack.append(self.current_node)
            self.current_node = self.current_node.left

        if len(self.stack) > 0:
            popped_node = self.stack.pop()
            next_value = popped_node.val
            self.current_node = popped_node.right

        return next_value
        

    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """
        return not ( self.current_node is None and len(self.stack) == 0 )
 
    def inorderTraversal(self):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        root = self.tree

        stack = []
        output = []
        
        while True:
            while root is not None:
                stack.append(root)
                root = root.left

            if len(stack) > 0:
                popped_node = stack.pop()
                output.append(popped_node.val)
                root = popped_node.right

            if root is None and len(stack) == 0:
                break
            
        return output





if __name__ == '__main__':
    tree_values = [7,3,15,None,None,9,20]
    root = TreeNode(0).build(0, tree_values)
    
    obj = BSTIterator(root)
    print(obj.next())
    print(obj.next())   
    print(obj.hasNext())
    print(obj.next()) 
    print(obj.hasNext())
    print(obj.next())
    print(obj.hasNext())
    print(obj.next())
    print(obj.hasNext())

    #print(obj.inorderTraversal(root))

# python3

class TreeOrders:
    def read(self):
        #self.n = 10
        self.n = int(input())
        self.key = [0 for i in range(self.n)]
        self.left = [0 for i in range(self.n)]
        self.right = [0 for i in range(self.n)]
        for i in range(self.n):
            #tree_declaration = ["4 1 2", "2 3 4", "5 -1 -1", "1 -1 -1", "3 -1 -1"]
            #tree_declaration = ["0 7 2", "10 -1 -1", "20 -1 6", "30 8 9", "40 3 -1", "50 -1 -1", "60 1 -1", "70 5 4", "80 -1 -1", "90 -1 -1"]
            [a, b, c] = map(int, input().split())
            #[a, b, c] = map(int, tree_declaration[i].split())
            self.key[i] = a
            self.left[i] = b
            self.right[i] = c

    def inOrder(self, index=0):
        stack = []
        output = []
        
        if self.n > 0:
            while True:
                while index > -1:
                    stack.append(index)
                    index = self.left[index]

                if len(stack) > 0:
                    popped_index = stack.pop()
                    output.append(self.key[popped_index])
                    index = self.right[popped_index]

                if index == -1 and len(stack) == 0:
                    break
            
        return output

    def check(self):
        lst = self.inOrder()
        return "CORRECT" if sorted(lst) == lst else "INCORRECT"
        

    
def main():
    tree = TreeOrders()
    tree.read()
    print(tree.check())
    

"""
Failed case #3/36: (Wrong answer)

Input:
0

Your output:

Your stderr:
Traceback (most recent call last):
  File "w6_is_bst.py", line 67, in <module>
    main()
  File "w6_is_bst.py", line 47, in main
    print(tree.check())
  File "w6_is_bst.py", line 39, in check
    lst = self.inOrder()
  File "w6_is_bst.py", line 26, in inOrder
    index = self.left[index]
IndexError: list index out of range

Correct output:
CORRECT
"""

if __name__ == '__main__':
    main()

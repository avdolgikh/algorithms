# python3

class BSTree:
    def read(self):
        self.n = int(input())
        self.key = [0 for i in range(self.n)]
        self.left = [0 for i in range(self.n)]
        self.right = [0 for i in range(self.n)]
        for i in range(self.n):
            [a, b, c] = map(int, input().split())
            self.key[i] = a
            self.left[i] = b
            self.right[i] = c

    def is_binary_search_with_equality(self, index=0):
        stack = []
        output = []
        
        if self.n > 0:
            while True:
                while index > -1:
                    stack.append(index)
                    index = self.left[index]
                    is_left = True

                if len(stack) > 0:
                    popped_index = stack.pop()
                    output.append(self.key[popped_index])
                    if not self.check_part(output, is_left):
                        return False
                    index = self.right[popped_index]
                    is_left = False

                if index == -1 and len(stack) == 0:
                    break
            
        return True

    def check_part(self, output, is_left):
        if (len(output) < 2):
            return True
        if (output[len(output) - 1] > output[len(output) - 2]):
            return True
        if (output[len(output) - 1] == output[len(output) - 2]):
            return is_left
        return False
        

    
def main():
    tree = BSTree()
    tree.read()
    if tree.is_binary_search_with_equality():
        print("CORRECT")
    else:
        print("INCORRECT")
    

"""
Input:
3
2 1 2
2 -1 -1
3 -1 -1
Output:
INCORRECT
"""

if __name__ == '__main__':
    main()

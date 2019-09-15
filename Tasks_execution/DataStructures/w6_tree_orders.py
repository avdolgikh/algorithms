# python3

import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion

class TreeOrders:
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

    def inOrder(self, index=0):
        stack = []
        output = []
        
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

    def preOrder(self, index=0):
        output = []
        stack = [index]
        while len(stack) > 0:
            index = stack.pop()
            output.append(self.key[index])
            if self.right[index] > -1:
                stack.append(self.right[index])
            if self.left[index] > -1:
                stack.append(self.left[index])
        return output

    def postOrder(self, index=0):
        output = []
        
        stack = []
        while True:

            while index > -1:
                stack.append(index)
                stack.append(index)
                index = self.left[index]

            if len(stack) == 0:
                break

            index = stack.pop()
    
            if len(stack) > 0 and stack[-1] == index:
                index = self.right[index]
            else:
                output.append(self.key[index])
                index = -1

        return output

def main():
    tree = TreeOrders()
    tree.read()
    print(" ".join(str(x) for x in tree.inOrder()))
    print(" ".join(str(x) for x in tree.preOrder()))
    print(" ".join(str(x) for x in tree.postOrder()))


if __name__ == '__main__':
    main()

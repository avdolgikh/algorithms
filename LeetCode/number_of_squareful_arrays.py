import math

def factorial(x):
    if x < 2:
        return 1
    result = 2
    for i in range(3, x+1):
        result *= i
    return result
    
def isSquared(x):
    rt = math.sqrt(x)
    return rt == int(rt)

def numSquarefulPerms(A):
    """
    :type A: List[int]
    :rtype: int
    """
    number_of_squared_sums = 0
    repeated_items = 0

    for i in range(len(A) - 1):
        for j in range(i+1, len(A)):
            if A[i] == A[j]:
                repeated_items += 1
            
            if isSquared(A[i] + A[j]):
                number_of_squared_sums += 1

    if number_of_squared_sums < len(A) - 1:
        return 0
    elif number_of_squared_sums == len(A) - 1:
        return int( 2 / (repeated_items + 1))
    else:
        return int( factorial(number_of_squared_sums) / factorial(number_of_squared_sums - len(A) + 1) / (repeated_items + 1) )

#https://medium.com/@nitishchandra/996-number-of-squareful-arrays-70474821a069

# http://guozet.me/leetcode/Leetcode-996-Number-of-Squareful-Arrays.html
class Solution(object):
    def numSquarefulPerms(self, A):
        """
        :type A: List[int]
        :rtype: int
        """   

        self.result = 0        
        self.cand = {}
        self.count = { a : A.count(a) for a in A }
        #print(self.count)

        # We build a graph: vertices are unique items of A, an edge ij exists if (A[i]+A[j]) is squared number.
        for x in self.count:
            for y in self.count:
                if isSquared(x + y):
                    if x not in self.cand:
                        self.cand[x] = set()
                    self.cand[x].add(y)

        for e in self.count:
            self.DFS(e, len(A) - 1)

        return self.result

    # Depth First Search. Start from some node and visit the graph. If we have covered whole array (size = 0), we have found a permutation.
    def DFS(self, x, size):
        self.count[x] -= 1

        if size == 0:
            self.result += 1

        if x in self.cand:
            for y in self.cand[x]:
                if self.count[y] > 0:
                    self.DFS(y, size - 1)
        
        self.count[x] += 1
                
               

    
                

if __name__ == '__main__':
    #print(numSquarefulPerms([1, 17, 8]))
    #print(numSquarefulPerms([2, 2, 2]))
    #print(numSquarefulPerms([2, 2]))
    #print(numSquarefulPerms([16, 9, 40, 24]))
    #print(numSquarefulPerms([1, 17, 8, 28, 19, 6, 20]))
    #print(numSquarefulPerms([2, 2, 2, 2]))
    #print(numSquarefulPerms([51,70,30]))

    s = Solution()    
    print(s.numSquarefulPerms([1, 17, 8]))
    print(s.numSquarefulPerms([2, 2, 2]))
    print(s.numSquarefulPerms([2, 2]))
    print(s.numSquarefulPerms([16, 9, 40, 24]))
    print(s.numSquarefulPerms([1, 17, 8, 28, 19, 6, 20]))
    print(s.numSquarefulPerms([2, 2, 2, 2]))
    print(s.numSquarefulPerms([51,70,30]))
def set_row_to_0(matrix, i, n):
    matrix[i] = [0] * n

def set_column_to_0(matrix, j, m):
    for k in range(m):
        matrix[k][j] = 0

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        i, j = 0, 0
        m, n = len(matrix), len(matrix[0])
        zerod_j = []
        row_is_zero = False
        
        while i < m:
            
            if matrix[i][j] == 0:
                row_is_zero = True
                zerod_j.append(j)

            j += 1
                    
            if j >= n:                
                if row_is_zero:
                    set_row_to_0(matrix, i, n)
                j = 0
                row_is_zero = False
                i += 1

        for k in zerod_j:
            set_column_to_0(matrix, k, m)
                    
            
if __name__ == '__main__':
    s = Solution()

    matrix = [[0,0,0,5],[4,3,1,4],[0,1,1,4],[1,2,1,3],[0,0,1,1]]
 
    s.setZeroes(matrix)

    print(matrix)

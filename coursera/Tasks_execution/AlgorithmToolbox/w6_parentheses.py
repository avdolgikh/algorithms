# Uses python3

import numpy as np

def apply_operation(a, b, op):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    else:
        return a * b

def min_and_max(i, j, m, M, expression):
    min_ = 10**6
    max_ = -10**6
    for k in range(i, j):
        a = apply_operation(M[i, k], M[k+1, j], expression[k*2 + 1])
        b = apply_operation(M[i, k], m[k+1, j], expression[k*2 + 1])
        c = apply_operation(m[i, k], M[k+1, j], expression[k*2 + 1])
        d = apply_operation(m[i, k], m[k+1, j], expression[k*2 + 1])

        min_ = np.min([min_, a, b, c, d])
        max_ = np.max([max_, a, b, c, d])

    return min_, max_


def parentheses(expression):
    n = (len(expression) - 1) // 2 + 1
    
    m = np.zeros((n, n), dtype=int)
    M = np.zeros((n, n), dtype=int)


    for i in range(n):
        m[i, i] = expression[i*2]
        M[i, i] = expression[i*2]

    for s in range(n):
        for i in range(n-s-1):
            j = i + s + 1
            m[i, j], M[i, j] = min_and_max(i, j, m, M, expression)

    return M[0, n-1]
        
    

if __name__ == '__main__':
    expression = input()

    #expression = "5-8+7*4-8+9"
    #expression = "1+5"

    print(parentheses(expression))

   


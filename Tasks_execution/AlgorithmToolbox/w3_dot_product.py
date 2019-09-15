# Uses python3

def swap(a, i, j):
    if i != j:
        temp = a[i]
        a[i] = a[j]
        a[j] = temp

def get_max_dot_product(n, a, b):
    sum = 0
    for i in range(n):
        a_max = -10 ** 5
        b_max = -10 ** 5
        a_max_index = i
        b_max_index = i
        for j in range(i, n):
            if a[j] > a_max:
                a_max = a[j]
                a_max_index = j
            if b[j] > b_max:
                b_max = b[j]
                b_max_index = j
        swap(a, i, a_max_index)
        swap(b, i, b_max_index)
        sum += a_max * b_max
    return sum
        

if __name__ == '__main__':
    n = int(input())
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]

    #n = 10 ** 3
    #import numpy as np
    #a = np.random.randint(-10 ** 5, 10 ** 5, n).tolist()
    #b = np.random.randint(-10 ** 5, 10 ** 5, n).tolist()
    
    print(get_max_dot_product(n, a, b))

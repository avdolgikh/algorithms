# python3

def left_child(i):
    return 2 * i + 1

def right_child(i):
    return 2 * i + 2

def min_heap_sift_down(a, i, swaps):
    n = len(a)
    min_index = i
    l = left_child(i)

    if l < n and a[l] < a[min_index]:
        min_index = l

    r = right_child(i)
    
    if r < n and a[r] < a[min_index]:
        min_index = r

    if i != min_index:
        swaps.append((i, min_index))
        #print(swaps)
        a[i], a[min_index] = a[min_index], a[i]
        min_heap_sift_down(a, min_index, swaps)

    return swaps

def build_heap(a):
    n = len(a)
    swaps = []

    for i in reversed(range(n // 2)):
        swaps = min_heap_sift_down(a, i, swaps)

    return swaps

if __name__ == '__main__':
    n = int(input())
    a = [int(x) for x in input().split()]
    #assert n == len(a)
    
    #n = 5
    #a = [5, 4, 3, 2, 1]
    #a = [1, 2, 3, 4, 5]

    #import numpy as np
    #n = 1000000
    #a = np.random.randint(0, 10**9, n*10, dtype=int)
    #a = np.unique(a).tolist()[:n]

    swaps = build_heap(a)

    print(len(swaps))
    for swap in swaps:
        print(swap[0], swap[1])

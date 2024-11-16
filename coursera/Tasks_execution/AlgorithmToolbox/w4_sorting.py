# Uses python3        

def swap(a, i, j):
    if i != j:
        #temp = a[i]
        #a[i] = a[j]
        #a[j] = temp
        a[i], a[j] = a[j], a[i]

def get_random_index(a, left_index, right_index):
    import numpy as np
    return np.random.randint(left_index, right_index + 1, 1)[0]


def quick_sort_2(a, left_index, right_index):
    if left_index >= right_index:
        return
    m = partition2(a, left_index, right_index)
    quick_sort_2(a, left_index, m - 1);
    quick_sort_2(a, m + 1, right_index);

def quick_sort_it_2(a, left_index, right_index):
    while left_index < right_index:
        m = partition2(a, left_index, right_index)
        if (m - 1) < (right_index - m):
            quick_sort_it_2(a, left_index, m - 1)
            left_index = m + 1
        else:
            quick_sort_it_2(a, m + 1, right_index)
            right_index = m - 1

def partition2(a, left_index, right_index):
    k = get_random_index(a, left_index, right_index)
    swap(a, left_index, k)

    x = a[left_index]
    j = left_index
    
    for i in range(left_index + 1, right_index + 1):
        if a[i] <= x:
            j += 1
            swap(a, j, i)
    swap(a, left_index, j)
    return j



def quick_sort_3(a, left_index, right_index):
    if left_index >= right_index:
        return
    m1, m2 = partition3(a, left_index, right_index)
    quick_sort_3(a, left_index, m1 - 1);
    quick_sort_3(a, m2 + 1, right_index);

def quick_sort_it_3(a, left_index, right_index):
    while left_index < right_index:
        m1, m2 = partition3(a, left_index, right_index)
        if (m1 - 1) < (right_index - m2):
            quick_sort_it_3(a, left_index, m1 - 1)
            left_index = m2 + 1
        else:
            quick_sort_it_3(a, m2 + 1, right_index)
            right_index = m1 - 1

def partition3(a, left_index, right_index):
    m2 = partition2(a, left_index, right_index)
    m1 = m2
    i = m2 - 1
    while left_index <= i:
        if a[i] == a[m2]:
           m1 -= 1
           swap(a, i, m1)
        i -= 1
    return m1, m2



    

if __name__ == '__main__':
    n = int(input())
    a = [int(x) for x in input().split()[:n]]

    #n = 10 ** 5
    #import numpy as np
    #a = np.random.randint(1, 10 ** 4, n).tolist()

    #n = 40
    #a = [1, 3, 2, 3, 9, 2, 2, 9, 3, 1, 1, 3, 2, 3, 9, 2, 2, 9, 3, 1, 1, 3, 2, 3, 9, 2, 2, 9, 3, 1, 1, 3, 2, 3, 9, 2, 2, 9, 3, 1]

    quick_sort_3(a, 0, n-1)

    print(" ".join([str(item) for item in a]))

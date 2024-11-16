# Uses python3

def swap(a, i, j):
    temp = a[i]
    a[i] = a[j]
    a[j] = temp

def max_pairwise_product(a):
    index1 = 0
    for i in range(1, len(a)):
        if a[i] > a[index1]:
            index1 = i

    swap(a, index1, len(a) - 1)
    index1 = len(a) - 1
    
    index2 = 0
    for i in range(1, len(a) - 1):
        if i != index1 and a[i] > a[index2]:
            index2 = i

    return a[index1] * a[index2]


if __name__ == '__main__':
    n = int(input())
    a = [int(x) for x in input().split()]
        
    product = max_pairwise_product(a)

    print(product)

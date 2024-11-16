# Uses python3        

def binary_search(a, low, high, key):
    if high < low:
        return -1
    mid = int(low + (high - low) / 2)
    if key == a[mid]:
        return mid
    elif key < a[mid]:
        return binary_search(a, low, mid - 1, key)
    else:
        return binary_search(a, mid + 1, high, key)

def binary_search_it(a, low, high, key):
    while low <= high:
        mid = int(low + (high - low) / 2)
        if key == a[mid]:
            return mid
        elif key < a[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1


if __name__ == '__main__':
    n_a = [int(x) for x in input().split()]
    k_b = [int(x) for x in input().split()]

    n = n_a[0]
    a = n_a[1:]
    k = k_b[0]
    b = k_b[1:]

    #n = 5
    #a = [1, 5, 8, 12, 13]
    #k = 5
    #b = [8, 1, 23, 1, 11]
    
    result = []
    for i in range(k):
        result.append(binary_search_it(a, 0, n-1, b[i]))
    
    print(" ".join([str(item) for item in result]))

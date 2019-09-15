# Uses python3        


if __name__ == '__main__':
    n = int(input())
    a = [int(x) for x in input().split()[:n]]

    #n = 10 ** 5
    #import numpy as np
    #a = np.random.randint(0, 10 ** 9, n).tolist()

    #n = 4
    #a = [1, 2, 3, 1]
    # Output: 1 if the sequence contains an element that appears strictly more than n/2 times, and 0 otherwise.

    counts = {}
    for i in range(n):
        if a[i] in counts:
            counts[a[i]] += 1
        else:
            counts[a[i]] = 1

    result = any([count for count in list(counts.values()) if count > int(n / 2)])

    print(1 if result else 0)

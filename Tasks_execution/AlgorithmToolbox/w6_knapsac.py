# Uses python3

def knapsac_without_repetiotion(W, item_weights, item_values):
    n = len(item_weights)
    import numpy as np
    value = np.zeros((W+1, n+1), dtype=int)
    for i in range(1, n+1):
        for w in range(1, W+1):
            value[w, i] = value[w, i-1]
            if item_weights[i-1] <= w:
                val = value[w-item_weights[i-1], i-1] + item_values[i-1]
                if value[w, i] < val:
                    value[w, i] = val
    return value[W, n]

if __name__ == '__main__':
    W, n = map(int, input().split())
    w = [int(x) for x in input().split()]

    #W = 10 ** 4
    #n = 300
    #import numpy as np
    #w = np.random.randint(0, 10 ** 5, n).tolist()

    #W = 10
    #n = 3
    #w = [1, 4, 8]

    print(knapsac_without_repetiotion(W, w, w))


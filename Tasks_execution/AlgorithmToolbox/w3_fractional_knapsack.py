# Uses python3

def swap(a, i, j):
    if i != j:
        temp = a[i]
        a[i] = a[j]
        a[j] = temp

def get_max_price_index(v, w, index):
    max_price = 0
    max_price_index = 0
    for i in range(index, len(v)):
        price = v[i]/w[i]
        if price > max_price:
            max_price = price
            max_price_index = i
    return max_price_index

def get_max_value(n, W, v, w):
    index = 0
    V = 0

    while W > 0 and index < n:
            
        max_price_index = get_max_price_index(v, w, index)
        swap(v, index, max_price_index)
        swap(w, index, max_price_index)
        if W < w[index]:
            weight = W
        else:
            weight = w[index]            
        W -= weight
        V +=  v[index]/w[index] * weight
        index += 1
    
    return V

if __name__ == '__main__':
    v = []
    w = []    
    
    n, W = map(int, input().split())
    
    for i in range(n):
        v_i, w_i = map(int, input().split())
        v.append(v_i)
        w.append(w_i)

    #n = 1
    #W = 10
    #v = [500]
    #w = [30]
    
    print(get_max_value(n, W, v, w))

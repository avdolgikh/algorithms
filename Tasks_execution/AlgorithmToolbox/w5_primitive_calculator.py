# Uses python3        

def optimal_sequence(n):
    sequence = []
    while n >= 1:
        sequence.append(n)
        if n % 3 == 0:
            n = n // 3
        elif n % 2 == 0:
            n = n // 2
        else:
            n = n - 1
    return list(reversed(sequence))

def optimal_sequence2(n):        
    n_operations = [None, 0]

    sequences = {}
    
    for j in range(2, n+1): 
        op1 = j
        op2 = j

        if j % 3 == 0:
            op1 = n_operations[j // 3] + 1

        if j % 2 == 0:
            op2 = n_operations[j // 2] + 1
            
        n_operations.append(min([op1, op2, n_operations[j - 1] + 1]))
        
    return n_operations[n]

def optimal_sequence3(n):        
    n_operations = [None, 0]
    sequences = { 1: [1]}
    
    for j in range(2, n+1):
        n_ops = n_operations[j - 1] + 1
        sequences[j] = sequences[j - 1] + [j]

        if j % 3 == 0 and n_operations[j // 3] + 1 < n_ops:
            n_ops = n_operations[j // 3] + 1
            sequences[j] = sequences[j // 3] + [j]

        if j % 2 == 0 and n_operations[j // 2] + 1 < n_ops:
            n_ops = n_operations[j // 2] + 1
            sequences[j] = sequences[j // 2] + [j]
            
        n_operations.append(n_ops)
        
    return n_operations[n], sequences[n]


if __name__ == '__main__':
    n = int(input())

    #n = 96234 # 10 ** 6
    #import numpy as np
    #n = np.random.randint(1, 10 ** 6, 1)[0]

    #sequence = optimal_sequence(n)
    #print(len(sequence) - 1)
    #print(" ".join([str(item) for item in sequence]))

    _, sequence = optimal_sequence3(n)
    print(len(sequence) - 1)
    print(" ".join([str(item) for item in sequence]))

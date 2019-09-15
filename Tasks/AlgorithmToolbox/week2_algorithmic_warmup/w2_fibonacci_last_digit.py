# Uses python3

if __name__ == '__main__':
    n = int(input())
    fibonacci = []

    fibonacci.append(0)
    fibonacci.append(1)

    for i in range(2, n+1):
        fibonacci.append((fibonacci[i - 1] + fibonacci[i - 2]) % 10)
    
    print(fibonacci[n])

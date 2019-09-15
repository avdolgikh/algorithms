# Uses python3

if __name__ == '__main__':
    n = int(input())
    fibonacci_mod_10 = []

    fibonacci_mod_10.append(0)
    fibonacci_mod_10.append(1)

    for i in range(2, n+1):
        fibonacci_mod_10.append((fibonacci_mod_10[i - 1] + fibonacci_mod_10[i - 2]) % 10)
    
    print(fibonacci_mod_10[n])

# Uses python3

def get_fibonacci_mod_m(n, m):
    fibonacci_mod_m = []
    fibonacci_mod_m.append(0)
    fibonacci_mod_m.append(1)

    i = 2
    while True:
        fibonacci_mod_m.append((fibonacci_mod_m[i - 1] + fibonacci_mod_m[i - 2]) % m)
        if fibonacci_mod_m[i] == 1 and fibonacci_mod_m[i - 1] == 0:
            i = i - 1
            break
        i += 1
    
    n = n % i
    
    return fibonacci_mod_m[n]

if __name__ == '__main__':
    n = int(input())

    sum_last_digit = get_fibonacci_mod_m(n + 2, 10)
    
    if sum_last_digit == 0:
        sum_last_digit = 9
    else:
        sum_last_digit -= 1

    print(sum_last_digit)

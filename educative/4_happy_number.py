# https://www.educative.io/module/page/8q5JgjuzjGkprAwQG/10370001/4896118288416768/6063132465954816


def sum_of_squared_digits(n):
    sum = 0
    for d in str(n):
        sum += int(d)**2
    return sum


def is_happy_number(n):
    slow = n
    fast = sum_of_squared_digits(n)

    # op_count = 0
    while fast != 1 and fast != slow and slow != 1:
        slow = sum_of_squared_digits(slow)
        fast = sum_of_squared_digits(sum_of_squared_digits(fast))
        # op_count += 1
    
    # print(f"{op_count} ops")

    return (fast == 1 or slow == 1)


if __name__ == "__main__":
    for n in [2147483646, 1, 19, 8, 7, 0, 10, 23, 2, 28, 3]:
        print(n, is_happy_number(n))

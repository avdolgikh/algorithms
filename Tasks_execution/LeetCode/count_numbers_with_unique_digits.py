def countNumbersWithUniqueDigits(n):
    """
    :type n: int
    :rtype: int
    """

    if n < 2:
        return 10 ** n
    
    with_repeatition = set()
        
    def find_repeated_digits(number):

        if number in with_repeatition:
            return

        if number[0] != '0':
            with_repeatition.add(number)

        if len(number) >= n:
            return

        for i in range(10):
            for k in range(len(number) + 1):
                if i == 0 and k == 0:
                    continue
                find_repeated_digits(number[:k] + str(i) + number[k:])
        
    find_repeated_digits("00")
    for i in range(9):
        find_repeated_digits(str( (i+1) * 10 + (i+1) ))

    #print(len(with_repeatition))
    
    return 10 ** n - len(with_repeatition)

# http://shirleyisnotageek.blogspot.com/2016/06/count-numbers-with-unique-digits.html
def countNumbersWithUniqueDigits2(n):
    if n == 0:
        return 1

    rst = 10
    count = 9

    for i in range(2, n+1):
        count *= (10 - i + 1)
        rst += count

    return rst

if __name__ == '__main__':
    print(countNumbersWithUniqueDigits2(12))
    #print(countNumbersWithUniqueDigits(6))
    


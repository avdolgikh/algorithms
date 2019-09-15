def numRollsToTarget(d, f, target):
    """
    :type d: int : dice number
    :type f: int : faces number
    :type target: int : sum target
    :rtype: int : ways number
    """

    mod = 10 ** 9 + 7
    
    def count_ways(d, f, target):

        table = [ [0]*(target+1) for i in range(d+1) ]

        for t in range(1, min(f+1, target+1)):
            table[1][t] = 1

        for i in range(2, d+1):
            for t in range(1, target+1):
                if f*d <= target:
                    table[i][t] = int(f*d == target)
                elif d >= target:
                    table[i][t] = int(d == target)
                else:
                    for k in range(1, min(f+1, t)):
                        table[i][t] += table[i-1][t-k]
                table[i][t] = table[i][t] % mod

        #print(table)
        return table[-1][-1]
    
    return count_ways(d, f, target)



if __name__ == '__main__':
    print(numRollsToTarget(30, 30, 500))


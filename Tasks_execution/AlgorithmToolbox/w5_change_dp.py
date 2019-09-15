# Uses python3        

def dp_change(money, coins):
    min_num_coins = { 0: 0 }
    for m in range(1, money + 1):
        min_num_coins[m] = money
        for i in range(len(coins)):
            if m >= coins[i]:
                n_coins = min_num_coins[m - coins[i]] + 1
                if n_coins < min_num_coins[m]:
                    min_num_coins[m] = n_coins
    return min_num_coins[money]


if __name__ == '__main__':
    money = int(input())

    coins = [1, 3, 4]

    #money = 10 ** 3
    #import numpy as np
    #money = np.random.randint(1, 10 ** 3, 1)[0]

    print(dp_change(money, coins))

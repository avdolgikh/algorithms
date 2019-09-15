# Uses python3


if __name__ == '__main__':
    m = int(input())

    coins = [10, 5, 1]

    for coins_index in range(len(coins)):
        if coins[coins_index] <= m:
            break

    n_coins = 0
    money = m
    
    while money > 0 and coins_index < len(coins):
        n_coins += int(money / coins[coins_index])
        money = money % coins[coins_index]
        coins_index += 1

    print(n_coins)

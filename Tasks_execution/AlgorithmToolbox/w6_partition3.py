# Uses python3

import numpy as np

def backtrace_optimal_solution(initial_price, item_prices, price_map):   
    n_items = len(item_prices)
    optimal_solution = np.zeros(n_items, dtype=int)
    price = initial_price
    item_index = n_items
    while item_index > 0:
        if price != price_map[price, item_index-1]:
            optimal_solution[item_index - 1] = 1
            price -= item_prices[item_index-1]
        item_index -= 1
    return optimal_solution

def items_of_total_price(total_price, item_prices):
    n_items = len(item_prices)
    
    price_map = np.zeros((total_price+1, n_items+1), dtype=int)

    for item_index in range(1, n_items+1):
        for price in range(1, total_price+1):
            price_map[price, item_index] = price_map[price, item_index-1]
                
            if item_prices[item_index-1] <= price:
                price_candidate = price_map[price - item_prices[item_index-1], item_index-1] + item_prices[item_index-1]
                if price_map[price, item_index] < price_candidate:
                    price_map[price, item_index] = price_candidate
    
    return price_map[total_price, n_items], backtrace_optimal_solution(price_map[total_price, n_items], item_prices, price_map)


def partitioning_souvenirs(n, item_prices):
    item_prices = np.array(item_prices)
    total_price = item_prices.sum()

    if n < 3:
        return 0
    elif total_price % 3 != 0:
        return 0
    else:
        part_total = total_price // 3
        
        potential_1, items_mask_1 = items_of_total_price(part_total, item_prices)
    
        if potential_1 < part_total:
            return 0
        else:
            item_prices_2 = item_prices[ np.invert(items_mask_1.astype(bool)) ]
            potential_2, _ = items_of_total_price(part_total, item_prices_2)

            if potential_2 < part_total:
                return 0
            else:
                return 1

def partitioning_souvenirs_shift(n, item_prices):
    for i in range(n):
        if partitioning_souvenirs(n, item_prices) == 1:
            return 1
        else:
            item_prices = np.roll(item_prices, 1)
    return 0

def test_positive():
    result = 1

    while result == 1:
        m = np.random.randint(1, 6, 1)[0]
        n = m * 3
        m_p = np.random.randint(1, 31, m)
        item_prices = np.array([m_p, m_p, m_p]).reshape(-1)
        np.random.shuffle(item_prices)
        result = partitioning_souvenirs_shift(n, item_prices)
    print(n)
    print(item_prices)


if __name__ == '__main__':
    n = int(input())
    item_prices = [int(x) for x in input().split()[:n]]

    #test_positive()

    #n = 12    
    #item_prices = [27, 24, 24, 19, 24, 29, 29, 19, 29, 27, 19, 27]

    print(partitioning_souvenirs_shift(n, item_prices))


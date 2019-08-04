from test_framework import generic_test


def solve_from_start(prices):
    lowest = prices[0]
    profits = [0]
    best_profit = 0

    for price in prices:
        lowest = min(lowest, price)
        best_profit = max(best_profit, price - lowest)
        profits.append(best_profit)

    return profits


def solve_from_end(prices):
    highest = prices[-1]
    profits = [0]
    best_profit = 0

    for price in prices[::-1]:
        highest = max(highest, price)
        best_profit = max(best_profit, highest - price)
        profits.append(best_profit)

    return profits


def buy_and_sell_stock_twice(prices):
    answers1 = solve_from_start(prices)
    answers2 = solve_from_end(prices)

    best_profit = 0
    for i in range(len(prices) + 1):
        best_profit = max(best_profit, answers1[i] + answers2[len(prices) - i])

    return best_profit


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("buy_and_sell_stock_twice.py",
                                       "buy_and_sell_stock_twice.tsv",
                                       buy_and_sell_stock_twice))

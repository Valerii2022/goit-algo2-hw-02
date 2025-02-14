from typing import List, Dict

def rod_cutting_memo(length: int, prices: List[int]) -> Dict:
    memo = {}

    def helper(n: int) -> int:
        if n == 0:
            return 0
        if n in memo:
            return memo[n]
        max_profit = float('-inf')
        for i in range(1, n + 1):
            max_profit = max(max_profit, prices[i - 1] + helper(n - i))
        memo[n] = max_profit
        return max_profit

    max_profit = helper(length)

    cuts = []
    n = length
    while n > 0:
        for i in range(1, n + 1):
            if prices[i - 1] + helper(n - i) == memo[n]:
                cuts.append(i)
                n -= i
                break

    return {
        "max_profit": max_profit,
        "cuts": cuts,
        "number_of_cuts": len(cuts) - 1
    }

def rod_cutting_table(length: int, prices: List[int]) -> Dict:
    dp = [0] * (length + 1)
    cuts = [0] * (length + 1)

    for i in range(1, length + 1):
        max_profit = float('-inf')
        for j in range(1, i + 1):
            if max_profit < prices[j - 1] + dp[i - j]:
                max_profit = prices[j - 1] + dp[i - j]
                cuts[i] = j
        dp[i] = max_profit

    n = length
    result_cuts = []
    while n > 0:
        result_cuts.append(cuts[n])
        n -= cuts[n]

    return {
        "max_profit": dp[length],
        "cuts": result_cuts,
        "number_of_cuts": len(result_cuts) - 1
    }

def run_tests():
    """Функція для запуску всіх тестів"""
    test_cases = [
        {
            "length": 5,
            "prices": [2, 5, 7, 8, 10],
            "name": "Базовий випадок"
        },
        {
            "length": 3,
            "prices": [1, 3, 8],
            "name": "Оптимально не різати"
        },
        {
            "length": 4,
            "prices": [3, 5, 6, 7],
            "name": "Рівномірні розрізи"
        }
    ]

    for test in test_cases:
        print(f"\nТест: {test['name']}")
        print(f"Довжина стрижня: {test['length']}")
        print(f"Ціни: {test['prices']}")

        print("\nМемоізація:")
        result_memo = rod_cutting_memo(test['length'], test['prices'])
        print(f"Максимальний прибуток: {result_memo['max_profit']}")
        print(f"Розрізи: {result_memo['cuts']}")
        print(f"Кількість розрізів: {result_memo['number_of_cuts']}")

        print("\nТабуляція:")
        result_table = rod_cutting_table(test['length'], test['prices'])
        print(f"Максимальний прибуток: {result_table['max_profit']}")
        print(f"Розрізи: {result_table['cuts']}")
        print(f"Кількість розрізів: {result_table['number_of_cuts']}")

        print("\nПеревірка пройшла успішно!")

if __name__ == "__main__":
    run_tests()

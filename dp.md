# dynamic programming concepts
1. Tabulization
2. Memoization
3. Bottom-up
4. Top-down

#### dp fibonacci
"""python
def fib(n):
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]
""""

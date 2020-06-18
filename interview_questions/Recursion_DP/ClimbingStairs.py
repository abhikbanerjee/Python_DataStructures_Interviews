

# Climbing stairs in how many distinct ways using DP (cna take only 1 or 2 steps) - LC 70
def climb_stairs(n: int) -> int:
        if n < 0:
            return 0
        dp = [0 for _ in range(n+1)]
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]

print(climb_stairs(2))
print(" ")
print(climb_stairs(5))
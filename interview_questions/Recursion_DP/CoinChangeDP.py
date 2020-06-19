from typing import List
import time

# Coin Change problem - make an amount with the least number of coins - LC 322
def smallest_number_coins(coins: List[int], amount: int) -> int:
        if len(coins) == 0:
            return 0
        dp_amount = [(amount+1) for _ in range(amount+1)]
        dp_amount[0] = 0
        sorted(coins)
        for i in range(1, len(dp_amount)):
            for j in coins:
                if j <= i:
                    dp_amount[i] = min(dp_amount[i],  1+dp_amount[i-j])
        ans = dp_amount[-1]
        if ans >= amount+1:
            return -1
        else:
            return ans


# given denomination of coins and the amount to make
coins = [5,1,2] # this can be non sorted
amount_to_make1 = 11
amount_to_make2 = 23
start = time.time()
print("Smallest Number of coins needed - ", smallest_number_coins(coins, amount_to_make1))
end = time.time()
print("Time taken - ", (end-start)*1000, " milliseconds")


start = time.time()
print("Smallest Number of coins needed - ", smallest_number_coins(coins, amount_to_make2))
end = time.time()
print("Time taken - ", (end-start)*1000, " milliseconds")
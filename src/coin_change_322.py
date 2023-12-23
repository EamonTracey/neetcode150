# You are given an integer array coins representing
# coins of different denominations and an integer
# amount representing a total amount of money.
#
# Return the fewest number of coins that you need to
# make up that amount. If that amount of money cannot
# be made up by any combination of the coins, return -1.
#
# You may assume that you have an infinite number of
# each kind of coin.

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {0: 0}

        def coin_helper(amount):
            if amount < 0:
                return -1
            
            if amount not in memo:
                decisions = (coin_helper(amount - coin) for coin in coins)
                all_fail = True
                mindec = float("inf")
                for dec in decisions:
                    if dec != -1:
                        all_fail = False
                        mindec = min(mindec, dec)
                memo[amount] = -1 if all_fail else 1 + mindec
            return memo[amount]
        
        return coin_helper(amount)

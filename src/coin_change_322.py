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
                return float("inf")

            if amount not in memo:
                decisions = (coin_helper(amount - coin) for coin in coins)
                mindec = float("inf")
                for dec in decisions:
                    mindec = min(mindec, dec)
                memo[amount] = 1 + mindec
            return memo[amount]

        sol = coin_helper(amount)
        return -1 if sol == float("inf") else sol


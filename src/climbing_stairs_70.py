# You are climbing a staircase. It takes n steps
# to reach the top.
#
# Each time you can either climb 1 or 2 steps. In
# how many distinct ways can you climb to the top?

class Solution:
    memo = {1: 1, 2: 2}

    def climbStairs(self, n: int) -> int:
        if n not in Solution.memo:
            Solution.memo[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        return Solution.memo[n]
 

class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [0] * 45
        memo[0] = 1
        memo[1] = 2

        for stairs in range(2, n):
            memo[stairs] = memo[stairs - 1] + memo[stairs - 2]
        
        return memo[n - 1]


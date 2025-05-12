class Solution:
    def __init__(self):
        self.memo = {}
    def climbStairs(self, n: int) -> int:
        def steps(n):
            if n < 0:
                return 0
            if n == 0:
                return 1
            
            one_hop = steps(n-1) if n-1 not in self.memo else self.memo[n-1]
            self.memo[n-1] = one_hop
            two_hop = steps(n-2) if n-2 not in self.memo else self.memo[n-2]
            self.memo[n-2] = two_hop
            return one_hop + two_hop
        return steps(n)
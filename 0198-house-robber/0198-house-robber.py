class Solution:
    def __init__(self):
        self.memo = {}

    def rob(self, nums: List[int]) -> int:
        
        def robbed(n):
            if n >= len(nums):
                return 0
            if not n+2 in self.memo:
                self.memo[n+2] = robbed(n+2)
            if not n+1 in self.memo:
                self.memo[n+1] = robbed(n+1)
            return max(nums[n] + self.memo[n+2], self.memo[n+1])
            
        return robbed(0)

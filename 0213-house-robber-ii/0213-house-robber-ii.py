class Solution:
    def __init__(self):
        self.memo = {}

    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
            
        def robbed(n, has_first):
            if n >= len(nums) or (has_first and n == len(nums) - 1):
                return 0
            if (n, has_first) in self.memo:
                return self.memo[(n, has_first)]

            take = nums[n] + robbed(n + 2, has_first)
            skip = robbed(n + 1, has_first)

            self.memo[(n, has_first)] = max(take, skip)  # Store result in memo
            return self.memo[(n, has_first)]
        
        return max(robbed(0, True), robbed(1, False))

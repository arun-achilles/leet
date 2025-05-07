class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        result = 0
        if len(nums) == 0:
            return 0
        prev = nums[0]
        longest = 1
        for idx in range(1, len(nums)):
            if nums[idx] in [prev, prev + 1]:
                longest += 1 if nums[idx] != prev else 0
            else:
                longest = 1
            prev = nums[idx]
            result = max(result, longest)
        return max(result, longest)


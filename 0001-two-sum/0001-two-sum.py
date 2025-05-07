
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for idx, el in enumerate(nums):
            remaining = target - el
            if remaining in nums[idx+1:]:
                val = nums[idx+1:].index(remaining)
                return [idx, idx + 1 + val]
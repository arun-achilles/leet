class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        prod = 1
        has_zero = False
        for idx in range(len(nums)):
            if has_zero and nums[idx] == 0:
                return [0] * len(nums)
            if nums[idx] == 0:
                has_zero = True
                continue
            prod = prod * nums[idx]
        
        for idx in range(len(nums)):
            if has_zero:
                nums[idx] = 0 if nums[idx] != 0 else prod
            else:
                nums[idx] = int(prod / nums[idx])
        
        return nums

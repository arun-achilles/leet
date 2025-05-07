class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        for idx in range(len(nums)-2):
            if idx > 0 and nums[idx] == nums[idx - 1]:
                continue
            first = idx + 1
            last = len(nums) - 1
            while first < last:
                pair = [nums[idx], nums[first], nums[last]]
                total = nums[idx] + nums[first] + nums[last]
                if total == 0:
                    result.append(pair)
                    while first < last and nums[first] == nums[first + 1]:
                        first += 1
                    while first < last and nums[last] == nums[last - 1]:
                        last -= 1
                    first += 1
                    last -= 1
                elif total > 0:
                    last -= 1
                else:
                    first += 1

        return result
            

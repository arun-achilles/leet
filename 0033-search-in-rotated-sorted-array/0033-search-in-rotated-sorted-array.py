class Solution:
    def search(self, nums: List[int], target: int) -> int:
        pos_map = {}
        for idx, el in enumerate(nums):
            pos_map[el] = idx
        
        nums.sort()
        for el in nums:
            if el > target:
                break
            if el == target:
                return pos_map[el]
        return -1

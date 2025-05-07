class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        unique = {}
        for el in nums:
            if el in unique:
                return True
            unique[el] = 1
        return False
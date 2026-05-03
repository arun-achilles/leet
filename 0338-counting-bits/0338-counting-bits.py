class Solution:
    def countBits(self, n: int) -> List[int]:
        # count_ones(i) = count_ones(all bits except last) + value_of_last_bit  
        res = [0] * (n + 1)
        for itr in range(1, n+1):
            res[itr] = res[itr >> 1] + (itr & 1)
        return res
        
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        counter = Counter(nums)
        counts = list(counter.values())
        counts.sort()
        counts = counts[::-1][:k]
        for el, count in counter.items():
            if count in counts:
                result.append(el)
        return result
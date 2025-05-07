class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        _map = {}
        for el in strs:
            val = ''.join(sorted(el))
            if val in _map:
                _map[val].append(el)    
            else:
                _map[val] = [el]
        return list(_map.values())


            

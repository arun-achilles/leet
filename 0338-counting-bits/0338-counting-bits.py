class Solution:
    def countBits(self, n: int) -> List[int]:
        def next_binary(binary):
            bits = list(binary)
            i = len(bits) - 1

            while i >= 0:
                if bits[i] == '0':
                    bits[i] = '1'
                    return ''.join(bits)
                else:
                    bits[i] = '0'
                    i -= 1

            return '1' + ''.join(bits)

        itr = 0
        curr_binary = '0'
        res = [0]
        while itr != n:
            curr_binary = next_binary(curr_binary)
            res.append(curr_binary.count('1'))
            itr += 1
        print(res)
        return res

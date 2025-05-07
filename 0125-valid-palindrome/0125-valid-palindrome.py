class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        cleaned_data = "".join([el if (ord(el) >= 97 and ord(el) <= 122) or (ord(el) >= 48 and ord(el) <= 57) else "" for el in s])
        return cleaned_data == cleaned_data[::-1]
        
    

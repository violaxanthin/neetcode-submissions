class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered_s = ''
        for c in s:
            if c.isalnum():
                filtered_s += c.lower()
        return filtered_s == filtered_s[::-1]
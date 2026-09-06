class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered = ""
        for char in s:
            if char.isalnum():
                filtered += char.lower()

        return filtered[::-1] == filtered
        

        
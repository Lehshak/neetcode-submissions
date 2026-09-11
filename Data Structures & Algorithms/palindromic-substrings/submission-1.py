class Solution:
    def countSubstrings(self, s: str) -> int:
        pals = 0

        for i in range(len(s)):

            # odd pals
            l, r = i-1, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                pals += 1
                l-=1
                r+=1

            # even pals
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                pals += 1
                l-=1
                r+=1
                
            pals += 1
        return pals
            






        
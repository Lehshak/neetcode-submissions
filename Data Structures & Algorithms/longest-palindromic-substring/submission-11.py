class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest_streak = 1
        res = s[0]

        for i in range(len(s)):

            mid = i
            l, r = mid, mid
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r-l+1) >= longest_streak:
                        longest_streak = r-l+1
                        res = s[l:r+1]
                l-=1
                r+=1


            # even length palindrome case
            l,r = mid, mid+1
            streak = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r-l+1) >= longest_streak:
                        longest_streak = r-l+1
                        res = s[l:r+1]
                streak += 2
                l-=1
                r+=1
                
        return res









            


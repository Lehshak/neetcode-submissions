class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        longest_unique = 0
        sp = 0

        # Let the for loop naturally advance the end pointer step-by-step
        for ep in range(len(s)):
            while s[ep] in seen:
                seen.remove(s[sp])
                sp += 1

            # shrink the window from the left
            seen.add(s[ep])
            longest_unique = max(longest_unique, ep - sp + 1)

        return longest_unique

                




                


        

        



            
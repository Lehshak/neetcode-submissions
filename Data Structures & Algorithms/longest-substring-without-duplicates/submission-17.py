class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        l = 0
        
        longest = 0

        for r in range(len(s)):
            if s[r] not in chars:
                chars.add(s[r])
            else:
                #s[r] in chars keep removing from l until its not
                while l < r and s[r] in chars:
                    if s[l] in chars:
                        chars.remove(s[l])
                    l+=1
                chars.add(s[r])

            longest = max(longest, len(chars))

        return longest




        




                


        

        



            
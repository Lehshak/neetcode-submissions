class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_unique = 0

        sp = 0
        ep = 1

        if len(s) == 1:
            return 1

        while ep < len(s):
            seen = set()
            seen.add(s[sp])

            while ep < len(s):
                if s[ep] in seen:
                    longest_unique = max(longest_unique, ep - sp)
                    break
                else:
                    seen.add(s[ep])
                    longest_unique = max(longest_unique, ep - sp + 1 )
                    ep += 1

            # keep removing chars until the duplicate is gone
            dupe = s[sp]
            while sp < len(s) and dupe in seen:
                past_char = s[sp]
                seen.remove(past_char)
                sp += 1

            ep = sp + 1


        return longest_unique

                




                


        

        



            
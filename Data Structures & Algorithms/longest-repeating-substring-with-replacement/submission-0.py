class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # 
        # algorithm keep going until you run out of swaps then reclaim them!
        # reclaim swaps from the left

        longest = 0
        sp = 0

        freq_chars = dict()

        for ep in range(len(s)):
            freq_chars[s[ep]] = freq_chars.get(s[ep], 0) + 1

            while ep - sp + 1 - max(list(freq_chars.values())) > k:
                # regain swaps from the left
                freq_chars[s[sp]] = freq_chars.get(s[sp], 0) - 1
                sp += 1
            
            longest = max(longest, ep - sp + 1)

        return longest
            

            



            





        
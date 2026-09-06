class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # notice the number of unique chars is always k for a valid substr
        freq = dict()

        l = 0
        longest = 0

        for r in range(len(s)):
            freq[s[r]] = freq.get(s[r], 0) + 1

            # the freq of non highest_freq values, must be <= k

            while l<r and r - l + 1 - max(list(freq.values())) > k:
                # we have to remove some swaps 
                freq[s[l]] = freq.get(s[l], 0) - 1
                l += 1

            longest = max(longest, r-l+1)

        return longest







            



            





        
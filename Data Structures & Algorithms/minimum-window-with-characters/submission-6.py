class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
            
        freq_t = dict()

        freq_window = dict()
        longest = float('inf')

        for char in t:
            freq_t[char] = freq_t.get(char,0) +1 

        have = 0
        need = len(freq_t.keys())
        res = ""
        l = 0

        for r in range(len(s)):
            freq_window[s[r]] = freq_window.get(s[r],0) + 1

            if s[r] in freq_t and freq_window[s[r]] == freq_t[s[r]]:
                have += 1
            
            while have == need:
                if r-l+1 < longest:
                    longest = r-l+1
                    res = s[l:r+1]
                
                freq_window[s[l]] -= 1

                if s[l] in freq_t and freq_window.get(s[l], 0) < freq_t[s[l]]:
                    have -= 1

                l+=1

        if longest == float('inf'):
            return ""
        return res



        



        
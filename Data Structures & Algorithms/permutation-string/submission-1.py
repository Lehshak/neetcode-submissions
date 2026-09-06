class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        req_freq = dict()
        for char in s1:
            req_freq[char] = req_freq.get(char, 0) + 1

        freq = dict()
        sp = 0
        ep = len(s1) - 1

        for i in range(ep + 1):
            freq[s2[i]] = freq.get(s2[i], 0) + 1

        while ep < len(s2):
            # check if its matching
            if freq == req_freq:
                return True

            # remove old sp freq
            freq[s2[sp]] -= 1
            if freq[s2[sp]] == 0:
                del freq[s2[sp]]

            sp += 1

            # add new ep freq
            ep += 1
            if ep < len(s2):
                freq[s2[ep]] = freq.get(s2[ep], 0) + 1

        return False






        





        
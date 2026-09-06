class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        freq_s1 = dict()

        for char in s1:
            freq_s1[char] = freq_s1.get(char,0) + 1

        freq_window = dict()

        l = 0
        for i in range(len(s1)):
            freq_window[s2[i]] = freq_window.get(s2[i], 0) + 1


        if freq_window == freq_s1:
            return True

        for r in range(len(s1), len(s2)):
            freq_window[s2[l]] = freq_window.get(s2[l],0) - 1
            if freq_window[s2[l]] == 0:
                del freq_window[s2[l]]
            freq_window[s2[r]] = freq_window.get(s2[r],0) + 1

            print(freq_window)
            print(freq_s1)

            if freq_window == freq_s1:
                return True

            l+=1

        return False








        





        
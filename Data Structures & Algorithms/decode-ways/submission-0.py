from collections import defaultdict
class Solution:
    def numDecodings(self, s: str) -> int:

        if not s or s[0] == "0":
            return 0

        ways = defaultdict(int)
        # ways to decode the sol at i

        ways[0] = 1
        #empty prefix has only one way to mapped
        ways[1] = 1

        for i in range(2, len(s)+1):
            # 2 is the digit at index i-1
            digit_one = s[i-1]
            two_digits = s[i-2:i]

            if digit_one != "0":
                ways[i] += ways[i-1]

            if 10 <= int(two_digits) <=26:
                #valid 
                ways[i] += ways[i-2]

        return ways[len(s)]



        





        
class Solution:
    def numDecodings(self, s: str) -> int:

        if not s or s[0] == "0":
            return 0

        codings = {0:1, 1:1}
        # index : number of possible decodings
        for i in range(2, len(s)+1):
            # string index
            index = i-1

            first_d = s[index-1]
            second_d = s[index]
            
            num = int(first_d+second_d)
            codings[i] = 0
            if second_d != "0":
                print(codings)
                codings[i] += codings[i-1]
            if 10 <= num <= 26:
                codings[i] += codings[i-2]

        return codings[len(s)]




        
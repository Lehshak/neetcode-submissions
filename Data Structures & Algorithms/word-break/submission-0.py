class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        can_reach = {0}
        # can we reach the char at this index

        for l in range(len(s)):
            
            if l in can_reach:
                for word in wordDict:
                    # check if l to r + 1 == word
                    if s[l:l+len(word)] == word:
                        # match!
                        can_reach.add(l+len(word))
        
        if len(s) in can_reach:
            return True
        else:
            return False

            


        




        
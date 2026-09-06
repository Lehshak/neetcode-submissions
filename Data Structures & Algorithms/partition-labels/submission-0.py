class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        partitions = []
        last_seen = {}

        for i in range(len(s)):
            char = s[i]
            last_seen[char] = i

        # now that we have the last seen positions we can create the partitions
        ep = 0
        sp = 0
        while sp < len(s):
            curr_char = s[sp]
            curr_break = last_seen[curr_char]
            while ep < curr_break:
                ep += 1
                curr_break = max(curr_break, last_seen[s[ep]])
            partitions.append(ep - sp + 1)
            sp = ep + 1

        return partitions

            



                





    



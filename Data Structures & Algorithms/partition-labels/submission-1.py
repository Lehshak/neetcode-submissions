class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        partitions = []
        last_seen = {}

        for i in range(len(s)):
            char = s[i]
            last_seen[char] = i

        # now that we have the last seen positions we can create the partitions
        sp = 0  # Start of the current partition
        ep = 0  # End of the current partition

        # Pass 2: Linearly scan through the string
        for i in range(len(s)):
            ep = max(last_seen[s[i]], ep)
            if i == ep:
                partitions.append(ep - sp + 1)
                sp = ep + 1

        return partitions



            



                





    



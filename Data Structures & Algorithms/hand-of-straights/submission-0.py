class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        if len(hand) % groupSize != 0:
            return False

        hand.sort()

        freq = dict()     

        # 1 2 2 3 3 4 4 5

        for entry in hand:
            freq[entry] = freq.get(entry, 0) + 1

        for card in hand:
            if freq.get(card, 0) == 0:
                # skip
                continue

            for i in range(groupSize):
                freq[card] = freq.get(card, 0) - 1

                if freq[card] < 0:
                    return False

                card += 1
            


        return True



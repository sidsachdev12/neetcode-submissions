class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        if n % groupSize != 0:
            return False

        counts = {}
        hand.sort()

        for i in range(n-1):
            
            if hand[i] not in counts:
                counts[hand[i]] = 1
            else:
                counts[hand[i]] += 1

        if hand[-1] not in counts:
            counts[hand[-1]] = 1
        else:
            counts[hand[-1]] += 1

        # print(hand)
        # print(counts)

        while counts:
            min_num = min(counts.keys())

            for i in range(groupSize):
                if (min_num + i) not in counts:
                    return False

                counts[min_num + i] -= 1
                if counts[min_num + i] == 0:
                    counts.pop(min_num + i)

            # print(counts)

        return True
        
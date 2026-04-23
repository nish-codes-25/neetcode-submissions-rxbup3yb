class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize !=0:
            return False
        hashMap = {}
        for h in hand:
            hashMap[h] = 1 + hashMap.get(h, 0)
        print(hashMap)
        hand.sort()

        for num in hand:
            if hashMap[num]:
                for i in range(num, num+groupSize):
                    if not hashMap.get(i, 0):
                        return False
                    hashMap[i] -= 1
        return True
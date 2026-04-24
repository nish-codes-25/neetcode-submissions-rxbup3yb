class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        x = y = z = False

        for t in triplets:
            x |= (t[0]==target[0] and t[1]<=target[1] and t[2]<=target[2])
            y |= (t[0]<=target[0] and t[1]==target[1] and t[2]<=target[2])
            z |= (t[0]<=target[0] and t[1]<=target[1] and t[2]==target[2])

            if x and y and z:
                return True
        return False
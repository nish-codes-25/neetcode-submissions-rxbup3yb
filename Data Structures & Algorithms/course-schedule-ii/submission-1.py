class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {i:[] for i in range(numCourses)}
        for crs, preCrs in prerequisites:
            preMap[crs].append(preCrs)

        visit, cycle = set(), set()
        res = []
        def dfs(crs):
            if crs in cycle:
                return False

            if crs in visit:
                return True

            cycle.add(crs)
            print(crs, cycle, visit, res)
            for preCrs in preMap[crs]:
                if dfs(preCrs)==False:
                    return False
            cycle.remove(crs)
            visit.add(crs)
            res.append(crs)

        for i in range(numCourses):
            if dfs(i)==False:
                return []

        return res
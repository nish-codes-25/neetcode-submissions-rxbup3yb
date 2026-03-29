class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i:[] for i in range(numCourses)}
        for crs, preCrs in prerequisites:
            preMap[crs].append(preCrs)

        visit = set()

        def dfs(crs):
            if crs in visit:
                return False

            if preMap[crs] == []:
                return True

            visit.add(crs)
            for preCrs in preMap[crs]:
                if not dfs(preCrs): return False
            visit.remove(crs)
            preMap[crs] = []

            return True

        for c in range(numCourses):
            if not dfs(c):
                return False

        return True

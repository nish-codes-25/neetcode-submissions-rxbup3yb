class TimeMap:

    def __init__(self):
        self.m = {} # key -> string; val -> [[value, timestamp]]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.m:
            self.m[key] = []
        self.m[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ""

        values = self.m.get(key, [])

        l, r = 0, len(values) - 1

        while l<=r:
            mid = (l+r)//2

            if values[mid][1] == timestamp:
                return values[mid][0]
            elif values[mid][1] < timestamp:
                res = values[mid][0]
                l = mid + 1
            else:
                r = mid - 1
        return res

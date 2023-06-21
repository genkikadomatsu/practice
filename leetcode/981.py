from collections import defaultdict


class TimeMap:

    def __init__(self):
        self.kv_map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.kv_map[key].append((timestamp, value)) 

    def get(self, key: str, timestamp: int) -> str:

        times = self.kv_map[key]
        left, right = 0, len(times) - 1
        result = (float("inf"), "")

        while left <= right:

            mid = (left + right) // 2

            if times[mid][0] < timestamp:
                result = times[mid]
                left = mid + 1
            elif times[mid][0] > timestamp:
                right = mid - 1
            else:
                return times[mid][1]

        return result[1]
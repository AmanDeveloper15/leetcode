class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        hours.sort()
        first = 0
        last = len(hours)

        while first < last:
            mid = (first + last) // 2

            if hours[mid] >= target:
                last = mid
            else:
                first = mid + 1

        return len(hours) - first
        
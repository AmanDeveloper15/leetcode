class Solution:
    def maximumCount(self, nums: list[int]) -> int:
        n=len(nums)
        i=0
        j=n
        while i < j:
            mid = i+(j-i) // 2

            if nums[mid] < 0:
                i = mid + 1
            else:
                j = mid

        neg = i


        i=0
        j=n
        while i < j:
            mid = i+(j-i) // 2
            if nums[mid]<=0:
                i = mid + 1
            else:
                j = mid

        pos = n-i
        return max(pos, neg)
class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        single = 0
        double_digit = 0

        for num in nums:
            if num < 10:
                single += num
            else:
                double_digit += num

        return single != double_digit
        
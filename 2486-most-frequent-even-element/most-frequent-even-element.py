class Solution:
    def mostFrequentEven(self, nums: list[int]) -> int:
        mp = {}

        # Count frequency of even numbers
        for num in nums:
            if num % 2 == 0:
                if num in mp:
                    mp[num] += 1
                else:
                    mp[num] = 1

        ans = -1
        maxi = 0

        # Find most frequent even number
        for key, value in mp.items():

            if value > maxi:
                maxi = value
                ans = key

            elif value == maxi and key < ans:
                ans = key

        return ans
        
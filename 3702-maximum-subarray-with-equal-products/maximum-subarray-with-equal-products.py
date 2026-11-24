class Solution:
    def maxLength(self, nums: List[int]) -> int:
        ans = 1
        n = len(nums)

        for i in range(n):

            product = 1
            gcd = 0
            lcm = 1

            for j in range(i, n):

                product *= nums[j]

                gcd = math.gcd(gcd, nums[j])

                lcm = math.lcm(lcm, nums[j])

                if product == gcd * lcm:
                    ans = max(ans, j - i + 1)

        return ans

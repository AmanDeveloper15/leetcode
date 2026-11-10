class Solution:
    def countQuadruplets(self, nums: list[int]) -> int:
        n = len(nums)
        count = 0
        freq = {}

        for d in range(3, n):
            freq = {}

            for c in range(d):
                target = nums[d] - nums[c]

                count += freq.get(target, 0)

                for a in range(c):
                    pair_sum = nums[a] + nums[c]
                    freq[pair_sum] = freq.get(pair_sum, 0) + 1

        return count
class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:

        candidate1 = 0
        candidate2 = 0
        count1 = 0
        count2 = 0

        for i in range(len(nums)):

            if candidate1 == nums[i]:
                count1 += 1

            elif candidate2 == nums[i]:
                count2 += 1

            elif count1 == 0:
                candidate1 = nums[i]
                count1 = 1

            elif count2 == 0:
                candidate2 = nums[i]
                count2 = 1

            else:
                count1 -= 1
                count2 -= 1

        count1 = 0
        count2 = 0

        for i in range(len(nums)):
            if candidate1 == nums[i]:
                count1 += 1
            elif candidate2 == nums[i]:
                count2 += 1

        ans = []

        if count1 > len(nums) // 3:
            ans.append(candidate1)

        if count2 > len(nums) // 3:
            ans.append(candidate2)

        return ans
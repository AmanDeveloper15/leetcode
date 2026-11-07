class Solution:
    def addToArrayForm(self, num: list[int], k: int) -> list[int]:

        target = str(k)

        index1 = len(num) - 1
        index2 = len(target) - 1

        carry = 0
        ans = []

        while index1 >= 0 or index2 >= 0 or carry:

            sum = carry

            if index1 >= 0:
                sum += num[index1]
                index1 -= 1

            if index2 >= 0:
                sum += int(target[index2])
                index2 -= 1

            carry = sum // 10
            ans.append(sum % 10)

        return ans[::-1]
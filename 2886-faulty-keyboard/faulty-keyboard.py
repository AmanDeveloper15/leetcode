class Solution:
    def finalString(self, s: str) -> str:
        arr = []

        for i in range(len(s)):
            if s[i] != 'i':
                arr.append(s[i])
            else:
                arr.reverse()

        return "".join(arr)
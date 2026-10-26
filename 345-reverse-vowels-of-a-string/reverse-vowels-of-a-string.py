class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"
        arr = list(s)
        found = []
        for i in range(len(s)):
            if arr[i] in vowels:
                found.append(arr[i])
                arr[i] = '*'

        found.reverse()
        count = 0
        for i in range(len(arr)):
             if arr[i] == '*':
                arr[i] = found[count]
                count += 1

        return "".join(arr)

            
        
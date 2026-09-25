class Solution:
    def sortVowels(self, s: str) -> str:

      
        # Frequency arrays for lowercase and uppercase letters
        lower = [0] * 26
        upper = [0] * 26

        # Count vowels and replace them with '#'
        s = list(s)

        for i in range(len(s)):

            # Lowercase vowels
            if s[i] in "aeiou":
                lower[ord(s[i]) - ord('a')] += 1
                s[i] = '#'

            # Uppercase vowels
            elif s[i] in "AEIOU":
                upper[ord(s[i]) - ord('A')] += 1
                s[i] = '#'

        # Create sorted vowel string
        vowel = ""

        # Uppercase vowels: A E I O U
        for i in range(26):
            c = chr(ord('A') + i)

            while upper[i]:
                vowel += c
                upper[i] -= 1

        # Lowercase vowels: a e i o u
        for i in range(26):
            c = chr(ord('a') + i)

            while lower[i]:
                vowel += c
                lower[i] -= 1

        # Put sorted vowels back
        first = 0
        second = 0

        while second < len(vowel):

            if s[first] == '#':
                s[first] = vowel[second]
                second += 1

            first += 1

        return "".join(s)
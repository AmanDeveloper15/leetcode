
class Solution:

    # 1. Build the LPS array
    def lpsfind(self, lps, s):
        pre = 0
        suf = 1

        while suf < len(s):
            if s[pre] == s[suf]:
                lps[suf] = pre + 1
                pre += 1
                suf += 1
            else:
                if pre == 0:
                    lps[suf] = 0
                    suf += 1
                else:
                    pre = lps[pre - 1]

    # 2. KMP pattern matching
    def KMP_MATCH(self, haystack, needle):
        lps = [0] * len(needle)
        self.lpsfind(lps, needle)

        first = 0
        second = 0

        while first < len(haystack) and second < len(needle):
            if haystack[first] == needle[second]:
                first += 1
                second += 1
            else:
                if second == 0:
                    first += 1
                else:
                    second = lps[second - 1]

        return 1 if second == len(needle) else 0

    # 3. Repeated String Match
    def repeatedStringMatch(self, a: str, b: str) -> int:
        if b == "":
            return 0
        if a == "":
            return -1
        if a == b:
            return 1

        repeat = 1
        temp = a

        while len(temp) < len(b):
            temp += a
            repeat += 1

        if self.KMP_MATCH(temp, b) == 1:
            return repeat

        if self.KMP_MATCH(temp + a, b) == 1:
            return repeat + 1

        return -1
class Solution:
    def platesBetweenCandles(self, s: str, queries: list[list[int]]) -> list[int]:
        n = len(s)

        prefix = [0] * n
        left = [0] * n
        right = [0] * n

        # 1. Prefix sum
        count = 0

        for i in range(n):
            if s[i] == '*':
                count += 1

            prefix[i] = count

        # 2. Nearest candle on left
        candle = -1

        for i in range(n):
            if s[i] == '|':
                candle = i

            left[i] = candle

        # 3. Nearest candle on right
        candle = -1

        for i in range(n - 1, -1, -1):
            if s[i] == '|':
                candle = i

            right[i] = candle

        # 4. Answer queries
        answer = []

        for l, r in queries:

            start = right[l]
            end = left[r]

            if start == -1 or end == -1 or start >= end:
                answer.append(0)

            else:
                plates = prefix[end] - prefix[start]

                answer.append(plates)

        return answer
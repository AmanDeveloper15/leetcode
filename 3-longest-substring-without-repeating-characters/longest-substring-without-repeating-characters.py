class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count=[0]*256
        first=0
        second=0
        length=0
        while second<len(s):
            while count[ord(s[second])]==1:
                count[ord(s[first])]=0
                first+=1
            count[ord(s[second])]=1
            length = max(length, second - first + 1)
            second+=1
        return length

            

        
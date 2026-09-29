class Solution:
    def romanToInt(self, s: str) -> int:
        def num(c):
            if c=='I':

               return 1
            elif c=='V':

                return 5
            elif c=='X':

                return 10
            elif c=='L':

                return 50
            elif c=='C':

                return 100
            elif c=='D':

                return 500
            elif c=='M':

                return 1000
        
        index=0
        sum=0

        while index<len(s)-1:
            if num(s[index])<num(s[index+1]):
                sum-=num(s[index])
            else:
                sum+=num(s[index])
            index+=1
        return sum + num(s[-1])
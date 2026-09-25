class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        if len(num1) < len(num2):
            num1, num2 = num2, num1 # to store small length in num2
        index1=len(num1)-1
        index2=len(num2)-1
        carry=0
        ans=""
       
        while index2>=0:
            sum=int(num1[index1])+int(num2[index2])+carry
            carry=sum//10
            ch=str(sum%10)
            ans+=ch
            index1-=1
            index2-=1

        while index1>=0:
             sum=int(num1[index1])+carry
             carry=sum//10
             ch=str(sum%10)
             ans+=ch
             index1-=1
        if carry:
          ans+= str(carry)
           
        return ans[::-1]


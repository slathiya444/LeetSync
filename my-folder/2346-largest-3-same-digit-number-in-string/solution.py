class Solution:
    def largestGoodInteger(self, num: str) -> str:
        n=len(num)
        ans=""
        for i in range(n):
            if i+2<n and num[i]==num[i+1] and num[i]==num[i+2]:
                ans=max(ans,num[i:i+3])
        return ans  
        

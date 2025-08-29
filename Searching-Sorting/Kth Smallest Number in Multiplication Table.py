#Kth Smallest Number in Multiplication Table

class Solution:

    def count_elements(self,x,m,n):
        count=0
        for i in range(1,m+1):
            count+=min(x//i,n)

        return count

    def findKthNumber(self, m: int, n: int, k: int) -> int:

        low = 1
        high = m*n

        

        while low<high:

            mid = (high+low)//2

            flag = self.count_elements(mid,m,n)

            if flag<k:
                low = mid+1
            else:
                high = mid

        return low
        

s= Solution()

print(s.findKthNumber(4,9,6))
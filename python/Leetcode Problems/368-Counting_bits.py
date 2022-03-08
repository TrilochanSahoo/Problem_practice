# Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

# Example 1:

# Input: n = 2
# Output: [0,1,1]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10
# Example 2:

# Input: n = 5
# Output: [0,1,1,2,1,2]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10
# 3 --> 11
# 4 --> 100
# 5 --> 101

# Constraints:

# 0 <= n <= 105

def countOne(n):
        n=str(n)
        count=0
        for i in n:
            if i=='1':
                count+=1
        return count
    
class Solution:
    
    def countBits(self, n: int) -> List[int]:
        num = []
        for i in range(n+1):
            x=bin(i).replace("0b", "")
            num.append(countOne(x))
        return num
    


class Solution:
    
    def countBits(self, num: int) -> List[int]:
        arr = [0]
        for i in range(1,num+1):
            arr.append(arr[i>>1]+(i&1))       
        return arr

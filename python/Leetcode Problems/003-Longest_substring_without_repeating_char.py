# Given a string s, find the length of the longest substring without repeating characters.

 

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r = 0,0
        count = 0
        stack = set()
#         for i in range(len(s)):
#             if s[i] not in stack:
#                 stack.add(s[i])
                
#             else:
#                 while(stack[0]!=s[i]):
#                     stack.remove(s[i])
#                 # stack.append(s[i])
#             count = max(count,len(stack))
        while(r<len(s)):
            if s[r] in stack:
                while s[l]!=s[r]:
                    stack.remove(s[l])
                    l+=1
                l+=1
            else:
                stack.add(s[r])
                count=max(count,len(stack))
            r+=1
        return count
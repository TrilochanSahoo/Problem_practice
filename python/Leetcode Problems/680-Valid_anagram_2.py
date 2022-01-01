# Given a string s, return true if the s can be palindrome after deleting at most one character from it.

# Example 1:

# Input: s = "aba"
# Output: true
# Example 2:

# Input: s = "abca"
# Output: true
# Explanation: You could delete the character 'c'.
# Example 3:

# Input: s = "abc"
# Output: false

class Solution:
    def validPalindrome(self, s: str) -> bool:
        start = 0
        end = len(s)-1
        while(start<end+1):
            if s[start]!=s[end]:
                s1 = s[start:end]
                s2 = s[start+1:end+1]
                if s1 == s1[::-1]:
                    return True
                if s2 == s2[::-1]:
                    return True
                return False
            start+=1
            end-=1
        return True
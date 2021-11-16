# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
 

# Example 1:

# Input: s = "()"
# Output: true
# Example 2:

# Input: s = "()[]{}"
# Output: true
# Example 3:

# Input: s = "(]"
# Output: false
# Example 4:

# Input: s = "([)]"
# Output: false
# Example 5:

# Input: s = "{[]}"
# Output: true
 

# Constraints:

# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2!=0:
            return False
        stack = []
        brackets = {'(':')','{':'}','[':']'}
        for ch in s:
            if ch in brackets:
                stack.append(ch)
            elif len(stack)!=0 and ch == brackets[stack[-1]]:
                stack.pop()
            else:
                return False
        if len(stack)==0:
            return True
        else:
            return False
        
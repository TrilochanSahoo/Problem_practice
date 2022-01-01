# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# Example 1:

# Input: s = "anagram", t = "nagaram"
# Output: true

# Example 2:

# Input: s = "rat", t = "car"
# Output: false
 
# Constraints:
# 1 <= s.length, t.length <= 5 * 104
# s and t consist of lowercase English letters.

class Solution(object):
    def isAnagram(self, s, t):
        if len(s)==len(t):
            for i in s:
                if i in t:
                    t=t.replace(i,"",1)
                else:
                    return False
            return True
        else:
            return False
        
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        sm, tm = {},{}
        for c in s:
            if c not in sm:
                sm[c]=1
            else:
                sm[c]+=1
        for c in t:
            if c not in tm:
                tm[c]=1
            else:
                tm[c]+=1
        if len(sm)!=len(tm):
            return False
        for c in sm.keys():
            if c not in tm or sm[c]!=tm[c]:
                return False
        return True
        
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        char_dictS = dict()
        char_dictT = dict()
        for c in s:
            char_dictS[c] = char_dictS.get(c, 0)+1
        for c in t:
            char_dictT[c] = char_dictT.get(c, 0)+1
        return char_dictS == char_dictT



        

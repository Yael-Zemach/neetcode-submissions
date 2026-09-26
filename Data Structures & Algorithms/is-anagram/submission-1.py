class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        char_dictS = dict()
        for c in s:
            char_dictS[c] = char_dictS.get(c, 0)+1
        for c in t:
            if char_dictS.get(c, 0) == 0:
                return False
            char_dictS[c]-=1

            
        return True



        

class Solution:
    def isValid(self, s: str) -> bool:
        bucket_dict = {")":"(", "]":"[", "}":"{"}
        stack = []
        for c in s:
            if c in "[({":
                stack.append(c)
            else:
                if not stack or stack.pop() != bucket_dict[c]:
                    return False
        if stack: 
            return False
        return True

    
        

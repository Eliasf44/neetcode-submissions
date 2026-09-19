class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {')':'(', ']':'[', '}':'{'}

        stack = []

        for ch in s:
            if ch in pairs.values():
                stack.append(ch)
            elif ch in pairs:
                if not stack or stack.pop() != pairs[ch]:
                    return False
            else:
                continue
            
        return not stack
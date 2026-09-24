class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []

        dic = {
            '}' : '{',
            ']' : '[',
            ')' : '('
        }


        for i in s:
            if i in dic.values():
                stack.append(i)
            elif i in dic.keys():
                if not stack or stack.pop() != dic[i]:
                    return False
            else:
                return False

        
        return not stack
class Solution:
    def scoreOfString(self, s: str) -> int:
        out = 0
        re = list(s)
        i = 0

        while i < len(re) - 1:
            cur = ord(re[i])
            nxt = ord(re[i+1])
            out += abs(nxt-cur)
            i += 1

        
        return out

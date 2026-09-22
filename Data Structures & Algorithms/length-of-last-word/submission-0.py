class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        reverse = s[::-1]

        br = reverse.split()

        it = br[0]

        i = 0
        for char in it:
            i+= 1
        
        return i
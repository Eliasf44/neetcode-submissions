class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        iteration = iter(t)

        return all(char in iteration for char in s)
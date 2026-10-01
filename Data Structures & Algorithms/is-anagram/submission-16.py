class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        h1 = {}
        h2 = {}

        for i, j in zip(s, t):
            if i in h1:
                h1[i] += 1
            else:
                h1[i] = 1

            if j in h2:
                h2[j] += 1
            else:
                h2[j] = 1

        return h1 == h2
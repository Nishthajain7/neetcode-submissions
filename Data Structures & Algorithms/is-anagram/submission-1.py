class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        chars, chart = {}, {}
        for i in range(len(s)):
            chars[s[i]] = chars.get(s[i], 0) + 1
            chart[t[i]] = chart.get(t[i], 0) + 1
        if chars==chart:
            return True
        return False       
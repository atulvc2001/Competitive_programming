class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        lstofwrds = s.split(" ")
        return len(lstofwrds[-1])

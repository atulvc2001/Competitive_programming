class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        
        curr = 0

        for i in columnTitle:
            curr = curr*26 + ord(i) - 64

        return curr

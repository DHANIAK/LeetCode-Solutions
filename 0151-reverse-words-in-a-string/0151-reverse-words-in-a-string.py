class Solution:
    def reverseWords(self, s: str) -> str:
        rev=s.split()
        s=rev[::-1]
        return " ".join(s)
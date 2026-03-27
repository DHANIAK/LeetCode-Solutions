class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res=[]
        k=len(p)
        p_sorted=sorted(p)
        for i in range(len(s)-k+1):
            if sorted(s[i:i+k])==p_sorted:
                res.append(i)
        return res        
        
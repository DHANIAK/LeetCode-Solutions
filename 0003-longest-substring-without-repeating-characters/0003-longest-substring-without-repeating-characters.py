class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        ml=0
        cset=set()
        n=len(s)
        for right in range(n):
            if s[right] not in cset:
                cset.add(s[right])
                ml=max(ml,right-left+1)
            else:
                while s[right] in cset:
                    cset.remove(s[left])
                    left+=1
                cset.add(s[right])
        return ml            


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
class Solution:
    def romanToInt(self, s: str) -> int:
        roman={
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }
        total=0
        prev_value=0
        for char in reversed(s):
            value=roman[char]
            if value<prev_value:
                total-=value
            else:
                total+=value
            prev_value=value
        return total    
solution = Solution()
s = "III"
print(solution.romanToInt(s))                     

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        
        h = 0
        
        for i in range(len(citations)):
            if citations[i] >= i + 1:
                h = i + 1
            else:
                break
                
        return h

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna
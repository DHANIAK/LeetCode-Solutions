class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        prof=0
        for i in range(1,n):
            if prices[i]>prices[i-1]:
                prof+=prices[i]-prices[i-1]
        return prof               

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna
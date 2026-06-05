class Solution:
    def jump(self, nums: List[int]) -> int:
        ce=0
        f=0
        j=0
        n=len(nums)
        for i in range(n-1):
            f=max(f,i+nums[i])
            if i==ce:
                j+=1
                ce=f
        return j        

               

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna
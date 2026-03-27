class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        st=[]
        maxarea=0
        for i,h in enumerate(heights):
            start=i
            while st and st[-1][1]>h:
                idx,h1=st.pop()
                maxarea=max(maxarea,h1*(i-idx))
                start=idx
            st.append((start,h))
        n=len(heights)
        for idx,h1 in st:
            maxarea=max(maxarea,h1*(n-idx))
        return maxarea
        
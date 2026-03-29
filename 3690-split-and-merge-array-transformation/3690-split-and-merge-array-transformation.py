class Solution:
    def minSplitMerge(self, nums1: List[int], nums2: List[int]) -> int:
        target = tuple(nums2)
        start = tuple(nums1)
        
        if start == target:
            return 0
        
        q = deque([(start, 0)])
        visited = set([start])
        
        while q:
            arr, steps = q.popleft()
            n = len(arr)
            
            
            for L in range(n):
                for R in range(L, n):
                    sub = arr[L:R+1]
                    remaining = arr[:L] + arr[R+1:]
                    
                    
                    for i in range(len(remaining) + 1):
                        new_arr = remaining[:i] + sub + remaining[i:]
                        
                        if new_arr == target:
                            return steps + 1
                        
                        if new_arr not in visited:
                            visited.add(new_arr)
                            q.append((new_arr, steps + 1))
        
        return -1
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights)-1
        amax=0
        while l<r:
            area = (r-l)*min(heights[r],heights[l])
            amax=max(amax, area)
            if heights[l]<heights[r]:
                l+=1
            else:
                r-=1
        return amax 
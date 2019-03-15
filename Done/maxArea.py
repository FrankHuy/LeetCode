class Solution:
    def maxArea(self, height: List[int]) -> int:
        result = 0
        leftp = 0
        rightp = len(height) - 1
        while(leftp != rightp):
            pre_result = (rightp-leftp) * min(height[leftp],height[rightp])
            result = max(pre_result,result)
            if(height[leftp]<height[rightp]):
                leftp += 1
            else:
                rightp -= 1
        return result
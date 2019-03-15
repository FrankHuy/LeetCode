class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i=0
        while True:
            if(i>=len(nums)):
                break;
            if nums[i] == val:
                nums.pop(i)
            else:
                i+=1
        return len(nums)
        
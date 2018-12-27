import pdb
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        num1 = self.findMedian(nums1)
        num2 = self.findMedian(nums2)
        if (num1 == None):
            return num2
        elif(num2 == None):
            return num1
        else:
            return ((num1+num2)/2)
    def findMedian(self,nums):
        length = len(nums)
        if(length == 0):
            return None
        elif(length % 2 == 0 ):
            return (nums[int(length/2)]+nums[int((length/2)-1)])/2
        else:
            return nums[int(length/2)]
def main():
    a = Solution()
    nums1 = [1,3]
    nums2 = [2]
    print (a.findMedianSortedArrays(nums1,nums2))
if __name__ == '__main__':
    main()
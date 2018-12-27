import pdb
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        if(len(nums1) == 0):
            return self.findMedian(nums2)
        elif(len(nums2) == 0):
            return self.findMedian(nums1)
        else:
            length = len(nums1)+len(nums2)
            times = int(length/2) + 1
            n1 = 0
            n2 = 0
            result = list()
            for i in range(times):
                #pdb.set_trace()
                if (n2+1 > len(nums2)):
                    result.append(nums1[n1])
                    n1+=1
                elif(n1+1 > len(nums1)):
                    result.append(nums2[n2])
                    n2+=1
                elif (nums1[n1]<nums2[n2]):
                    result.append(nums1[n1])
                    n1 += 1
                else:
                    result.append(nums2[n2])
                    n2 += 1
            if(length%2 == 0):
                return (result[times-1]+result[times-2])/2
            else:
                return result[times-1]
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
    nums1 = [2]
    nums2 = []
    print (a.findMedianSortedArrays(nums1,nums2))
if __name__ == '__main__':
    main()
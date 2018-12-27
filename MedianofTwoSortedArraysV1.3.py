class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        Length = (len(nums1) + len(nums2))
        mid = int(Length / 2)
        if (len(nums1) == 0):
            return self.findMedian(nums2)
        elif (len(nums2) == 0):
            return self.findMedian(nums1)
        else:
            for i in range(len(nums1)):
                position = self.insertNum(nums1[i], nums2)
                nums2.insert(position, nums1[i])
                if (position >= mid or i == (len(nums1) - 1)):
                    if (Length % 2 == 0):
                        return (nums2[mid] + nums2[mid - 1]) / 2
                    else:
                        return nums2[mid]

    def findMedian(self, nums):
        length = len(nums)
        if (length == 0):
            return None
        elif (length % 2 == 0):
            return (nums[int(length / 2)] + nums[int((length / 2) - 1)]) / 2
        else:
            return nums[int(length / 2)]

    def insertNum(self, num, nums):
        start = 0
        end = len(nums) - 1
        while True:
            if (num >= nums[int((start + end) / 2)]):
                start = int((start + end) / 2) + 1
                if (end < start):
                    return start
            elif (num < nums[int((start + end) / 2)]):
                end = int((start + end) / 2) - 1
                if (end < start):
                    return end + 1


def main():
    a = Solution()
    nums1 = [1, 3]
    nums2 = [2]
    print(a.findMedianSortedArrays(nums1, nums2))


if __name__ == '__main__':
    main()
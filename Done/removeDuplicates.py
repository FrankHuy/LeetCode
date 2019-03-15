from collections import Counter
class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c = Counter(nums)
        c_list = c.most_common()
        nums.clear()
        for c_ in c_list:
                nums.append(c_[0])
        nums.sort()
        return len(nums)
        
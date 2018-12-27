#1.Two Sum
#Given an array of integers, return indices of the two numbers such that they add up to a specific target.
#You may assume that each input would have exactly one solution, and you may not use the same element twice.
#Example:
#Given nums = [2, 7, 11, 15], target = 9,
#Because nums[0] + nums[1] = 2 + 7 = 9,
#return [0, 1]
class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if((nums[i]+nums[j])==target):
                    return [i,j]
        return -1

def main():
    #nums = [0,2,4,6,8,10,12,14,16,18,20…………
    #print(len(nums))
    nums = [3,2,4]
    target = 6
    b = Solution()
    a = b.twoSum(nums,target)
    print(a)

if __name__ == '__main__':
        main()



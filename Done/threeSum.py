class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = list()
        if len(nums)<3:
            return res
        for i in range(len(nums)-2):
            if nums[i]>0:
                return res
            j=i+1
            k=len(nums)-1
            while (j<k):
                if nums[i]+nums[j]+nums[k]==0:
                    if not res.__contains__([nums[i],nums[j],nums[k]]):
                         res.append(list([nums[i],nums[j],nums[k]]))
                    j+=1
                    k-=1
                    while(nums[j]==nums[j-1]):
                            j+=1
                            if(j>k):
                                break
                elif nums[i]+nums[j]+nums[k]>0:
                    k-=1
                else:
                    j+=1
        return res
        
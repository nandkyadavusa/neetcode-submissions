class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count =0
        maxcount=0
        res=0
        for i in range(len(nums)):
            if nums[i]==1:
                count=count+1
               
                res=max(res,count)
            elif nums[i]==0:
                count=0
        return res

        
class Solution(object):
    def twoSum(self,nums,target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        result = {}
        if n <= 1:
            return False
        else:
            for i in range(n):
                if nums[i] in result:
                    return result[nums[i]],i
                else :
                    result[target-nums[i]]=i


nums=[2,7,11,15]
target=9
result=Solution()
result_num=result.twoSum(nums,target)
print(result_num)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prefix=1
        size=len(nums)
        result=[1]*size
        prefix=1

        for num in range(size):
            result[num]=prefix
            prefix*=nums[num]

        postfix=1
        for num in range(size-1,-1,-1):
            result[num]*=postfix
            postfix*=nums[num]

        return list(result)

        

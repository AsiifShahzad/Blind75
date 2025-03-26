class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
              #This check that is current and prevoius digit in sorted array is same or not if same than it return true
                return True
        return False

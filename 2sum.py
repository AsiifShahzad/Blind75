''' The problem asks us to find two numbers in the list that add up to the given target and return their indices. To solve this efficiently, we don’t check every pair; instead, we use a dictionary (hashmap). As we loop through each number in the list, we calculate the difference between the target and the current number. This difference represents the number we need to find to complete the pair. We check if this difference is already stored in the hashmap (meaning we’ve seen it before). If it is, we instantly return the stored index of that difference and the current index. If it’s not, we store the current number and its index in the hashmap and move on. This way, we only loop through the list once, making it very fast and efficient.
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in hashmap:
                return [hashmap[diff], i]
            hashmap[num] = i

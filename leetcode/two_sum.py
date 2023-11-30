class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        past_nums = {}
        for x,y in enumerate(nums):
            diff = target-y
            if diff in past_nums:
                return [past_nums[diff], x]
            past_nums[y]=x
    
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_l={}
        for i in range(len(nums)):
            diff = target - nums[i]
            if nums[i] not in hash_l:
                hash_l[diff] = i
            else:
                return [hash_l[nums[i]], i]
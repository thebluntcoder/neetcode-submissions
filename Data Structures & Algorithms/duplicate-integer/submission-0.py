class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        len_list = len(nums)
        len_set = len(set(nums))
        if len_list!=len_set:
            return True
        else:
            return False
        
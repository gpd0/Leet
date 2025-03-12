class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashMap = {}
        for index, value in enumerate(nums):
            if value in hashMap:
                return True
            hashMap[value] = index
        return False
        
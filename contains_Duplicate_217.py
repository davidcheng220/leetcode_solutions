class Solution:
    def containsDuplicate(self, nums: list) -> bool:
        hash_set = set()
        for i in nums:
            if i in hash_set:
                return True
            hash_set.add(i)
        return False
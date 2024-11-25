class Solution:
    def containsDuplicate(self, nums: list) -> bool:
        new_set = set()
        for i in nums:
            if i in new_set:
                return True
            else:
                new_set.add(i)
        return False
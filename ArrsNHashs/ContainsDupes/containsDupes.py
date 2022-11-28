from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        print(sorted(nums))

obj = Solution()
obj.containsDuplicate([1,5,3,4,2])
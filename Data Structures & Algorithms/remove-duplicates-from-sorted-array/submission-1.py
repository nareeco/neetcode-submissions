class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        seen = []
        i = 0
        while i < len(nums):
            if nums[i] in seen:
                nums.pop(i)
            else:
                seen.append(nums[i])
                k += 1
                i += 1

        return k
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        if m == 0:
            nums1[:] = nums2
        if n == 0:
            return
        combined = nums1[:m] + nums2
        combined.sort()
        nums1[:] = combined
class Solution:
    def minSum(self, nums1: list[int], nums2: list[int]) -> int:
        sum1 = sum(nums1)
        sum2 = sum(nums2)
        zeros1 = nums1.count(0)
        zeros2 = nums2.count(0)

        # Minimum possible sum for each array: current sum + number of zeros
        # (each zero must be replaced with at least 1)
        min_sum1 = sum1 + zeros1
        min_sum2 = sum2 + zeros2

        # If min_sum1 < min_sum2, we need to increase sum1.
        # We can only increase sum1 if it has zeros (replace them with larger values).
        # If nums1 has no zeros, we can't increase its sum, so it's impossible.
        if min_sum1 < min_sum2:
            if zeros1 == 0:
                return -1
            return min_sum2

        # Symmetric case
        if min_sum2 < min_sum1:
            if zeros2 == 0:
                return -1
            return min_sum1

        # min_sum1 == min_sum2
        return min_sum1

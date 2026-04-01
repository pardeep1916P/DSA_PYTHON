class Solution:

    """
    Left and Right Sum Differences — Prefix Sum Optimization (Optimal Solution)

    Approach:
    - Compute total sum of the array.
    - Maintain a running left sum.
    - For each element:
          • right sum = total - left - current element
          • append absolute difference |left - right|
    - Update left sum as you move forward.

    Example:
        nums = [10,4,8,3]
        result = [15,1,11,22]

    Time  : O(n) — single pass
    Space : O(n) — result array

    Note:
    - Avoids building separate prefix/suffix arrays.
    - Uses total sum trick for efficient computation.
    """

    def leftRightDifference(self, nums: List[int]) -> List[int]:

        total = sum(nums)
        left = 0
        res = []

        for num in nums:

            # Compute right sum using total and left
            right = total - left - num

            # Store absolute difference
            res.append(abs(left - right))

            # Update left sum
            left += num

        return res
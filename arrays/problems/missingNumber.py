class Solution:

    """
    Missing Number — Mathematical Sum Formula (Optimal Solution)

    Approach:
    - For numbers in range [0, n], the expected sum is:
          n * (n + 1) // 2
    - Subtract each element in the array from this total.
    - The remaining value is the missing number.

    Example:
        nums = [3,0,1]
        n = 3
        expected_sum = 3*4//2 = 6
        subtract 3,0,1 → remaining = 2

    Time  : O(n) — single pass
    Space : O(1) — constant extra space

    Note:
    This is one of the most optimal and interview-preferred solutions.
    Alternative optimal approach uses XOR.
    """

    def missingNumber(self, nums: List[int]) -> int:

        n = len(nums)

        # Expected sum of numbers from 0 to n
        tot = (n * (n + 1)) // 2

        # Subtract actual elements
        for num in nums:
            tot -= num

        return tot

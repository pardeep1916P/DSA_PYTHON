class Solution:

    """
    Max Consecutive Ones — Linear Scan Counter (Optimal Solution)

    Approach:
    - Traverse the array once.
    - Maintain two variables:
          • count → current streak of consecutive 1s
          • max   → longest streak seen so far
    - If the current element is 1:
          • increment count
    - If the current element is 0:
          • reset count to 0
    - Update max whenever a longer streak is found.

    Time  : O(n) — single pass through the array
    Space : O(1) — constant extra space
    """

    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        max, count = 0, 0

        for i in nums:

            # Increase streak if current number is 1
            if i == 1:
                count += 1
            else:
                # Reset streak when a 0 appears
                count = 0

            # Update maximum streak
            max = count if (count > max) else max

        return max
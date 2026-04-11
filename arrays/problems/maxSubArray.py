class Solution:

    """
    Maximum Subarray — Kadane’s Algorithm (Optimal Solution)

    Approach:
    - Maintain two variables:
          • current_sum → max subarray ending at current index
          • max_sum     → overall maximum subarray sum
    - For each element:
          • Either extend previous subarray OR start fresh from current element
          • Update max_sum accordingly

    Example:
        nums = [-2,1,-3,4,-1,2,1,-5,4]
        result = 6 → subarray [4,-1,2,1]

    Time  : O(n) — single pass
    Space : O(1)

    Note:
    - At each step, decide:
          “Continue previous subarray or start new?”
    """

    def maxSubArray(self, nums: List[int]) -> int:

        current_sum = nums[0]
        max_sum = nums[0]

        for i in range(1, len(nums)):

            # Either take current element alone OR extend previous subarray
            current_sum = max(nums[i], current_sum + nums[i])

            # Update global maximum
            max_sum = max(max_sum, current_sum)

        return max_sum
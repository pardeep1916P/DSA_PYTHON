class Solution:

    """
    Maximum Average Subarray I — Sliding Window (Optimal Solution)

    Approach:
    - Compute the sum of the first window of size k.
    - Slide the window across the array:
          • Add the next element
          • Remove the element leaving the window
    - Track the maximum window sum.
    - Return the maximum average (max_sum / k).

    Time  : O(n) — each element processed once
    Space : O(1) — constant extra space

    Note:
    - Avoid recomputing sum for every window.
    - Sliding window reduces time from O(n*k) to O(n).
    """

    def findMaxAverage(self, nums: List[int], k: int) -> float:

        # Initial window sum
        window_sum = sum(nums[:k])
        max_sum = window_sum

        # Slide the window
        for i in range(k, len(nums)):

            window_sum += nums[i] - nums[i - k]

            # Update maximum sum
            max_sum = max_sum if max_sum > window_sum else window_sum

        return max_sum / k
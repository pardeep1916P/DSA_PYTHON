class Solution:

    """
    Maximize Sum After K Negations — Greedy (Optimal Solution)

    Approach:
    - Sort the array.
    - Flip negative numbers first (largest gain).
    - Stop when:
          • no negatives left OR
          • k operations used
    - After processing:
          • If k is odd → flip the smallest element once
          • If k is even → no change needed

    Why it works:
    - Flipping negative numbers increases sum the most.
    - If flips remain, only parity (odd/even) matters.

    Time  : O(n log n) — sorting
    Space : O(1)

    Note:
    - min_val is used to handle leftover odd flips.
    """

    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:

        nums.sort()

        # Flip negatives greedily
        for i in range(len(nums)):
            if nums[i] < 0 and k > 0:
                nums[i] = -nums[i]
                k -= 1

        # Find smallest element after flipping
        min_val = min(nums)

        # If k is odd → flip smallest once
        if k % 2 == 1:
            return sum(nums) - 2 * min_val

        return sum(nums)
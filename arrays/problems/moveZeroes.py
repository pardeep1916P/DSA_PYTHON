class Solution:

    """
    Move Zeroes — Two Pointer In-Place Swap (Optimal Solution)

    Approach:
    - Maintain a pointer `k` indicating the position
      where the next non-zero element should be placed.
    - Traverse the array using index `i`:
          • If nums[i] is non-zero,
            swap it with nums[k] and increment k.
    - This ensures:
          • All non-zero elements retain their relative order.
          • All zeroes are moved to the end.

    Time  : O(n) — single pass
    Space : O(1) — in-place modification

    Note:
    Swapping works even when i == k (self-swap),
    so no additional condition is required.
    """

    def moveZeroes(self, nums: List[int]) -> None:

        k = 0  # position to place next non-zero element

        for i in range(len(nums)):

            if nums[i] != 0:
                temp = nums[k]
                nums[k] = nums[i]
                nums[i] = temp
                k += 1

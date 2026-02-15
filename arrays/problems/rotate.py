class Solution:

    """
    Rotate Array — Reversal Algorithm (Optimal In-Place Solution)

    Approach:
    - If k >= n, reduce it using k % n.
    - Reverse the entire array.
    - Reverse the first k elements.
    - Reverse the remaining n-k elements.
    - This effectively rotates the array to the right by k steps.

    Why it works:
    Example: [1,2,3,4,5,6,7], k = 3
      1) Reverse all        → [7,6,5,4,3,2,1]
      2) Reverse first 3    → [5,6,7,4,3,2,1]
      3) Reverse remaining  → [5,6,7,1,2,3,4]

    Time  : O(n) — each element swapped at most once
    Space : O(1) — in-place modification

    Note:
    This is the most optimal solution for array rotation
    without using extra space.
    """

    def rotate(self, nums: List[int], k: int) -> None:

        if len(nums) < 2 or k < 1: return

        n = len(nums)
        k = k % n  # handle cases where k > n

        # Step 1: Reverse entire array
        self.reverse(nums, 0, n - 1)

        # Step 2: Reverse first k elements
        self.reverse(nums, 0, k - 1)

        # Step 3: Reverse remaining elements
        self.reverse(nums, k, n - 1)

    def reverse(self, nums: List[int], l: int, r: int) -> None:

        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

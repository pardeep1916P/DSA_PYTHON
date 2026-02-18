class Solution:

    """
    Contains Duplicate II — Sliding Window with Set (Optimal Solution)

    Approach:
    - Maintain a sliding window of size at most k.
    - Use a set to store elements currently inside the window.
    - Traverse the array:
          • If nums[i] already exists in the window → duplicate found within k distance.
          • Add nums[i] to the window.
          • If window size exceeds k, remove nums[i - k] to maintain size constraint.
    - If no duplicate found within distance k, return False.

    Time  : O(n) — each element added and removed at most once
    Space : O(k) — window stores at most k elements

    Note:
    Using `discard()` avoids KeyError if element is not present.
    This ensures safe removal when shrinking the window.
    """

    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        n = len(nums)
        window = set()

        for i in range(n):

            # Duplicate found within window
            if nums[i] in window:
                return True

            window.add(nums[i])

            # Maintain window size ≤ k
            if len(window) > k:
                window.discard(nums[i - k])

        return False

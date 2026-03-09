class Solution:

    """
    Two Sum II — Two Pointer Technique (Optimal Solution)

    Approach:
    - Since the array is sorted, use two pointers:
          • l at the beginning
          • r at the end
    - Compute the sum of numbers[l] and numbers[r].
    - If the sum equals target → return the 1-based indices.
    - If the sum is smaller than target → move left pointer right.
    - If the sum is greater than target → move right pointer left.
    - Continue until the pointers meet.

    Time  : O(n) — each pointer moves at most n times
    Space : O(1) — constant extra space

    Note:
    - The problem requires **1-based indices**, so return l+1 and r+1.
    """

    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        l, r = 0, len(numbers) - 1

        while l < r:

            sum = numbers[l] + numbers[r]

            if sum == target: return [l + 1, r + 1]

            elif sum < target: l += 1

            else: r -= 1

        return [-1, -1]
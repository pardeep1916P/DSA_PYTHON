class Solution:

    """
    Third Maximum Number — Three Variables Tracking (Optimal Solution)

    Approach:
    - Maintain three variables:
          • first  → largest
          • second → second largest
          • third  → third largest
    - Traverse the array:
          • Skip duplicates to ensure distinct values.
          • Update first, second, third accordingly.
    - If third exists → return it
      else → return first (maximum).

    Example:
        nums = [2,2,3,1]
        distinct → [3,2,1]
        answer = 1

    Time  : O(n) — single pass
    Space : O(1) — constant extra space

    Note:
    - Using None helps handle initial comparisons cleanly.
    - Avoids sorting (which would be O(n log n)).
    """

    def thirdMax(self, nums: List[int]) -> int:

        first = second = third = None

        for num in nums:

            # Skip duplicates
            if num == first or num == second or num == third: continue

            # Update first, second, third
            if first is None or num > first:
                third = second
                second = first
                first = num

            elif second is None or num > second:
                third = second
                second = num

            elif third is None or num > third: third = num

        # Return third max if exists, else max
        return third if third is not None else first
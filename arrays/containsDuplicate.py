class Solution:

    """
    Contains Duplicate — HashSet Membership Check (Optimal Solution)

    Approach:
    - Use a set to track elements seen so far.
    - Traverse the array:
          • If the element already exists in the set,
            a duplicate is found → return True.
          • Otherwise, add the element to the set.
    - If traversal completes with no duplicates, return False.

    Time  : O(n) average — each lookup and insertion is O(1)
    Space : O(n) — in worst case, all elements stored in set

    Note:
    This is the standard and interview-expected solution.
    """

    def containsDuplicate(self, nums: List[int]) -> bool:

        seen = set()

        for i in nums:
            if i in seen: return True
            seen.add(i)

        return False

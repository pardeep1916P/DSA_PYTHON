class Solution:

    """
    Find All Numbers Disappeared in an Array — In-Place Marking (Optimal Solution)

    Approach:
    - The array contains numbers in range [1, n].
    - Use indices to mark presence:
          • For each number x → mark index (x-1) as visited
            by making nums[x-1] negative.
    - After marking:
          • Indices with positive values indicate missing numbers.

    Example:
        nums = [4,3,2,7,8,2,3,1]
        After marking → some indices remain positive → missing numbers

    Time  : O(n) — two passes
    Space : O(1) — in-place (no extra structures)

    Note:
    - Use abs() because values may already be negative.
    - This modifies the input array.
    """

    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        res = []

        # Mark indices as visited
        for i in range(len(nums)):
            
            index = abs(nums[i]) - 1

            if nums[index] > 0: nums[index] = -nums[index]

        # Collect missing numbers
        for i in range(len(nums)):
            
            if nums[i] > 0: res.append(i + 1)

        return res
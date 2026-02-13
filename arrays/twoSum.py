class Solution:

    """
    Two Sum — HashMap (Dictionary) Complement Lookup (Optimal Solution)

    Approach:
    - Traverse the array once.
    - For each element:
          • Compute its complement = target - current value.
          • If the complement already exists in the map,
            return the stored index and current index.
          • Otherwise, store the current value and its index in the map.
    - Return empty list if no solution exists.

    Time  : O(n) — single pass through the array
    Space : O(n) — dictionary stores seen elements

    Note:
    - Dictionary provides O(1) average lookup.
    - This is the standard and interview-expected solution.
    """

    def twoSum(self, nums: List[int], target: int) -> List[int]:

        map = {}  # value → index mapping

        for i in range(len(nums)):

            complement = target - nums[i]

            # If complement already seen, return indices
            if complement in map:
                return [map[complement], i]

            # Store current value with its index
            map[nums[i]] = i

        return []

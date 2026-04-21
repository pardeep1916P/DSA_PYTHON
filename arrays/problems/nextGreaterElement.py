class Solution:

    """
    Next Greater Element I — Monotonic Stack (Optimal Solution)

    Approach:
    - Use a decreasing stack to process nums2.
    - For each number in nums2:
          • While current number > top of stack:
                → current number is the next greater element
                → store in map
          • Push current number onto stack
    - Remaining elements in stack → no greater element → map to -1
    - Build result for nums1 using the map.

    Example:
        nums2 = [1,3,4,2]
        map = {1:3, 3:4, 4:-1, 2:-1}

    Time  : O(n + m)
            n = len(nums1), m = len(nums2)
    Space : O(m) — stack + hashmap

    Note:
    - Each element is pushed and popped at most once → O(n)
    - Classic monotonic stack pattern.
    """

    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        stack = []
        ele_map = {}

        # Build next greater map using nums2
        for num in nums2:

            # Resolve elements smaller than current
            while stack and num > stack[-1]:
                ele_map[stack.pop()] = num

            stack.append(num)

        # Remaining elements have no next greater
        while stack:
            ele_map[stack.pop()] = -1

        # Build result for nums1
        return [ele_map[num] for num in nums1]
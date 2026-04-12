class Solution:

    """
    Assign Cookies — Greedy Matching (Optimal Solution)

    Approach:
    - Sort both arrays:
          • g → children's greed factors
          • s → cookie sizes
    - Use two pointers:
          • i → child index
          • j → cookie index
    - Try to satisfy the least greedy child first.
    - If current cookie can satisfy child:
          • assign cookie → move to next child
    - Always move to next cookie.

    Example:
        g = [1,2,3], s = [1,1]
        → only 1 child satisfied

    Time  : O(n log n + m log m)
    Space : O(1)

    Note:
    - Greedy works because we always try to satisfy
      the smallest requirement first.
    """

    def findContentChildren(self, g: List[int], s: List[int]) -> int:

        g.sort()
        s.sort()

        i, j = 0, 0

        while i < len(g) and j < len(s):

            # If current cookie satisfies child
            if s[j] >= g[i]: i += 1  # move to next child

            j += 1  # always move to next cookie

        return i  # number of satisfied children
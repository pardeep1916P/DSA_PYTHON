class Solution:

    """
    Majority Element — Boyer–Moore Voting Algorithm (Optimal Solution)

    Approach:
    - Maintain two variables:
          • candidate → current majority candidate
          • votes → vote balance counter
    - Traverse the array:
          • If votes == 0, choose current element as candidate.
          • If element equals candidate → increment votes.
          • Otherwise → decrement votes.
    - Since a majority element (> n/2 times) is guaranteed,
      the final candidate will be the majority element.

    Why it works:
    - Majority element survives pairwise cancellations.
    - Non-majority elements cancel each other out.

    Time  : O(n) — single pass
    Space : O(1) — constant extra space

    Note:
    This is the most optimal solution.
    If majority were not guaranteed, a verification pass would be required.
    """

    def majorityElement(self, nums: List[int]) -> int:

        candidate, votes = 0, 0

        for i in nums:

            if votes == 0: candidate = i

            votes += 1 if i == candidate else -1

        return candidate

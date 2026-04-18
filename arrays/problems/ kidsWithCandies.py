class Solution:

    """
    Kids With the Greatest Number of Candies — Max Comparison (Optimal Solution)

    Approach:
    - Find the maximum number of candies among all kids.
    - For each child:
          • Check if current candies + extraCandies >= max_candies
          • Append True/False accordingly.

    Example:
        candies = [2,3,5,1,3], extra = 3
        max = 5
        result = [True, True, True, False, True]

    Time  : O(n) — one pass for max, one pass for result
    Space : O(n) — result list

    Note:
    - Simple comparison problem.
    - No need for sorting or complex logic.
    """

    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:

        max_candies = max(candies)
        result = []

        for candie in candies: result.append(candie + extraCandies >= max_candies)

        return result
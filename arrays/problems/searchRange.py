class Solution:
    def first(self, nums: List[int], target: int) -> List[int]:
        l = 0
        r = len(nums)-1
        ans = -1
        while l <= r:
            mid = (l+r)//2
            if nums[mid] == target:
                ans = mid
                r = mid - 1
            elif nums[mid]<target:
                l = mid+1
            elif nums[mid]>target:
                r = mid-1
        return ans

    def last(self, nums: List[int], target: int) -> List[int]:
        l = 0
        r = len(nums)-1
        ans = -1
        while l <= r:
            mid = (l+r)//2
            if nums[mid] == target:
                ans = mid
                l = mid + 1
            elif nums[mid]<target:
                l = mid+1
            elif nums[mid]>target:
                r = mid-1
        return ans

    def searchRange(self, nums: List[int], target: int) -> List[int]:

        return  [self.first(nums,target), self.last(nums,target)]

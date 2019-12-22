class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left, right = 0, n-1
        while left <= right:
            mid = (left+right)//2
            if nums[mid] > nums[-1]:
                left = mid + 1
            else:
                right = mid - 1
        right += n
        while left <= right:
            mid = (left+right)//2
            if nums[mid%n] == target:
                return mid%n 
            elif nums[mid%n] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1
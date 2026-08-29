class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = 0
        r = len(nums) - 1

        while l < r:
            two_sum = nums[l] + nums[r]

            if two_sum == target:
                return [l+1, r+1]

            if two_sum < target:
                l += 1
            
            if two_sum > target:
                r -= 1

        return [l, r]
        



        
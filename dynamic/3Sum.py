class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        len_nums = len(nums)
        if len_nums < 3:
            return []
        res = []
        nums.sort()
        for i in range(len_nums - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, len_nums - 1
            while left < right:
                sum_ = nums[i] + nums[left] + nums[right]

                if sum_ > 0:
                    right -= 1
                elif sum_ < 0:
                    left += 1
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
        return res
class Solution:
    def twoSum(self, nums,target):
        for num in nums:
            for var in nums:
                if num!=var:
                    result = num + var
                    if result == target:
                        return [num,var]

nums = [2,7,11,15]
target = 17
solution = Solution()
print(solution.twoSum(nums,target))

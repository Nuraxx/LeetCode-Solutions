#problem link : https://leetcode.com/problems/two-sum
class Solution(object):
    def twoSum(self, nums, target):
        # Loop through each element in the list by index
        for i in range(len(nums)):
            # Loop again to pair it with every other element
            for j in range(len(nums)):
                # Skip the same index (can't use the same element twice)
                if i == j:
                    continue
                # Check if the two numbers add up to the target
                if nums[i] + nums[j] == target:
                    # Return the indices of the two numbers
                    return [i, j]
#get the inputs
#call the function

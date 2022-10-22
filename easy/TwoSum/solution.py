class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}

        for i in range(len(nums)):
            remainingValue = target - nums[i]

            if remainingValue in hashMap:
                return [i, hashMap[remainingValue]]

            # Store index value
            hashMap[nums[i]] = i


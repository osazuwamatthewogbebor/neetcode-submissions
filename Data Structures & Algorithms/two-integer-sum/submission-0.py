class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map =  {}

        for i in range(len(nums)):
            num = nums[i]
            if num in hash_map:
                return [hash_map[num], i]
            
            complement = target - num
            hash_map[complement] = i


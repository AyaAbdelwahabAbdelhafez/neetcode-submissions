class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seens={}
        for i, num in enumerate(nums):
            if target-num in seens:
                return [seens[target-num],i]
            else:
                seens[num]=i

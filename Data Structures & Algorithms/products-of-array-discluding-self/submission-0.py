class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = 1
        post = 1
        out = []
        size = len(nums)

        for i in range(size):
            out.append(pre)
            pre *= nums[i]

        for j in range(size - 1, -1, -1):
            out[j] *= post
            post *= nums[j]

        return out
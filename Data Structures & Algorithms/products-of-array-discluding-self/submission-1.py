class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1]*len(nums)
        for i in range(len(output)-1):
            output[i+1] = output[i]*nums[i]
        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            output[i] = output[i] * postfix
            postfix = postfix*nums[i]
        return output

       
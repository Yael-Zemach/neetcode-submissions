class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        idx = -1
        flag = False
        output = [0]*len(nums)
        for index, num in enumerate(nums):
            if num != 0:
                product = product * num   
            elif not flag: 
                    idx = index
                    flag = True# flag = false
            else:
                idx = -1
        if idx == -1 and flag:
            return output
        if flag:
            output[idx] = product
            return output
        for index, num in enumerate(nums):
            output[index] =  product// nums[index]
        return output


        

        
            
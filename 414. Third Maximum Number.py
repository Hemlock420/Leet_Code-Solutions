class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums=list(set(nums))
        if len(nums)<3:
            return max(nums)
        else:
            nums.sort(reverse=True)
            return nums[2]
        
        
            
        

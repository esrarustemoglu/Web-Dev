def centered_average(nums):
    total_sum = sum(nums) - max(nums) - min(nums)
    
    count = len(nums) - 2
    return total_sum // count
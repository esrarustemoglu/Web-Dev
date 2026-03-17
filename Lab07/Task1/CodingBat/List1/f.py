def rotate_left3(nums):
  if len(nums) == 0:
    return nums
  return nums[1:] + nums[:1]
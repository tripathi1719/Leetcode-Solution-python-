#Time:O(n)
#Space:O(1)
class Solution:
  def minimumReplacement(self, nums: List[int]) -> int:
    res = 0

    max = nums[-1]
    for i in range(len(nums) - 2, -1, -1):
      ans = (nums[i] - 1) // max
      res += ans
      max = nums[i] // (ans + 1)

    return res

#Time:O(n)
#Space:O(n)
class Solution:
  def minTaps(self, n: int, ranges: List[int]) -> int:
    num = [0] * (n + 1)

    for i, range_ in enumerate(ranges):
      l = max(0, i - range_)
      r = min(n, range_ + i)
      num[l] = max(num[l], r - l)

    res = 0
    end = 0
    dis = 0

    for i in range(n):
      dis = max(dis, i + num[i])
      if i == end:
        res += 1
        end = dis

    return res if end == n else -1

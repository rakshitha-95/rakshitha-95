'''reverse intezer'''
class Solution:
  def reverse(self, x):
    ans = 0
    sign = -1 if x < 0 else 1
    x *= sign

    while x:
      ans = ans * 10 + x % 10
      x //= 10

    return 0 if ans < -2**31 or ans > 2**31 - 1 else sign * ans

x=1213
s=Solution()
print(s.reverse(x))
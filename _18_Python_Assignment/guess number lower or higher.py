class Solution:
    def guessNumber(self, n: int):
        l, r = 1, n
        while l < r:
            m = (l+r)//2
            x = guess(m)
            if x == 0:
                return m
            elif x > 0:
                l = m + 1
            else:
                r = m - 1
        return l
obj=Solution()
result=obj.guessNumber(n=9)
print(result)
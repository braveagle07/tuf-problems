class Solution:
    def largestDigit(self, n):
        return max(int(d) for d in str(abs(n)))

class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        i = 0
        if (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0):
        	isPositive = False
        else:
        	isPositive = True
        dividend = abs(dividend)
        divisor = abs(divisor)
        sum_num = divisor
        while divisor <= dividend:
        	k = 1
        	tmp = divisor
	        while tmp << 2 < dividend:
	        	k <<= 2
	        	tmp <<= 2
	        i += k
	        dividend -= tmp
        if not isPositive:
            i = -i
        if i > 2147483647:
            return 2147483647
        return i

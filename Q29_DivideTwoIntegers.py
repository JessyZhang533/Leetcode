class Solution:
    def divide_1(self, dividend: int, divisor: int) -> int:
        is_negative = (dividend < 0) != (divisor < 0)  # !!! determine sign
        divisor, dividend = abs(divisor), abs(dividend)  # calculate the quotient assuming all non-negative

        quotient = 0
        the_sum = divisor

        while the_sum <= dividend:
            current_quotient = 1
            while (the_sum + the_sum) <= dividend:  # !!! this while loop is essentially a trick to shorten operation time
                the_sum += the_sum  # essentially *2; can increase more quickly than 'the_sum += divisor'
                current_quotient += current_quotient  # essentially *2; can increase more quickly than 'current_quotient += 1'
            dividend -= the_sum
            the_sum = divisor
            quotient += current_quotient

        return min(2147483647, max(-quotient if is_negative else quotient, -2147483648))

    def divide_2(self, dividend: int, divisor: int) -> int:
        " bitwise operators https://wiki.python.org/moin/BitwiseOperators "
        is_negative = (dividend < 0) != (divisor < 0)
        divisor, dividend = abs(divisor), abs(dividend)

        quotient = 0
        the_sum = divisor

        while the_sum <= dividend:
            current_quotient = 1
            while (the_sum << 1) <= dividend:  # bitewise operator <<: essentially *2
                the_sum <<= 1
                current_quotient <<= 1
            dividend -= the_sum
            the_sum = divisor
            quotient += current_quotient

        return min(2147483647, max(-quotient if is_negative else quotient, -2147483648))

class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:

        n, remainder = divmod(abs(numerator), abs(denominator))
        sign = '-' if numerator*denominator < 0 else ''
        result = [sign+str(n), '.']
        remainders = {}  # key: remainder; value: number of digits + 1 (this is for '.')

        while remainder > 0 and remainder not in remainders:  # the second condition: once the digits start repeating (recursive decimals), exit the while loop
            remainders[remainder] = len(result)
            n, remainder = divmod(remainder*10, abs(denominator))  # calculate the next digit: remainder*10
            result.append(str(n))

        if remainder in remainders:  # for non-recursive decimals, now 'remainder'=0, and it is not in 'remainders'
            idx = remainders[remainder]
            result.insert(idx, '(')
            result.append(')')

        return ''.join(result).rstrip(".")  # .rstrip() get rid of '.' if result is an integer


# 1.rstrip(): returns a copy of the string in which all chars have been stripped from the end of the string (default whitespace characters).
# 2.divmod(num, den): returns the quotient and remainder as a tuple
# 3.join(): takes all items in an iterable and joins them into one string

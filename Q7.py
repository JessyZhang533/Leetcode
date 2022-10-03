# Reverse an integer

class Solution:
    def reverse_1(self, x: int) -> int:
        x_abs = abs(x)
        reverse = 0
        while x_abs > 0:  # Reverse an integer
            reverse = reverse * 10 + x_abs % 10
            x_abs = x_abs // 10
        if str(reverse)[0] == 0:
            for i in range(len(str(reverse))):
                if str(reverse)[i] != 0:
                    new_str = str(reverse)[i:]
                    break
            reverse = int(new_str)

        if x < 0:
            reverse = -reverse
        if reverse < -2**31 or reverse > 2**31 - 1:
            return 0
        return reverse
  
    def reverse_2(self, x):
        s = (x > 0) - (x < 0)  # Inside the parentheses: True=1, False=0
        r = int(str(x*s)[::-1])  # Use SLICING to reverse
        return s*r * (r < 2**31)

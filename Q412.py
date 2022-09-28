# Fizz Buzz
# "1-indexed list/array": first index is 1 instead of 0

class Solution:
    def fizzBuzz_1(self, n: int) -> List[str]:
        answer = [str(i) for i in range(1,n+1)]  # Read requirements. We need items in 'answer' to be strings instead of numbers
        for i in range(1,n+1):
            if i%3 == 0 and i%5 == 0:
                answer[i-1] = "FizzBuzz"  # index is i-1 because of '1-indexed'
            elif i%3 == 0:
                answer[i-1] = "Fizz"
            elif i%5 == 0:
                answer[i-1] = "Buzz"
        return answer

    # One line
    def fizzBuzz_2(self, n):
        return ['Fizz' * (not i % 3) + 'Buzz' * (not i % 5) or str(i) for i in range(1, n+1)]
    # 'for i in range(1, n+1)' concludes all stuff come before
    # multiply a string by a boolean: If the boolean == True, return the string
    # note the '+', enabling 'Fizz' + 'Buzz' = 'FizzBuzz'
    # 'not i % 3' is equivalent to i % 3 == 0

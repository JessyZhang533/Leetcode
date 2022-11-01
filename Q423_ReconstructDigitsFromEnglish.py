from collections import Counter


class Solution:
    # eg. s = "owoztneoer"
    def originalDigits(self, s: str) -> str:
        cnt = Counter(s)
        # cnt: Counter({'o': 3, 'e': 2, 'w': 1, 'z': 1, 't': 1, 'n': 1, 'r': 1})
        Digits = ["zero", "two", "four", "six", "eight", "one", "three", "five", "seven", "nine"]
        Corresp = [0, 2, 4, 6, 8, 1, 3, 5, 7, 9]  # sequence according to 'Digits'
        Counters = [Counter(digit) for digit in Digits]
        # Counters: [Counter({'z': 1, 'e': 1, 'r': 1, 'o': 1}), Counter({'t': 1, 'w': 1, 'o': 1}), Counter({'f': 1, 'o': 1, 'u': 1, 'r': 1}), Counter({'s': 1, 'i': 1, 'x': 1}), Counter({'e': 1, 'i': 1, 'g': 1, 'h': 1, 't': 1}), Counter({'o': 1, 'n': 1, 'e': 1}), Counter({'e': 2, 't': 1, 'h': 1, 'r': 1}), Counter({'f': 1, 'i': 1, 'v': 1, 'e': 1}), Counter({'e': 2, 's': 1, 'v': 1, 'n': 1}), Counter({'n': 2, 'i': 1, 'e': 1})]
        Found = [0]*10
        for it, C in enumerate(Counters):
            k = min(cnt[x]//C[x] for x in C)  # x is a key, cnt and C are dictionaries: one created using 's', the other created using English words of numbers
            # k is the frequency of number 'it' in the string 's'
            for i in C.keys():  # C.keys() is a collection of letters of word zero or one or two or...or nine
                C[i] *= k
            cnt -= C  # !!! operation between dictionaries
            Found[Corresp[it]] = k

        return "".join([str(i)*Found[i] for i in range(10)])
        # str(i): need to convert the digit (0, 1, 2...or 9) to a string
        # *Found[i]: multiplied by the frquency ofthat digit
        # !!!: .join()

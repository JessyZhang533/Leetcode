# Count Binary Substrings

# First, I count the number of 1 or 0 grouped consecutively.
# For example "0110001111" will be [1, 2, 3, 4].

# Second, for any possible substrings with 1 and 0 grouped consecutively, the number of valid substring will be the minimum number of 0 and 1.
# For example "0001111", will be min(3, 4) = 3, ("01", "0011", "000111")

# For "01": we have 01 --> 1 substring
# For "0011": we have 01, 0011 --> 2 substrings
# For "000111": we have 01, 0011, 000111 --> 3 substrings
# ...

def detectCapitalUse(self, s):
    """
    :type word: str
    :rtype: bool
    """
    l = []
    for i in s.replace("01", "0 1").replace("10", "1 0").split():  # First
        l.append(len(i))
    return sum(min(a, b) for a, b in zip(l, l[1:]))  # Second

# zip(a, b): join items in a with items in b

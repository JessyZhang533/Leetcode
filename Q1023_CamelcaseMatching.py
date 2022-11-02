class Solution:
    # Design a function that checks if a word matches a pattern; then apply it to every word in queries
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        def pat_match(string, pat):  # check if all uppercase letters in the string is in 'pattern'
            j = 0  # pointer pointing at uppercase letters in 'pat'
            for i in string:
                if j < len(pat) and i == pat[j]:
                    j += 1
                elif ord('Z') >= ord(i) >= ord('A'):  # ascii table: https://www.rapidtables.com/code/text/ascii-table.html all uppercase letters are before lowercase ones
                    return False
            return  j == len(pat) 

        res = []
        for i in queries:
            res.append(pat_match(i, pattern))
        return res

# Longest substring without repeating characters
# example: pwwkew --> wke
# example: abcad --> bcad

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # !!! use dic
        used = {}
        # max_length: the maximum length of the substring known existed
        # start: the start of the current substring
        max_length = start = 0
        for i, c in enumerate(s):  # enumerate can be used on strings (apart from lists
            if c in used and start <= used[c]:  # if 'start' is after user[c], then c shold be included into the current substring (move on to 'else')
                start = used[c] + 1
            else:
                max_length = max(max_length, i - start + 1)  # i-start+1 is the length of the current growing substring
            used[c] = i  # if we encounter a repeated character as before, this line OVERWRITES the 'value'(index) associated with the 'key'(character)
        return max_length


solution = Solution()
print(solution.lengthOfLongestSubstring("tmmzuxt"))

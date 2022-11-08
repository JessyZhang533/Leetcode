# Group anagrams

from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        letters_to_words = defaultdict(list)
        for word in strs:
            letters_to_words[tuple(sorted(word))].append(word)  # 'tuple(sorted(word))' is a tuple of separate letters; need to convert to tuples because it is hashable but lists are not
        return list(letters_to_words.values())

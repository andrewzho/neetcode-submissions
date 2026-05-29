class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_dictionary = dict()
        for i in strs:
            value = ''.join(sorted(i))
            if value in word_dictionary.keys():
                word_dictionary[value].append(i)
            else:
                word_dictionary[value] = [i]
        return list(word_dictionary.values())
        
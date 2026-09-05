class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        groups = {}

        for word in strs:

            # Create a unique signature for all anagrams
            key = ''.join(sorted(word))

            # Create a new list if key doesn't exist
            if key not in groups:
                groups[key] = []

            # Add the word to its anagram group
            groups[key].append(word)

        # Return all grouped values
        return list(groups.values())
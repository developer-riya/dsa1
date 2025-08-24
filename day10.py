from collections import defaultdict

def groupAnagrams(strs):
    anagram_map = defaultdict(list)   # dictionary with list as default value
    
    for word in strs:
        # Sort word to form key
        sorted_word = ''.join(sorted(word))
        anagram_map[sorted_word].append(word)
    
    # Return grouped anagrams
    return list(anagram_map.values())

# Example usage
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(groupAnagrams(strs))
[['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]

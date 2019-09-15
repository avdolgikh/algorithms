
# O(nlogn) in worst case

def createWordMap(word):
    word_map = {}
    for s in word:
        if s in word_map:
            word_map[s] += 1
        else:
            word_map[s] = 1
    return word_map

class Solution(object):    
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        result = []    
        maps = []
        for word in strs:
            word_map = createWordMap(word)
            is_new_map = True
            for i in range(len(maps)):
                if maps[i] == word_map:
                    result[i].append(word)
                    is_new_map = False
                    break
            if is_new_map:
                maps.append(word_map)
                result.append([word])
        return result


# ==============================

# Faster:
# O()
class Solution(object):    
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        result = []    
        maps = {}
        for word in strs:
            w = str(sorted(word))
            if w in maps:
                result[maps[w]].append(word)
            else:
                result.append([word])
                maps[w] = len(result) - 1
        return result
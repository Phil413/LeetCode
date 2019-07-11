class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        words_map = {}
        result = []
        if not s or not words or len(words)*len(words[0]) > len(s):
        	return result
        words_len = len(words[0])
        for i in words:
        	words_map[i] = words_map.get(i, 0) + 1

        for i in range(0, words_len):
        	tmp_map = {}
        	left = i
        	count = 0
        	for j in range(i, len(s)-words_len+1, words_len):
        		word = s[j:j+words_len]
        		if word in words_map:
        			tmp_map[word] = tmp_map.get(word, 0) + 1
        			if tmp_map[word] <= words_map[word]:
        				count += 1
        			else:
        				count += 1
        				while tmp_map[word] > words_map[word]:
        					tmp_word = s[left:left+words_len]
        					tmp_map[tmp_word] -= 1
        					left += words_len
        					count -= 1

        			if count == len(words):
        				result.append(left)
        				tmp_word = s[left:left+words_len]
        				tmp_map[tmp_word] -= 1
        				count -= 1
        				left += words_len
        		else:
        			tmp_map = {}
        			count = 0
        			left = j + words_len
        		# print (left, j, word, count, tmp_map)
        return result

if __name__ == "__main__":
	sl = Solution()
	print (sl.findSubstring("wordgoodgoodgoodbestword", ["word","good","best","good"]))
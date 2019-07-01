class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_len = 0
        begin = 0
        ascii_map = {}
        i = 0
        for i in range(len(s)):
        	char_s = s[i]
        	if i > ascii_map.get(char_s, -1) >= begin:
        		max_len = max(max_len, i-begin)
        		begin = ascii_map[char_s] + 1
        		ascii_map[char_s] = i
        	ascii_map[char_s] = i
        	i += 1
        max_len = max(max_len, i-begin)
        return max_len
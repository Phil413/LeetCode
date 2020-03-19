class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_num = 0
        curry_num = 0
        parenthese_stack = list()
        for i, e in enumerate(s):
            if e == '(':
                parenthese_stack.append((i, e))
            else:
                if parenthese_stack:
                    if parenthese_stack[-1][1] == "(":
                        parenthese_stack.pop()
                        if parenthese_stack:
                            curry_num = i - parenthese_stack[-1][0]
                        else:
                            curry_num = i + 1
                        max_num = max(max_num, curry_num)
                    else:
                        parenthese_stack.append((i, e))
                else:
                    parenthese_stack.append((i, e))
        return max_num

    def longestValidParentheses2(self, s):
        max_num = 0
        s_len = len(s)
        max_i = {s_len-1: 0}
        for i in range(s_len-2, -1, -1):
            if s[i] == "(" and i+1+max_i[i+1] < s_len and s[i+1+max_i[i+1]] == ")":
                max_i[i] = max_i[i+1] + 2
                if (i+2+max_i[i+1] < s_len):
                    max_i[i] += max_i[i+2+max_i[i+1]]
                max_num = max(max_num, max_i[i])
            else:
                max_i[i] = 0
        return max_num


if __name__ == "__main__":
    sl = Solution()
    print(sl.longestValidParentheses2("()(()"))  # ()(()  )()())
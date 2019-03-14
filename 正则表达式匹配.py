# -*- coding:utf-8 -*-
class Solution:
    # s, pattern都是字符串
    def match(self, s, pattern):
        if not s and not pattern:
            return True
        if s and not pattern:
            return False
        # pattern[1]等于*的情况
        if len(pattern) > 1 and pattern[1] == '*':
            # s对应位置上有相等的元素
            if len(s) > 0 and (s[0] == pattern[0] or pattern[0] == '.'):
                # 1）匹配一个后继续匹配
                # 2）虽然有相等元素，但是不进行匹配，因为*之前的元素可以没出现
                return self.match(s[1:], pattern) or self.match(s, pattern[2:])
            # s为空，或者s对应位置没有相等的元素，只能不进行匹配跳过
            else:
                return self.match(s, pattern[2:])

        if len(s) > 0 and (s[0] == pattern[0] or pattern[0] == '.'):
            return self.match(s[1:], pattern[1:])
        return False


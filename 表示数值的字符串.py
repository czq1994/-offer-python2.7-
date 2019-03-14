# -*- coding:utf-8 -*-
import re
class Solution:
    # s字符串
    def isNumeric(self, s):
        # write code here
        if not s:
            return False
        return re.match('^[\+\-]?[0-9]*(\.[0-9]*)?([Ee][\+\-]?[0-9]+)?$', s)
        #return re.match(r'^[\+\-]?[0-9]*(\.[0-9]*)?([Ee][\+\-]?[0-9]+)?$', s)
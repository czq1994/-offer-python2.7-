# -*- coding:utf-8 -*-
class Solution:
    
    def GetLeastNumbers_Solution(self, tinput, k):
        length = len(tinput)
        ls = []
        if k == length:
            return sorted(tinput)
        if k > length or k < 1 or length <= 0:
            return []
        for i in range(length):

            if i < k:
                ls.append(tinput[i])
                if i == k - 1:  # 此时正好k个元素，开始初始化最大堆
                    start = (0 + i) // 2
                    for j in range(start, -1, -1):
                        print(j)
                        self.heap_once(ls, j, k - 1)
                        print(ls)
            else:
                if tinput[i] < ls[0]:
                    ls[0] = tinput[i]
                    self.heap_once(ls, 0, k - 1)
                else:
                    pass
        return sorted(ls)

    def heap_once(self, ls, start, end):
        i = start
        save = ls[start]
        j = i * 2 + 1
        while j <= end:
            print(j)
            if j + 1 <= end and ls[j + 1] > ls[j]:
                j += 1
            if ls[i] < ls[j]:
                ls[i], ls[j] = ls[j], ls[i]
                i = j
                j = 2 * j + 1
            else:
                break
        # ls[i] = save
# -*- coding:utf-8 -*-
# heapq.heappush(heap, num) #将num插入heap，并维持堆的数据结构
# heapq.heappop(heap) #弹出堆顶，即最小元素，注意是弹出，
# a = heap[0] #取得堆顶，不弹出
import heapq  # python 最小堆


class Solution:
    def __init__(self):
        self.maxheap = []
        self.minheap = []
        self.count = 0

    def Insert(self, num):
        self.count += 1
        if self.count == 1:
            heapq.heappush(self.maxheap, -num)
        elif self.count == 2:
            if num < -self.maxheap[0]:
                val = -heapq.heappop(self.maxheap)
                heapq.heappush(self.minheap, val)
                heapq.heappush(self.maxheap, -num)
            else:
                heapq.heappush(self.minheap, num)
        else:
            if self.count & 1 == 1:  # 奇数,放到最大堆里
                if num > self.minheap[0]:
                    val = heapq.heappop(self.minheap)
                    heapq.heappush(self.maxheap, -val)
                    heapq.heappush(self.minheap, num)
                else:
                    heapq.heappush(self.maxheap, -num)
            else:  # 偶数，放到最小堆里
                if num < -self.maxheap[0]:
                    val = -heapq.heappop(self.maxheap)
                    heapq.heappush(self.minheap, val)
                    heapq.heappush(self.maxheap, -num)
                else:
                    heapq.heappush(self.minheap, num)

    def GetMedian(self, n=None):
        # write code here
        if self.count & 1 == 1:
            return -self.maxheap[0]
        else:
            return (self.minheap[0] - self.maxheap[0]) / 2.0


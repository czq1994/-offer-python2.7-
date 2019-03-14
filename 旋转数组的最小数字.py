class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        if not rotateArray:
            return 0
        low = 0
        high = len(rotateArray) - 1
        while rotateArray[low] >= rotateArray[high]:
            if high - low <= 1:
                return rotateArray[high]
            mid = (high + low) // 2
            if rotateArray[high] == rotateArray[low] and rotateArray[mid] == rotateArray[low]:
                return self.normal_find(rotateArray)
            # 左边为有序，在右边寻找转折点（最小数）
            if rotateArray[mid] >= rotateArray[low]:
                low = mid
            # 右边为有序，在左边寻找转折点（最小数）
            elif rotateArray[mid] <= rotateArray[high]:
                high = mid

    def normal_find(self, rotateArray):
        # write code here
        if len(rotateArray) == 0:
            return 0
        for i in range(1, len(rotateArray) - 1):
            if rotateArray[i - 1] <= rotateArray[i] <= rotateArray[i + 1]:
                pass
            else:
                return rotateArray[i + 1]
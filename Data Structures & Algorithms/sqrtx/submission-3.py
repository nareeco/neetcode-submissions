class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x
        while left <= right:
            mid = (left + right) // 2
            result = mid * mid
            if result <= x:
                answer = mid
            if result == x:
                return mid
            if result < x:
                left = mid + 1
            else:
                right = mid -1

        return answer

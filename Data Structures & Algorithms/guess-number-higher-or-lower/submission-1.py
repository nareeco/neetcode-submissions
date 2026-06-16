# The guess API is already defined for you.
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        low = 1
        high = n

        while low <= high:
            mid = (low + high) // 2

            guess_result = guess(mid)
            if guess_result > 0:
                low = mid + 1
            elif guess_result < 0:
                high = mid - 1
            else:
                return mid
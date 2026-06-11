class Solution:
    def validPalindrome(self, s: str) -> bool:
        s = "".join(char.lower() for char in s if char.isalnum())
        def is_pali(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        l, r = 0, len(s) - 1

        while l < r:
            if s[l] != s[r]:
                # try skipping left OR right
                return is_pali(l + 1, r) or is_pali(l, r - 1)
            l += 1
            r -= 1

        return True
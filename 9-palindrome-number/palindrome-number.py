class Solution:
    def isPalindrome(self, x: int) -> bool:
        xStr = str(x)
        start = 0
        end = len(xStr) - 1
        for i in range((len(xStr) + 1) // 2):
            if xStr[start] != xStr[end]:
                return False
            start += 1
            end -= 1
        return True

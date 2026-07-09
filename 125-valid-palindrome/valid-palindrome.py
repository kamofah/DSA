class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphaS = ""
        for i in s.lower():
            if i.isalnum():
                alphaS += i

        start = 0
        end = len(alphaS) - 1
        for i in range((len(alphaS) + 1) // 2):
            if alphaS[start] != alphaS[end]:
                return False
            start += 1
            end -= 1
        return True 


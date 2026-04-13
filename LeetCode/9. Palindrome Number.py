class Solution:
    def isPalindrome(self, x: int) -> bool:
        out=" "
        xs=str(x)
        rev=xs[::-1]
        if xs==rev:
            return True
        else:
            return False

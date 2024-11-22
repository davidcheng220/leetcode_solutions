class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_x = str(x)
        reverse_x = str_x[::-1]
        if reverse_x == str_x:
            return True
        else:
            return False
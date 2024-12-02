#  Wrong solution because it is not a sequence
# class Solution:
#     def isSubsequence(self, s: str, t: str) -> bool:
#         count = 0
#         if s == "":
#             return True
            
#         while count <= len(s):
#             for i in s:
#                 if i in t:
#                     count += 1
#                 else:
#                     return False
#         return True

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        countS = countT = 0
        if s == "":
            return True

        while countS < len(s) and countT < len(t):
            if s[countS] == t[countT]:
                countS += 1
            countT += 1
        
        return countS == len(s)
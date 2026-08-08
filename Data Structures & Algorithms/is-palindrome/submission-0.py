class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        head = 0
        tail = len(s)-1
        while head < tail:
            if not s[head].isalnum():
                head += 1
                continue
            if not s[tail].isalnum():
                tail -= 1
                continue
            if s[head] != s[tail]:
                return False
            else:
                head += 1
                tail -= 1
        return True
            
            
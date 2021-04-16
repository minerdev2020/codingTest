class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        for l in range(length, 0, -1):
            for start in range(length - l + 1):
                end = start + l
                mid = (start + end) // 2
                if l % 2 == 0 and s[start:mid] == s[mid:end][::-1]:
                    return s[start:end]
                
                elif l % 2 == 1 and s[start:mid] == s[mid + 1:end][::-1]:
                    return s[start:end]
        
solution = Solution()
print(solution.longestPalindrome("a"))
print(solution.longestPalindrome("ac"))
print(solution.longestPalindrome("babad"))
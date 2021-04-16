class Solution:
    # 내 풀이
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
                
    # 다른 사람의 풀이 (다이내믹 프로그래밍)
    def checkPalindrome(self, s, mid, odd = True):
        left = mid - 1 if odd else mid
        right = mid + 1
        length = len(s)
        while left >= 0 and right < length:
            if(s[left] != s[right]):
                break
            
            left -= 1
            right += 1

        return [left + 1, right]
    
    def longestPalindrome1(self, s: str) -> str:
        longest_idx = []
        size = 0

        for idx in range(len(s)):
            odd_idx = self.checkPalindrome(s, idx)
            even_idx = self.checkPalindrome(s, idx, False)

            if even_idx[1] - even_idx[0] > size:
                longest_idx = even_idx
                size = even_idx[1] - even_idx[0]
                
            if odd_idx[1] - odd_idx[0] > size:
                longest_idx = odd_idx
                size = odd_idx[1] - odd_idx[0]

        return s[longest_idx[0]:longest_idx[1]]

solution = Solution()
print(solution.longestPalindrome("a"))
print(solution.longestPalindrome("ac"))
print(solution.longestPalindrome("babad"))

print(solution.longestPalindrome1("a"))
print(solution.longestPalindrome1("ac"))
print(solution.longestPalindrome1("babad"))
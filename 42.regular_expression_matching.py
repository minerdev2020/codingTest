class Solution:
    # 다른 사람의 풀이 1 (재귀 + 다이내믹 프로그래밍)
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}
        def dp(i, j):
            if (i, j) not in memo:           
                if j == len(p): 
                    ans = i == len(s)
                
                else:
                    first_match = i < len(s) and p[j] in {s[i], '.'}
                    if j + 1 < len(p) and p[j + 1] == '*':
                        ans = dp(i, j + 2) or first_match and dp(i + 1, j)
                        
                    else:
                        ans = first_match and dp(i + 1, j + 1)

                memo[i, j] = ans
            
            return memo[i, j]

        return dp(0, 0)
        
    # 다른 사람의 풀이 2 (단순 재귀)
    def isMatch1(self, s: str, p: str) -> bool:
        if not p: 
            return not s
        
        first_match = bool(s) and p[0] in {s[0], '.'}
        
        if len(p) >= 2 and p[1] == '*':
            return (self.isMatch(s, p[2:]) or
                    first_match and self.isMatch(s[1:], p))
            
        else:
            return first_match and self.isMatch(s[1:], p[1:])
        
solution = Solution()
# print(solution.isMatch("aa", "a"))
# print(solution.isMatch("aa", "aa"))
# print(solution.isMatch("aab", "aab"))
# print(solution.isMatch("ab", "a."))
# print(solution.isMatch("ab", ".."))
# print(solution.isMatch("a", ".."))
# print(solution.isMatch("aa", "a"))
# print(solution.isMatch("aa", "a*"))
# print(solution.isMatch("ab", "."))
# print(solution.isMatch("ab", ".*"))
# print(solution.isMatch("aab", "c*a*b"))
# print(solution.isMatch("mississippi", "mis*is*p*."))
# print(solution.isMatch("abcd", "d*"))
print(solution.isMatch("ab", ".*c"))
print(solution.isMatch("ab", ".*c.*"))
print(solution.isMatch("abcab", ".*c.*"))
print(solution.isMatch("c", ".*c.*"))
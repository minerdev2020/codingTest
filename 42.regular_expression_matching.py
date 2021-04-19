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
    # '*'가 있냐 없냐에 따라 갈린다
    # '*'가 없다면 한글자씩 오른쪽으로 이동하면서 매치
    # '*'가 있다면 해당하는 패턴이 등장하지 않았을 경우와 등장할 경우로 다시 나뉜다
    # 등장하지 않았을 경우 다음 패턴으로 넘어가 같은 글자에 계속해서 매치한다
    # 등장할 경우 같은 패턴으로 다음 글자에 계속해서 매치한다
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
def checkPalindrome(string, leftIdx, rightIdx):

	if(leftIdx > rightIdx):
		return

	while leftIdx >= 0 and rightIdx < len(string):
		if(string[leftIdx] != string[rightIdx]):
			break
		leftIdx -= 1
		rightIdx += 1

	return [leftIdx + 1, rightIdx]


class Solution:
	def longestPalindrome(self, s: str) -> str:
		longestIdx = []
		size = 0

		for idx in range(len(s)):
			oddIdx = checkPalindrome(s, idx - 1, idx + 1)
			evenIdx = checkPalindrome(s, idx - 1, idx)

			if evenIdx and evenIdx[1] - evenIdx[0] > size:
				longestIdx = evenIdx
				size = evenIdx[1] - evenIdx[0]
			if oddIdx and oddIdx[1] - oddIdx[0] > size:
				longestIdx = oddIdx
				size = oddIdx[1] - oddIdx[0]

		return s[longestIdx[0]:longestIdx[1]]

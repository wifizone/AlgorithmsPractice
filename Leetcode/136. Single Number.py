class Solution:
def singleNumber(self, nums: List[int]) -> int:
	s = {}
	count = 0
	for idx in range(len(nums)):
		s[str(nums[idx])] = idx
		if count == len(s):
			s.pop(str(nums[idx]))
			count -= 1
		else:
			count += 1
	
	return nums[int(s.popitem()[1])]
	

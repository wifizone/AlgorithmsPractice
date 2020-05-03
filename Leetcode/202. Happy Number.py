class Solution:
def isHappy(self, n: int) -> bool:
	count = 0
	s = {n}
	while count != len(s):
		sum = 0
		for digit in str(n):
			sum += int(digit)**2
		n = sum
		count += 1
		s.add(sum)
		sum = str(sum).replace("0", "")
		if str(sum) == "1":
			return True
	return False

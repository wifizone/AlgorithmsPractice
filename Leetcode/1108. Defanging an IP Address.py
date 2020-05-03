class Solution:
def defangIPaddr(self, address: str) -> str:
	newStr = []
	for idx in range(len(address)):
		if address[idx] == ".":
			newStr.append("[.]")
		else:
			newStr.append(address[idx])
	return ''.join(newStr)

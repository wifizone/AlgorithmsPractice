def search(array, value):
	low = 0
	high = len(array) - 1
	
	while(low <= high):
		mid = int((high + low) / 2)
		if array[mid] == value:
			return mid
		elif array[mid] > value:
			high = mid - 1
		else:
			low = mid + 1
	return -1


a = [1, 2, 3, 4, 5, 6, 7, 8]

print(search(a, 1))
print(search(a, 2))
print(search(a, 3))
print(search(a, 4))
print(search(a, 5))
print(search(a, 6))
print(search(a, 7))
print(search(a, 8))
print(search(a, 9))

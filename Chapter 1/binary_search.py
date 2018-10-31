class BinarySearchClass:

    @staticmethod
    def binarySearch(value, sortedArray):
        low = 0
        high = len(sortedArray) - 1

        while (high >= low):
            mid = int((high + low) / 2)
            if (value > sortedArray[mid]):
                low = mid + 1
            elif (value < sortedArray[mid]):
                high = mid - 1
            else:
                return mid

        return -1

sortedArray = [2, 6, 8, 10, 14, 18, 20, 40, 43, 49, 63, 70]

print(BinarySearchClass.binarySearch(10, sortedArray))
print(BinarySearchClass.binarySearch(65, sortedArray))
print(BinarySearchClass.binarySearch(2, sortedArray))
print(BinarySearchClass.binarySearch(63, sortedArray))
print(BinarySearchClass.binarySearch(40, sortedArray))


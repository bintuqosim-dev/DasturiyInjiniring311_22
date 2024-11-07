"""
Search, insert and delete in a sorted array
Saralangan massivda qidirish, kiritish va o'chirish
"""


class Sortedarray:
    def __init__(self):
        self.array = []


    def __str__(self):
        return str(self.array)


    def binary_search(self, target):
        low, high = 0, len(self.array) - 1
        while low <= high:
            mid = (low + high) // 2
            if self.array[mid] == target:
                return mid
            elif self.array[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        return -1


    def insert(self, *values):
        self.array.extend(values)
        self.array.sort()


    def delete(self, value):
        if value in self.array:
            self.array.remove(value)
        else:
            print(f"ELement {value} topilmadi")


sorted_array = Sortedarray()

sorted_array.insert(5, 1, 3, 7, 2)
print("saralangan massiv:", sorted_array)

index = sorted_array.binary_search(3)
print(f"Element 3 ning indeksi: {index}" if index != -1 else "Element 3 topilmadi.")

sorted_array.delete(3)
print("o'chirilgandan keyin massiv:", sorted_array)

sorted_array.delete(3)

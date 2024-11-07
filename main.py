import random
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] > right_half[j]:
                arr[k] = right_half[j]
                j += 1
            else:
                arr[k] = left_half[i]
                i += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

n = int(input("Massivga random asosida nechta son o'zlashtirishni hohlaysiz: "))
arr = [random.randint(-50, 50) for _ in range(n)]
print("Berilgan list:", arr)
merge_sort(arr)
print("Tartiblangan list:", arr[::-1])
def merge_sort(arr):
    if len(arr) < 2:
        return arr
    
    mid = len(arr)//2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)

    return merge(left_sorted, right_sorted)

def merge (left, right):
    sorted_arr = []
    left_index, right_index = 0 , 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            sorted_arr.append(left[left_index])
            left_index += 1
        else:
            sorted_arr.append(right[right_index])
            right_index += 1

    while left_index < len(left):
        sorted_arr.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        sorted_arr.append(right[right_index])
        right_index += 1


    return sorted_arr


if __name__ == "__main__":
    arr = [38, 27, 43, 3, 9, 82, 10]
    print("Array after sorting: ",merge_sort(arr))

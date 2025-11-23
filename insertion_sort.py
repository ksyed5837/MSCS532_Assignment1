def insertion_sort_desc(arr):
    # Loop through each element starting from index 1
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        # Move elements that are smaller than key to one position ahead
        # This creates a decreasing order
        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr


# Example usage
if __name__ == "__main__":
    data = [12, 4, 5, 3, 8, 7]
    print("Original array:", data)
    sorted_data = insertion_sort_desc(data)
    print("Sorted in decreasing order:", sorted_data)

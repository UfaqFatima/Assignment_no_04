def binary_search(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid  # Number found at this index
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1  # Number not found

# Main function
def main():
    print("🔍 Binary Search in Python")

    # Sorted list input
    arr = list(map(int, input("📌 Enter sorted numbers (space-separated): ").split()))
    
    # Number to search
    target = int(input("🎯 Enter number to search: "))

    # Perform Binary Search
    result = binary_search(arr, target)

    # Show result
    if result != -1:
        print(f"✅ Number {target} found at index {result}!")
    else:
        print(f"❌ Number {target} not found in the list.")

# Run the program
if __name__ == "__main__":
    main()
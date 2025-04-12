def index_game():
    my_list = ['apple', 'banana', 'orange', 'grape', 'pineapple']
    
    while True:
        print("\nOptions:")
        print("1. Access an element")
        print("2. Modify an element")
        print("3. Slice the list")
        print("4. Exit")
        
        choice = input("Select an operation (1/2/3/4): ")
        
        if choice == "1":
            try:
                index = int(input("Enter the index to access: "))
                print(f"Element at index {index}: {my_list[index]}")
            except ValueError:
                print("⚠️ Please enter a valid number!")
            except IndexError:
                print("⚠️ Index out of range! Try again.")
                        
        elif choice == "2":
            try:
                index = int(input("Enter the index to modify: "))
                new_value = input("Enter the new value: ")
                my_list[index] = new_value
                print(f"Updated list: {my_list}")
            except ValueError:
                print("⚠️ Please enter a valid number!")
            except IndexError:
                print("⚠️ Index out of range! Try again.")

        elif choice == "3":
            try:
                start = int(input("Enter the start index: "))
                end = int(input("Enter the end index: "))
                print(f"Sliced list: {my_list[start:end]}")
            except ValueError:
                print("⚠️ Please enter valid numbers for slicing!")
        
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("⚠️ Invalid choice! Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    index_game()
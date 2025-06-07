shopping_list = []

while True:
    print("\nShopping List Manager")
    print("1. Add an item")
    print("2. Remove an item")
    print("3. View the list")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")
    
    if choice == "1":
        item = input("Enter item to add: ")
        shopping_list.append(item)
        print(f"{item} added to the list.")
    elif choice == "2":
        item = input("Enter item to remove: ")
        if item in shopping_list:
            shopping_list.remove(item)
            print(f"{item} removed from the list.")
        else:
            print(f"{item} not found in the list.")
    elif choice == "3":
        if shopping_list:
            print("\nYour shopping list:")
            for item in shopping_list:
                print(f"- {item}")
        else:
            print("Your shopping list is empty.")
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")
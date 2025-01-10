# Initialize the balance to 0
balance = 0

#
print("""
=====================================================================================================================
██╗   ██╗███████╗███╗   ██╗██████╗ ██╗███╗   ██╗ ██████╗     ███╗   ███╗ █████╗  ██████╗██╗  ██╗██╗███╗   ██╗███████╗
██║   ██║██╔════╝████╗  ██║██╔══██╗██║████╗  ██║██╔════╝     ████╗ ████║██╔══██╗██╔════╝██║  ██║██║████╗  ██║██╔════╝
██║   ██║█████╗  ██╔██╗ ██║██║  ██║██║██╔██╗ ██║██║  ███╗    ██╔████╔██║███████║██║     ███████║██║██╔██╗ ██║█████╗  
╚██╗ ██╔╝██╔══╝  ██║╚██╗██║██║  ██║██║██║╚██╗██║██║   ██║    ██║╚██╔╝██║██╔══██║██║     ██╔══██║██║██║╚██╗██║██╔══╝  
 ╚████╔╝ ███████╗██║ ╚████║██████╔╝██║██║ ╚████║╚██████╔╝    ██║ ╚═╝ ██║██║  ██║╚██████╗██║  ██║██║██║ ╚████║███████╗
  ╚═══╝  ╚══════╝╚═╝  ╚═══╝╚═════╝ ╚═╝╚═╝  ╚═══╝ ╚═════╝     ╚═╝     ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝╚══════╝
=====================================================================================================================

⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣿⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⣿⡿⠿⢿⣿⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣿⠀⠀⢠⣤⠀⠀⣴⠀⠀⠀⠀⠀⣿⠀⣶⠀⣿⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣿⠀⠰⠾⠿⠶⠾⠿⠶⠶⠶⠶⠀⣿⣀⣉⣀⣿⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⢀⣤⡀⠀⠀⣿⣏⣉⣹⣿⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣿⠀⠐⠒⠒⠒⠒⠒⠚⠛⠓⠒⠀⣿⣯⣉⣹⣿⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣿⠀⠀⢠⡀⠀⣾⠀⠀⣶⡆⠀⠀⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣿⠀⠘⠛⠛⠛⠛⠛⠛⠛⠛⠛⠀⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣿⠀⠀⣶⣦⠀⣶⣶⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣿⠀⠈⠉⠉⠉⠉⠉⠉⠉⠉⠉⠀⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣏⣉⣹⣿⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣿⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⠶⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣿⠀⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⡄⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣿⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
              """)

# Define a list of items available in the vending machine with their ID, name, and price
items_list = [
    {"id": 1, "name": "Water", "price": 1.00},
    {"id": 2, "name": "Chuckie Milk", "price": 2.00},
    {"id": 3, "name": "Mountain Dew", "price": 3.00},
    {"id": 4, "name": "Sprite", "price": 2.50},
    {"id": 5, "name": "Yakult", "price": 2.50},
    {"id": 6, "name": "Oreo", "price": 2.00},
    {"id": 7, "name": "Mars", "price": 1.50},
    {"id": 8, "name": "Bounty", "price": 1.00},
    {"id": 9, "name": "M&M", "price": 2.50},
    {"id": 10,"name": "Lays", "price": 4.00}
]

# List to track items purchased by the user
purchased_items = []

# Function to display available items
def show_items():
    # Print a header for the item list
    print("\n=== Available Snacks & Drinks ===")
    # Loop through the items list and display each item
    for item in items_list:
        print(f"{item['id']}. {item['name']} - ${item['price']:.2f}")
    print()

# Function to handle money insertion
def insert_money(balance):
    # Continuously prompt the user until a valid amount is inserted
    while True:
        try:
            # Ask the user to insert money
            amount = float(input("Insert money: $"))

            # Check if the inserted amount is valid
            if amount > 0:
                # Add the amount to the balance
                balance += amount
                # Display the inserted amount and updated balance
                print(f"Money inserted: ${amount:.2f}")
                print(f"Current balance: ${balance:.2f}")
                break
            else:
                # Inform the user that the amount must be greater than zero
                print("Please insert a valid amount greater than zero.")
        except ValueError:
            # Handle invalid numeric input
            print("Invalid input. Please enter a numeric value.")
    return balance

# Function to select an item from the vending machine
def select_item(balance):
    # Show available items to the user
    show_items()

    while True:
        try:
            # Prompt the user to select an item by its ID
            choice = int(input("Select an item by number (1-10): "))

            # Find the item in the list using the entered ID
            item = next((i for i in items_list if i["id"] == choice), None)

            if item:
                # Extract the name and price of the selected item
                name, price = item["name"], item["price"]

                # Check if the user has enough balance
                if balance >= price:
                    # Deduct the item's price from the balance
                    balance -= price
                    # Add the item to the purchased items list
                    purchased_items.append(item)
                    # Dispense the item and show the remaining balance
                    print(f"\nDispensing {name}...")
                    print(f"Remaining balance: ${balance:.2f}")
                else:
                    # Inform the user about insufficient funds and prompt for additional cash
                    print(f"\nInsufficient funds! {name} costs ${price:.2f}, but you only have ${balance:.2f}.")
                    add_cash = input("Would you like to insert more cash? (y/n): ").lower()
                    if add_cash == 'y':
                        balance = insert_money(balance)
                    else:
                        # Exit the selection process if no more cash is added
                        print("Returning to main menu.")
                        break
                break
            else:
                # Handle invalid item selection
                print("Invalid selection. Please choose a number between 1 and 10.")
        except ValueError:
            # Handle invalid numeric input
            print("Invalid input. Please enter a number between 1 and 10.")

    return balance

# Function to print a receipt of purchased items
def print_receipt():
    # Check if any items were purchased
    if purchased_items:
        # Print the receipt header
        print("\n=== Receipt ===")
        total_spent = 0
        # Loop through purchased items and display them
        for item in purchased_items:
            print(f"{item['name']} - ${item['price']:.2f}")
            total_spent += item['price']
        # Display the total amount spent
        print(f"Total spent: ${total_spent:.2f}")
    else:
        # Inform the user if no items were purchased
        print("\nNo items purchased.")

# Main function to simulate the vending machine operation
def vending_machine():
    global balance

    # Show items as a menu before starting
    show_items()

    while True:
        # Prompt the user to add money if the balance is zero
        if balance == 0:
            balance = insert_money(balance)

        # Allow the user to select an item
        balance = select_item(balance)

        while True:
            # Ask if the user wants to make another purchase
            continue_choice = input("\nWould you like to make another purchase? (y/n): ").lower()
            if continue_choice == 'y':
                # Continue to another purchase
                break
            elif continue_choice == 'n':
                # Print a receipt and exit the vending machine
                print_receipt()
                print(f"\nThank you for using the vending machine. Your change is ${balance:.2f}. ")
                return
            else:
                # Handle invalid input for the choice
                print("Invalid input. Please enter 'y' or 'n'.")
                continue  # Ensures it prompts again for a valid input

# Start the vending machine simulation
vending_machine()
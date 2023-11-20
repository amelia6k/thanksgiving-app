# Make planning for your Thanksgiving dinner easy! Log your expenses here!


my_string = ""
spending = 0
while True:
    print("Lets get started!")
    num_cat = int(input("How many categories of expenses would you like to budget?: "))
    for i in range(num_cat):
        cat_name = input("Enter a category: ")
        num_items = int(input("How many items would you like to record in " + str(cat_name) + "?: "))
        for i in range(num_items):
            item_name = input("Enter an item name: ")
            item_price = float(input("And the price?: $"))
            my_string = my_string + " " + item_name + ","
            spending = spending + item_price
        print("Items so far: " + str(my_string))
    print("In total, you have " + str(num_cat) + " categories.")
    print("Your items are " + str(my_string))
    print("Your total spending is " + str(spending))
    needed = input("Would you like to continue budgeting assistance? (Y/N/IDK):")
    if needed == "N":
        break
    if needed == "IDK":
        print("You can never budget too much!")
        continue
print("Have a great Thanksgiving!")
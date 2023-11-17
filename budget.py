# Make planning for your Thanksgiving dinner easy! Log your expenses here!

needed = input("Would you like budgeting assistance? (Y/N): ")
my_string = ""

while needed == "Y":
    print("Great! Lets get started")
    num_cat = int(input("How many categories of expenses would you like to budget?: "))
    for i in range(num_cat):
        cat_name = input("Enter a category: ")
        num_items = int(input("How many items would you like to record in " + str(cat_name) + "?: "))
        for i in range(num_items):
            item_name = input("Enter an item name: ")
            item_price = float(input("And the price?: $"))
            my_string = my_string + item_name

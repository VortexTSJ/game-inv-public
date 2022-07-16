import csv

# The function which display the inventory


def display_inventory(inventory):

    print("Your inventory contains the following:\n")

    for item in inventory:
        print(f"{item}:{inventory[item]}")

    print("\n")


# The starting inventory

inv = {"arrow": 12, "gold coin": 42, "rope": 1, "torch": 6,
       "dagger": 1}


# Function to add items to the inventory

def add_to_inventory(inventory, added_items):

    # create new item in inventory if not present yet
    for new_item in added_items:
        if new_item not in inventory:
            inventory.update({new_item: 0})

    # add items to the inventory
    for item in inventory:
        for new_item in dragon_loot:
            if item == new_item:
                inventory[item] += 1


# new stack of items

dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby',]

add_to_inventory(inv, dragon_loot)
display_inventory(inv)


# function which adds all the items and their number in a table

def print_table(inventory, order=None):

   # max_item_n#ame = max(len(it) for it in inv)

    print("-----------------\n")
    print("item name | count\n")
    print("-----------------\n")

    # sorting values ascending
    if order == "count, asc":
        inventory = sorted(inventory.items(), key=lambda count: count[1])
        inventory = dict(inventory)

    # sorting values descending
    if order == "count, desc":
        inventory = sorted(inventory.items(),
                           key=lambda count: count[1], reverse=True)
        inventory = dict(inventory)

    # creating the table rows
    for i, c in inventory.items():
        print(f"{i:>9} |  {c:>4}\n")
        # print("".join(i.ljust(max_item_name) for c in i))

    print("-----------------\n")


print_table(inv, "count, desc")


# function which updates the inventory from a file with items

def import_inventory(inventory, filename="import_inventory.csv"):

    items_from_file = []

    # creating a list of items from the file
    f = open(filename, "r")
    file_line = f.readlines()
    for it in file_line:
        list_from_file_items = it.split(",")
        for item in list_from_file_items:
            items_from_file.append(item)

    # if new item is found, add it to the inventory
    for item_f in items_from_file:
        if item_f not in inventory:
            inventory.update({item_f: 0})

    # when item found in list from file, increase it's number in the inventory
    for item in inventory:
        for item_f in items_from_file:
            if item == item_f:
                inventory[item] += 1


# importing new items from the test_inventory file
import_inventory(inv, "test_inventory.csv")


# printing the table with the updated data
print_table(inv, "count, desc")


# creating a list with all the values from the inventory
list_values_inv = list(inv.values())

# creating a list with all the keys from the inventory
list_key_inv = list(inv)


# functions which exports all the items and values from the inventory to a csv file

def export_inventory(inventory, filename="export_inventory.csv"):

    with open("export_inventory.csv", mode="w") as items_export_file:

        # creating template format for the csv file with exported inventory
        fieldnames = ["item_name", "number_of_items"]

        # settings for the file whhere the inventory data is exported
        items_to_write = csv.DictWriter(
            items_export_file, fieldnames=fieldnames)

        # loop which creates a row for each item in the inventory
        i = 0
        while i < len(list_key_inv):
            items_to_write.writerow(
                {"item_name": list_key_inv[i], "number_of_items": list_values_inv[i]})
            i += 1


export_inventory(inv)
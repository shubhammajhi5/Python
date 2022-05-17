# function to display the inventory
def displayInventory(inventory):

    print('Inventory :')
    totalItem = 0
    for item, quantity in inventory.items():
        print(quantity, item)
        totalItem += quantity

    print('Total number of items :', totalItem, '\n')


# function to add new items
def addToInventory(inventory, addedItems):
    for item in addedItems:
        inventory.setdefault(item, 0)
        inventory[item] += 1

    return inventory


# items list in the inventory along with their quantity
stuff = {
    'rope' : 1,
    'torch' : 6,
    'gold coin' : 42,
    'dagger' : 1,
    'arrow' : 12
}

# new items to be added
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

displayInventory(stuff)
stuff = addToInventory(stuff, dragonLoot)    #adding new items
displayInventory(stuff)
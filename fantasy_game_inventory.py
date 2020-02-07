#fantasy game inventory

inventory = { 'arrow': 12,
            'gold coin': 42,
            'rope': 1,
            'torch': 6,
            'dagger': 1 }

def displayInventory(inventory):
    print('Inventory:')
    for k, v in inventory.items():
        print(k + ':' + str(v))

displayInventory(inventory)
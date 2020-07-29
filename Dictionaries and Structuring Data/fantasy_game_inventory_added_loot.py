def display_inventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(v,k)
        item_total += v
    print("Total number of items:", item_total)


def add_to_inventory(inventory, added_items):
    for i in added_items:
        inventory.setdefault(i,0)
        inventory[i] += 1
        
stuff = {'gold coin': 42, 'rope': 1}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

add_to_inventory(stuff, dragon_loot)
display_inventory(stuff)

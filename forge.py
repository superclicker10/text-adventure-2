from inventory import *

rarity_names = ["minimum",
    "pitiful",
    "bad",
    "subpar",
    "normal",
    "good",
    "epic",
    "legendary",
    "perfect"]

book_rarity_names = ["minimum",
    "blank",
    "overrated",
    "bad",
    "normal",
    "knowledgeable",
    "intellectual",
    "philosophical",
    "wisdom"
]

book_requirements = {"minimum": 2,
    "blank": 2,
    "overrated": 3,
    "bad": 2,
    "normal": 2,
    "knowledgeable": 2,
    "intellectual": 3,
    "philosophical": 5,
    "wisdom": 10
}

requirements = {
    "minimum": 2,
    "pitiful": 2,
    "bad": 2,
    "subpar": 2,
    "normal": 2,
    "good": 2,
    "epic": 3,
    "legendary": 5,
    "perfect": 10
}

def merge_items(item, rarity, amount, n):
    if item == "book":
        for temp in range(0, len(book_rarity_names)):
            if book_rarity_names[temp] == rarity:
                pos = temp
                break
    else:
        for temp in range(0, len(rarity_names)):
            if rarity_names[temp] == rarity:
                pos = temp
                break
    if item == "book":
        rarity_to_merge = book_rarity_names[pos+1]
        temp1 = Inventory.inventory[f'{rarity} {item}']
        temp2 = amount*book_requirements[rarity_to_merge]
    else:
        rarity_to_merge = rarity_names[pos+1]
        temp1 = Inventory.inventory[f'{rarity} {item}']
        temp2 = amount*requirements[rarity_to_merge] 
    if temp1 < temp2:      #add requirements for merging
        print(f"You don't have enough of that item to merge it (have {temp1}, need {temp2})")
        t.sleep(n)
        return 0
    
    if item == "book":
        Inventory.inventory[f'{rarity} {item}'] -= amount*book_requirements[rarity_to_merge]  
    else:          
        Inventory.inventory[f'{rarity} {item}'] -= amount*requirements[rarity_to_merge]
    if Inventory.inventory[f'{rarity} {item}'] <= 0:
        Inventory.inventory.pop(f'{rarity} {item}')
    if item == "book":
        print(f'Merged into {amount} {book_rarity_names[pos+1]} {item}!')
        t.sleep(n)
        add_item(item, book_rarity_names[pos+1], amount, n)
    else:
        print(f'Merged into {amount} {rarity_names[pos+1]} {item}!')
        t.sleep(n)
        add_item(item, rarity_names[pos+1], amount, n)
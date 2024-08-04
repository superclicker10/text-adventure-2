from inventory import *
from lootgeneration import *
from cellcreation import *
from mainscript import * 
import time as t
import random as r
import math as m

loot_names = {
    "hp_pot": "Health potion",
    "mn_pot": "Mana potion",
    "book": "Book",
    "max_health": "Max Health",
    "max_mana": "Max Mana",
    "attack": "Attack",
    "defence": "Defence"
    }

valid_items = [ #valid sellable items
    "health potion",
    "mana potion",
    "book",
    "scrap"
]

pots = [
    "hp_pot",
    "mn_pot"
]

other = [
    "book",
    "scrap"
]

misc = [
    "max_health",
    "max_mana",
    "attack",
    "defence"
]

rarities = {        
    "minimum": 0,
    "pitiful": 80,
    "bad": 230,
    "subpar": 430,
    "normal": 780,
    "good": 930,
    "epic": 985,
    "legendary": 999,
    "perfect": 1000
}

book_rarities = {
    "minimum": 0,
    "blank": 100,
    "overrated": 200,
    "bad": 365,
    "normal": 765,
    "knowledgeable": 930,
    "intellectual": 989,
    "philosophical": 999,
    "wisdom": 1000
}

misc_rarities = {
    "minimum": 0,
    "tiny": 80,
    "smaller": 200,
    "small": 300,
    "normal": 700,
    "large": 800,
    "larger": 880,
    "huge": 960,
    "huger": 990,
    "enormous": 995,
    "enormouser": 999,
    "gigantic": 1000
}

book_rarity_names = [
    "minimum",
    "blank",
    "overrated",   
    "bad",
    "normal",
    "knowledgeable",
    "intellectual",
    "philosophical",
    "wisdom"
]

rarity_names = [
    "minimum",
    "pitiful",
    "bad",
    "subpar",
    "normal",
    "good",
    "epic",
    "legendary",
    "perfect"]

misc_rarity_names = [
    "minimum",
    "tiny",
    "smaller",
    "small",
    "normal",
    "large",
    "larger",
    "huge",
    "huger",
    "enormous",
    "enormouser",
    "gigantic",
]

rarity_prices = {        
    "minimum": 0,
    "pitiful": 1,
    "bad": 2,
    "subpar": 3,
    "normal": 5,
    "good": 7,
    "epic": 10,
    "legendary": 25,
    "perfect": 100
}

book_rarity_prices = {  #will have to be changed 
    "minimum": 0,
    "blank": 1,
    "overrated": 5,
    "bad": 3,
    "normal": 5,
    "knowledgeable": 7,
    "intellectual": 10,
    "philosophical": 25,
    "wisdom": 100
}

misc_rarity_prices = {
    "minimum": 0,
    "tiny": 1,
    "smaller": 2,
    "small": 3,
    "normal": 5,
    "large": 6,
    "larger": 8,
    "huge": 10,
    "huger": 15,
    "enormous": 25,
    "enormouser": 50,
    "gigantic": 100
}

market_loot = [
    "hp_pot",
    "mn_pot",
    "book",
    "max_health",
    "max_mana", # sell books??
    "attack",   # could add difference in chance based on how big your attack and defence already is
    "defence"]  # could also add differences in the amount of stuff you get in a rarity-like system?

classes = {
    "hp_pot": hp_pot,
    "mn_pot": mn_pot,
    "book": book,
    "max_health": max_health,
    "max_mana": max_mana,
    "attack": attack,
    "defence": defence
}

stat_items = [
    "max_health",
    "max_mana",
    "attack",
    "defence"
]

prices = []
gen_rarities = []
gen_items = []
stat = 0

def buy_options(option_amt, n, stats_list):        #printing the options for what is being sold.
    global prices
    global gen_rarities
    global gen_items
    global stat
    gen_market_loot(option_amt, n)
    market_done = False
    items_left = Market.buy_max
    try:    #putting outside of loop so it only tells once
        print(f'You have {Inventory.inventory["gold"]} gold left.')
    except: #case for 0 gold (gold is not in inventory yet)
        try:
            if Inventory.inventory["gold"] <= 0:
                print("You have no gold.")  #just in case that having 0 gold while having it unlocked is a bad thing
            else:
                print("You have no gold.")
        except:
            print("You have no gold.")
        t.sleep(n)
    while market_done == False:
        if items_left == 0: # checks how many items you have left
            market_done = True
        while items_left >= Market.buy_max:
            counter = 1
            choices = ""
            while counter <= option_amt:
                choices = choices + str(counter) + ", "
                counter += 1
            #print(len(gen_items))
            for option in range(0, len(gen_items)):
                #print(option, gen_rarities[option])
                try:
                    stat = getattr(classes[gen_items[option]], gen_rarities[option]) #tries to get an attribute for an item that has one
                except Exception:
                    pass
                #print(type(loot_names[gen_items[option]]))
                if gen_items[option] == "book":
                    print(f'{option+1}. {gen_rarities[option].capitalize()} {loot_names[gen_items[option]]} - {prices[option]} gold')   #special book text
                else:
                    print(f'{option+1}. {gen_rarities[option].capitalize()} ({stat}) {loot_names[gen_items[option]]} - {prices[option]} gold')
                t.sleep(n)
            try:
                choice = int(input(f"Enter the number of the option you want to buy: ({choices}0 for none): "))
            except:
                print("You didn't enter a valid option.")
                t.sleep(n)
                continue
            if choice == 0:
                print("Exiting out of market...")
                t.sleep(n)
                market_done = True
                items_left = 0
                return 0
            if choice >= 1 and choice <= option_amt:
                try:
                    if Inventory.inventory["gold"] >= prices[choice-1]:
                        buy_item(prices[choice-1])
                        add_item(loot_names[gen_items[choice-1]], gen_rarities[choice-1], 1, n)
                        #print("item added")
                        items_left -= 1
                    else:
                        print("You don't have enough gold for that.")
                        t.sleep(n)
                except:
                    print("You have no gold in your inventory.")
                    t.sleep(n)
            else:
                print("You didn't enter a valid option.")
                t.sleep(n)

def gen_market_loot(option_amt, n):          #generating the loot to be sold
    global prices
    global gen_rarities
    global gen_items
    prices = []
    gen_rarities = []
    gen_items = []
    for option in range(0, option_amt):
        loot = r.choice(market_loot)
        #print(loot)
        if loot == "hp_pot" or loot == "mn_pot" or loot in pots:
            rarity = pots_rarity_gen()
            price = pots_price_gen(rarity)
        elif loot == "book" or loot in other:
            rarity = book_rarity_gen()
            price = book_price_gen(rarity)
        elif loot in misc:
            rarity = misc_rarity_gen()
            price = misc_price_gen(rarity)
        gen_rarities.append(str(rarity))
        rarity = rarity.capitalize()
        #print(rarity)
        gen_items.append(loot)
        prices.append(price)
        #print(gen_items, gen_rarities, prices)
        #print(f'{option}. {rarity} {loot_names[loot].lower()}')
        

def book_rarity_gen():
    num = r.randint(1, 1000)    #number for chance
    for chance in range(1, len(book_rarities)):
        #print(rarity_names[chance-1])
        if num >= book_rarities[book_rarity_names[chance-1]] and num < book_rarities[book_rarity_names[chance]]:
            item_rarity = book_rarity_names[chance]
            return item_rarity
        else:
            continue

def book_price_gen(rarity):
    return book_rarity_prices[rarity]

def pots_rarity_gen():
    num = r.randint(1, 1000)
    for chance in range(1, len(rarities)):
        #print(rarity_names[chance-1])
        if num >= rarities[rarity_names[chance-1]] and num < rarities[rarity_names[chance]]:
            item_rarity = rarity_names[chance]
            return item_rarity
        else:
            continue

def pots_price_gen(rarity):
    return rarity_prices[rarity]

def misc_rarity_gen():
    num = r.randint(1, 1000)
    for chance in range(1, len(misc_rarities)):
        #print(rarity_names[chance-1])
        if num >= misc_rarities[misc_rarity_names[chance-1]] and num < misc_rarities[misc_rarity_names[chance]]:
            item_rarity = misc_rarity_names[chance]
            return item_rarity
        else:
            continue

def misc_price_gen(rarity):
    return misc_rarity_prices[rarity]

def sell_item(n):
    market_done = False
    while market_done == False:
        try:
            item = input("Enter type of item (health potion, mana potion, book, scrap, 0 for exit): ").lower().strip()       # update for future items
        except:
            print("That is not valid.")
            t.sleep(n)
            return 0
        if item == "0":
            print("Exiting...")
            t.sleep(n)
            market_done = True
            break
        if item == "gold":
            print("You can't sell money, doofus.")
            t.sleep(n)
            continue
        #temp loop to find word keys for just items
        item_found = False
        for item_temp in Inventory.inventory.keys():
            try:
                item_word = item_temp.split(" ")[1] #tries to find item word if it has rarity
            except:
                if item.split(" ")[0] == "scrap":
                    break
            try:
                if item == item_word:   # item_word wont exist to compare to if no rarity so it must be in try/except
                    item_found = True
                    break
            except:
                continue
        if item_found == False:
            print("That item is not in your inventory.")
            t.sleep(n)
            continue
        while True:
            if item in no_rarity:
                pass
            else:
                if item == "book":
                    rarity = input("Enter the rarity (blank, overrated, bad, normal, knowledgeable, intellectual, philosophical, wisdom, 0 for exit): ").strip().lower()
                else:
                    rarity = input("Enter the rarity (pitiful, bad, subpar, normal, good, epic, legendary, perfect, 0 for exit): ").strip().lower()
                if rarity not in rarity_names:  #checking if its in rarity_names
                    if rarity in book_rarity_names: #check if its in the other list, cuz its still valid if it is
                        pass
                    else:
                        print("That is not a valid rarity.")
                        t.sleep(n)
                        continue
                elif rarity not in book_rarity_names:   #if its not valid properly
                    print("That is not a valid rarity.")
                    t.sleep(n)
                    continue
                if f'{rarity} {item}' not in Inventory.inventory.keys():
                    print(f"You do not have a {item} with that rarity.")
                    t.sleep(n)
                    continue
                if rarity == "0":
                    print("Exiting market...")
                    t.sleep(n)
                    market_done = True
                    break
            break
        while True:
            try:
                if item in no_rarity:
                    amount = int(input(f'Enter the amount to be sold (you have {Inventory.inventory[f'{item}']}, 0 for exit): '))
                else:
                    amount = int(input(f'Enter the amount to be sold (you have {Inventory.inventory[f'{rarity} {item}']}, 0 for exit): '))
            except:
                print("That is not a valid amount.")
                t.sleep(n)
                continue
            if amount == 0:
                print("Exiting market...")
                t.sleep(n)
                market_done = True
                break
            if item in no_rarity:
                if amount > Inventory.inventory[f'{item}'] or amount <= 0:
                    print("You can't sell that many.")
                    t.sleep(n)
                    continue
            else:
                if amount > Inventory.inventory[f'{rarity} {item}'] or amount <= 0:
                    print("You can't sell that many.")
                    t.sleep(n)
                    continue
            if item not in no_rarity:
                try:
                    Inventory.inventory[f'{rarity} {item}'] -= amount
                    if amount >= 2: #grammar purposes
                        print(f'Sold {amount} {rarity} {item}s.')
                    elif amount == 1:
                        print(f'Sold {amount} {rarity} {item}.')
                    t.sleep(n)
                    if rarity in rarity_prices:
                        add_item("gold", None,  m.floor(0.6*rarity_prices[rarity]), n)
                    else:
                        if rarity == "overrated":
                            add_item("gold", None,  m.floor(1*book_rarity_prices[rarity]), n)
                        else:
                            add_item("gold", None,  m.floor(0.6*book_rarity_prices[rarity]), n)
                    if Inventory.inventory[f'{rarity} {item}'] <= 0:
                        Inventory.inventory.pop(f'{rarity} {item}')
                    market_done = True
                    break
                            
                except Exception:
                    print("there was error here, somehow")
                    t.sleep(n)
                break

            else:
                try:
                    Inventory.inventory[f'{item}'] -= amount
                    print(f'Sold {amount} {item}.')
                    t.sleep(n)
                        #only scrap for now
                    add_item("gold", None,  m.ceil(0.5*amount), n)
                    if Inventory.inventory[f'{item}'] <= 0:
                        Inventory.inventory.pop(f'{item}')
                            
                except Exception:
                    print("error here??")
                    t.sleep(n)
                break
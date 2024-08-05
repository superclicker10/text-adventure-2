from mainscript import *
from inventory import *
from cellcreation import *
import os

def save(stats_list, x, y):
    try:
        os.remove("cells.txt")
    except:
        pass
    file = open("cells.txt", "w")
    for line in list(cells):
        val = cells[line]
        file.writelines(f"{line}\n")
        file.writelines(f"{val}\n")
    file.close()
    try:
        os.remove("cellsvisited.txt")
    except:
        pass
    file = open("cellsvisited.txt", "w")
    for line in list(cells_visited):
        val = cells_visited[line]
        file.writelines(f"{line}\n")
        file.writelines(f"{val}\n")
    file.close()
    try:
        os.remove("playerstats.txt")
    except:
        pass
    file = open("playerstats.txt", "w")
    file.write(f'{x}\n')
    file.write(f'{y}\n')
    for line in stats_list:
        try:
            file.writelines(f'{line}\n')
        except:
            file.writelines(f"{line}\n")
    file.close()
    try:
        os.remove("inventory.txt")
    except:
        pass
    file = open("inventory.txt", "w")
    for line in list(Inventory.inventory):
        val = Inventory.inventory[line]
        file.writelines(f"{line}\n")
        file.writelines(f"{val}\n")
    file.close()

def load(player, x, y):
    try:
        file = open("cells.txt", "r")
        content = file.readlines()
        for line in range(0, len(content), 2):
            content[line] = content[line].rstrip('\n')
            content[line+1] = content[line+1].rstrip('\n')
            cells[content[line]] = str(content[line+1])
        file.close()
        #print(cells)
    except:
        #print("There is error")
        return 0
    try:
        file = open("cellsvisited.txt", "r")
        content = file.readlines()
        for line in range(0, len(content), 2):
            content[line] = content[line].rstrip('\n')
            content[line+1] = content[line+1].rstrip('\n')
            #print(content[line])
            cells_visited[content[line]] = eval(content[line+1])
        file.close()
    except:
        return 0
    try:
        file = open("inventory.txt", "r")
        content = file.readlines()
        for line in range(0, len(content), 2):
            content[line] = content[line].rstrip('\n')
            content[line+1] = content[line+1].rstrip('\n')
            Inventory.inventory[content[line]] = int(content[line+1])
        file.close()
    except:
        return 0
    try:
        file = open("playerstats.txt", "r")
        content = file.readlines()
        for line in content:
            line = line.rstrip("\n")
        x = int(content[0].rstrip("\n"))
        y = int(content[1].rstrip("\n"))
        player.health = float(content[2].rstrip("\n"))
        player.max_health = float(content[3].rstrip("\n"))
        player.health_regen = float(content[4].rstrip("\n"))
        player.mana = float(content[5].rstrip("\n"))
        player.max_mana = float(content[6].rstrip("\n"))
        player.mana_regen = float(content[7].rstrip("\n"))
        player.attack = float(content[8].rstrip("\n"))
        player.defence = float(content[9].rstrip("\n"))
        Inventory.inventory["gold"] = int(content[10].rstrip("\n"))
        stats_list = [player.health,    # reinitializing the list to update the values
            player.max_health,
            player.health_regen,
            player.mana,
            player.max_mana,
            player.mana_regen,
            player.attack,
            player.defence,
            Inventory.inventory["gold"]]
            #print("here")
        file.close()
    except:
        return 0
    return cells, cells_visited, Inventory.inventory, stats_list, x, y
    
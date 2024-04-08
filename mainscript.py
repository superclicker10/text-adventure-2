from move import *
import time as t
x = 0
y = 0
n = 1
grid = Grid()
def delay():
    global n
    try:
        n = float(input("How long should the text delay be in seconds? (0.5-2): "))
    except:
        print("You have entered an invalid value. Delay set to default (1).")
        n = 1 
    if n < 0.5:
        print("Delay set to minimum value (0.5).")
        n = 0.5
    if n > 2:
        print("Delay set to maximum value (2).")
        n = 2

def move():
    global x
    global y
    direction = input("Where would you like to move? (left, right, up, down): ")
    try:
        temp_x = x
        temp_y = y
        try:
            x = eval(f'grid.{direction}(grid.oob, temp_x, temp_y, n)')[0]
        except:
            return x, y
        if f'grid.{direction}(grid.oob, temp_x, temp_y, n)' == False:
            return x, y
        y = eval(f'grid.{direction}(grid.oob, temp_x, temp_y, n)')[1]
    except AttributeError:
        print("You have entered an invalid movement direction.")
    return x, y

def repeated_action():
    print(f'You are currently at ({x}, {y}).')
    choice = input("What would you like to do? (move, interact, use, exit): ")
    if choice == "exit":
        print("Thanks for playing!")
        t.sleep(1)
        exit()
    try:
        eval(f'{choice}()')
    except:
        print("You can't do that.")

delay()
while True:
    repeated_action()



    
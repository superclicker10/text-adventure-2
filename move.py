import time as t
from oobcreation import oob_creation
class Grid:
    oob = oob_creation()

    def right(self, oob, x, y, n):
        if (x+1, y) in oob:
            print("You can't move that way.")
            t.sleep(n)
            return False
        else:
            x += 1
        t.sleep(n/2)
        return x, y
    
    def left(self, oob, x, y, n):
        if (x-1, y) in oob:
            print("You can't move that way.")
            t.sleep(n)
            return False
        else:
            x -= 1
        t.sleep(n/2)
        return x, y

    def up(self, oob, x, y, n):
        if (x, y+1) in oob:
            print("You can't move that way.")
            t.sleep(n)
            return False
        else:
            y += 1
        t.sleep(n/2)
        return x, y
    
    def down(self, oob, x, y, n):
        if (x, y-1) in oob:
            print("You can't move that way.")
            t.sleep(n)
            return False
        else:
            y -= 1
        t.sleep(n/2)
        return x, y
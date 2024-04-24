import os as o
import time as t

def make_reqs(requirements_file_write, n):
    if o.path.isfile("requirements.txt"):
        o.remove("requirements.txt")
        #print("Original file deleted.")
        #t.sleep(n)
    with open("requirements.txt", "w") as reqs:
        for line in requirements_file_write:
            reqs.write(line+"\n")

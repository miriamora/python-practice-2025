import os

inventory = [ "nproc", "uname -r", "pwd"]
try:

    for i in inventory:
        os.system(i)
except Exception as e:
    print(e)
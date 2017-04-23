import sys, os 
dir = '/storage/emulated/0/qpython/scripts3/' 
os.chdir(dir) 
def callyps(val):
    os.system(sys.executable+" yps.py " + val) 
while True: 
    val = input('$:') 
    if val: 
        callyps(val) 
    else: 
        break
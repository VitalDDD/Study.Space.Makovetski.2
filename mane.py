import shutil, os, os.path

def mane_function(slov, nazva):
    sl=open(f"{nazva}.txt", "w")
    for k in slov:
        sl.write(f"{k} : {slov[k]} \n")
    sl.close()
    print("Good job!")
    return sl


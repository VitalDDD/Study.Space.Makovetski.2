import shutil, os, os.path

def mane_function(slov, nazva):
    sl=open(f"{nazva}.txt", "w")
    for k in slov:
        sl.write(f"{k} : {slov[k]} \n")
    sl.close()
    print("Good job!")
    print("Good luck!")
    return sl

def pr_nt(p):
    i,j=0,0
    for f in os.listdir(p):
        if os.path.isdir(f):
            j+=1
            print("|", f)
        else:
            i+= 1
            print(f)
    print(f"Каталогів: {j}", f"Файлів: {i}")

def test_function(file):
    dct={}
    dt=open(f"{file}", "r")
    for l in dt:
        kk=l.rstrip("\n")
        kl = kk.rsplit(":")
        k = kl[0]
        v = kl[1]
        dct.update({k:v})
    dt.close()
    return dct

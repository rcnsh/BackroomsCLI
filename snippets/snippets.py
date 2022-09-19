def updatenoclip():
    f = open("./profileData/noclip.txt", "r")
    noclipcount = f.read()
    f.close()
    noclipcount = int(noclipcount)
    noclipcount = - 1
    noclipcount = str(noclipcount)
    f = open("./profileData/noclip.txt", "w")
    f.write(noclipcount)
    f.close()

def updatehealth(health):
    f = open("./profileData/health.txt", "r")
    healthcount = f.read()
    f.close()
    healthcount = int(healthcount)
    healthcount = + health
    healthcount = str(healthcount)
    f = open("./profileData/health.txt", "w")
    f.write(healthcount)
    f.close()

def updatealmond(almond):
    f = open("./profileData/almondWater.txt", "r")
    almondcount = f.read()
    f.close()
    almondcount = int(almondcount)
    almondcount = + almond
    almondcount = str(almondcount)
    f = open("./profileData/almondWater.txt", "w")
    f.write(almondcount)
    f.close()

def clear():
    import os
    clear = lambda: os.system('cls')
    clear()

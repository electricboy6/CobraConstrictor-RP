from constants import *
import schembuilder as schem
import infoROMparser as ROMparse
import pickle

def saveRP():
    with open('temp/rp.pickle', 'wb') as f:
        f.write(pickle.dumps(RPcompiled))
    with open('output/out.rp', 'w') as f:
        f.write(str(RPcompiled))

def loadRP():
    with open('temp/rp.pickle', 'rb') as f:
        RPcompiled = pickle.load(f)

def loadCobra():
    with open("input/code.cobra", "r") as cobraCode:
        print("not done")
        return("cobra code")

def sourceToLowLevel():
    print("not done")
    return("low level code")

def lowLevelToRP():
    global RPcompiled
    print("not done")
    RPcompiled = [[0 for i in range(BIT_COUNT)] for j in range(1)] #word count goes in place of 1

def compile():
    lowLevelToRP(sourceToLowLevel(loadCobra()))
    makeROM()

def makeROM(wordcount, version):
    global RPcompiled
    RPcompiled = [[0 for i in range(BIT_COUNT)] for j in range(wordcount)]
    saveRP()
    schem.makeROM(wordcount, version)
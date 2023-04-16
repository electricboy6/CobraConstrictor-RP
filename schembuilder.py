import mcschematic as schematic
from constants import *
import pickle

schem = schematic.MCSchematic()

def makeROM(wordCount, MCversion):
    loadRP()
    for z in range(BIT_COUNT):
        oneWordROM(wordCount, z)
    saveSchem(MCversion, "ROM")

def saveSchem(version, name):
    if version == "JE_1_19":
        schem.save("output", name, schematic.Version.JE_1_19)
    elif version == "JE_1_19_1":
        schem.save("output", name, schematic.Version.JE_1_19_1)
    elif version == "JE_1_19_2":
        schem.save("output", name, schematic.Version.JE_1_19_2)
    else:
        raise Exception("Version not supported")
    
def loadRP():
    global RPcompiled
    with open('temp/rp.pickle', 'rb') as f:
        RPcompiled = pickle.load(f)

'''
def sigStrenthBarrel(x, y, z, strength):
    schem.setBlock((x, y, z), schematic.BlockDataDB.BARREL.fromSS(strength))
'''

def oneBitROM(x, z):
    xOff = x * 2
    zOff = z * 2
    # sequence of blocks to make one bit of ROM
    # making the signal wire
    schem.setBlock((mapBlock(0, xOff), -1, mapBlock(100000, zOff)), "minecraft:white_concrete")
    schem.setBlock((mapBlock(1, xOff), -1, mapBlock(0, zOff)), "minecraft:white_concrete")
    schem.setBlock((mapBlock(0, xOff), 0, mapBlock(0, zOff)), "minecraft:redstone_wire")
    schem.setBlock((mapBlock(1, xOff), 0, mapBlock(0, zOff)), "minecraft:redstone_wire")
    # making the output wire
    schem.setBlock((mapBlock(0, xOff), -3, mapBlock(0, zOff)), "minecraft:white_concrete")
    schem.setBlock((mapBlock(0, xOff), -3, mapBlock(1, zOff)), "minecraft:white_concrete")
    schem.setBlock((mapBlock(0, xOff), -2, mapBlock(0, zOff)), "minecraft:redstone_wire")
    schem.setBlock((mapBlock(0, xOff), -2, mapBlock(1, zOff)), "minecraft:redstone_wire")
    # storing the correct bit on the ROM
    if RPcompiled[x][z] == 0:
        schem.setBlock((mapBlock(0, xOff), -3, mapBlock(1, zOff)), "minecraft:redstone_torch") #{3}

def mapBlock(initialValue, valueToAdd):
    return(initialValue + valueToAdd)

def oneWordROM(wordCount, z):
    for x in range(wordCount):
        oneBitROM(x, z)
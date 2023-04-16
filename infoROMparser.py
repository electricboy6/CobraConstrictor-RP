import json
import schembuilder as schem
from constants import *

def parseInfoROM():
    with open("input/requirements.json", "r") as f:
        requirements = json.load(f)
        f.close()
    requirements["RPversion"] = RP_VERSION
    requirements["CobraRPversion"] = COBRA_RP_VERSION
    #generate rom schematic for the infoROM
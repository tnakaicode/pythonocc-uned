import os
import sys
from pathlib import Path

import pytest

import freecad

fp = open("./test_import_debug.txt", "w")
for key in os.environ.keys():
    fp.write(key + "\n")
fp.close()

sys.path.append(os.path.join("./src/"))
import geouned

def test_1():
    print(1)
    fp = open("./test_import_pytest.txt", "w")
    #fp.write(geouned.__version__ + "\n\n")
    for key in os.environ.keys():
        fp.write(key + "\n")
    fp.close()
    
    geo = geouned.CadToCsg()
    #geo.start()

import os
import sys
from pathlib import Path

import pytest

sys.path.append(os.path.join("./src/"))
import geouned

def test_1():
    print(1)

    geo = geouned.CadToCsg()
    #geo.start()

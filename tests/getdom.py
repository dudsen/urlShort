import sys, os
sys.path.append(os.getcwd())
#'/home/dudsen/py/tests/urlShort')
from urlShortCore import interfaceout
from random import randrange

with open('tests/hex.txt') as f:
        lines = f.read().splitlines()
print lines
for item in lines:
    print interfaceout(item)

for i in range(10):
    val = interfaceout(hex(randrange(21433552)).lstrip('0x'))
    if val:
        print val
    else:
        print 'sorry'

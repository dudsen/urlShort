from urlShortCore import interfacein
from gen.getstr import getdom 

print getdom()
vals = []
for i in range(500):
    val =  interfacein(getdom())
    print val
    vals.append(val)

open("hex.txt", "w").write("\n".join(("\t".join(item)) for item in vals))

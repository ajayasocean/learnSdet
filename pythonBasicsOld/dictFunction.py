# Examples of dict() function

aPort = [[80,"http"],[20,"ftp"],[23,"telnet"]]

bPort = [(443,"https"),(53,"DNS")]

print('aport = ',aPort)
print('Type of aPort is',type(aPort))
aPortD = dict(aPort)
print('aportD = ',aPortD)
print('Type of aPortD is',type(aPortD))

print('bport = ',bPort)
print('Type of bPort is',type(bPort))
bPortD = dict(bPort)
print('bportD = ',bPortD)
print('Type of bPortD is',type(bPortD))

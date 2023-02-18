import json

d = open('sample.json').read()

ob = json.loads(d)
print(
    "================================================================================" "\n"
    "DN                                                 Description           Speed   MTU" "\n" 
    "-------------------------------------------------- --------------------  ------ ------")
imdata = ob["imdata"]
for i in imdata:
        dn = i["l1PhysIf"]["attributes"]["dn"]
        descr = i["l1PhysIf"]["attributes"]["descr"]
        speed = i["l1PhysIf"]["attributes"]["speed"]
        mtu = i["l1PhysIf"]["attributes"]["mtu"]

        print("{0:50} {1:21} {2:7} {3:10}".format(dn, descr, speed, mtu))
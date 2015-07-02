#!/usr/bin/python
import lmdb
import sys
env = lmdb.open('/home/andrew/.bitmonero/lmdb/' , max_dbs=2, readonly=True)
#subdb = env.open_db('data.mdb')

print"stat"
print(env.stat())
print""

print"Keys"
with env.begin() as txn:
    with txn.cursor() as curs:
        for key, value in curs: # Iterate from first key >= '5'.
            print((key, value))

keyy = raw_input("key desired?")
child_db = env.open_db(key = keyy)

print("blah")
i = 0
top = 20
if len(sys.argv) >= 2:
    top = int(sys.argv[1])
with env.begin() as txn:
    with txn.cursor(child_db) as curs:
        for a in curs:
            i = 0
            for b in a:
                c = b.encode("hex")
                #print(c)
                if keyy == "txs":
                    if i == 0:
                        print("txhash", c)
                        print("header:", c[0:2])
                        print("ring size:", int(c[2:2+4], 16))
                    else:
                        header = c[0:2]
                        ringsize = int(c[2:2+4], 16)
                        if ringsize > 10000:
                            print("mixin 0")
                            #not a ring
                        else:
                            bleh = c[6:26]
                            for j in range(0, ringsize):
                                inkey = c[26 + j*86:26 + j*86 + 64]
                                print("inkey", inkey)
                                bleh2 = c[26 + j*86 +64:26 + j*86 + 64 + 22]
                            outs = c[26 + (ringsize - 1) * 86 + 80 :]
                            header2 = outs[0:2]
                            numouts = int(len(outs) / (70))
                            print("header2:", header2)
                            print("# outputs = ", numouts)
                            for j in range(0, numouts):
                                output = outs[2*int(j==0)+j * 80:2*int(j==0) + j * 80 + 64]
                                print("output", output)

                            print("outs", outs)
                            header2 = outs[0:2]
                                



                else:
                    print(c)
                i+= 1


            q = raw_input("Continue?")
            if q == "q":
                quit()
            print("")
        #if not curs.set_key(keyy):
            #print("No values found for '"+keyy+"'")
        #else:
            #for a in enumerate(curs.iternext()):
                #print("a:", a)

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
            for b in a:
                print(b.encode("hex"))
            #print(unicode(a[0]).decode('utf-8'))
            q = raw_input("Continue?")
            if q == "q":
                quit()
            print("")
        #if not curs.set_key(keyy):
            #print("No values found for '"+keyy+"'")
        #else:
            #for a in enumerate(curs.iternext()):
                #print("a:", a)

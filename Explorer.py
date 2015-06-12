import lmdb
env = lmdb.open('/home/andrew/.bitmonero/lmdb/', readonly=True)
i = 0
with env.begin() as txn:
    for i in range(0, 200):
        cursor = txn.cursor()
        print("thing i = ", i)
        for key, value in cursor:
            print(key, value)
        print (" ")
        print(" ")
        print ("next ")
        cursor.next()



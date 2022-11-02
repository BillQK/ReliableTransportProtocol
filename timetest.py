import time, hashlib

testtime = time.time() + 1.0
while(time.time() <= testtime):
    print("silly goose")
#print("this is the current time " + str(time.time()) + " this is what happens after adding one " + str(time.time() + 1.0))

#how does hashing this help the problem
blockex = "----- Block 0000000 -----496a65fef982481c67afebdca03a356"
y = hashlib.md5(blockex.encode('utf-8')).digest()
print(y)

blockex2 = "----- Block 0000000 -----496a65fef982481c67afebdca03a356"
y1 = hashlib.md5(blockex2.encode('utf-8')).digest()
print(y1)



corrblock = "BlocX 00000X7 -----45Xe3e63c8fc5c94db63fb3f2271173eddf52fa76ad13"



#lETS SEE WHO IS FASTER, LIST OR TUPLE

import time
L = list(range(100000000))
T = tuple(range(100000000))

start = time.time()
for i in L:
    i*5
LTime = time.time()
print('List time: ',LTime-start)

start1 = time.time()
for i in T:
    i*5
TTime = time.time()
print('Tuple time: ', TTime-start1)

print(LTime - TTime)

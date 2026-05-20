#Also check who take more space in memory

import sys

L = list(range(10000))
T = tuple(range(10000))

print('List size: ',sys.getsizeof(L))
print('Tuple size: ',sys.getsizeof(T))
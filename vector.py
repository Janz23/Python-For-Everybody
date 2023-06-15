import numpy as np
import time

one = np.array(range(10000))
two = np.array(range(10000))

f = 0
#tic = time.time()
#for j in range(1000):
#    f = f + one[j] * two[j]
#    print(j, 'of 10000')
#toc = time.time()
#print(f)
#print('Time of execution', 1000*(toc-tic), 'ms.')

tic = time.time()
h = np.dot(one, two)
toc = time.time()
print(h)
print('Time of execution', 100000*(toc-tic), 'sec.')

# %% importing

from multiprocessing.pool import Pool
from time import time

import matplotlib.pyplot as plt
from numba import njit
from numpy import array, dot, random, ndarray, zeros
from numpy._core.multiarray import ndarray
import seaborn as sns

sns.set_style('darkgrid')


# %% mapped operation
@njit
def operation(data1: ndarray, data2: ndarray):
    result = zeros((data1.shape[0], data2.shape[1]))
    for i in range(data1.shape[0]):
        for j in range(data2.shape[1]):
            result[i,j] = data1[i,:].dot(data2[:,i])
    return result


# %%

n = 100
data1 = random.rand(n,n)
data2 = random.rand(n,n)
# %%

data1[99,:].dot(data2[:,99])


# %%


args = [(data1[i,:], data2[:,i]) for i in range(n)]

# %%

def multiprocess_multiplication(process_number: int, data1, data2) -> ndarray:
    with Pool(processes=process_number) as pool:
        result = array(pool.starmap(operation, iterable=(data1, data2)))
    return result


# %%

start = time()
np_result = dot(data1, data2)
np_duration = time() - start
np_duration
# %%

start = time()
py_result = operation(data1, data2)
py_duration = time() - start
py_duration



# %%
my_times = []
diffs = []

for n in range(1, 16):
    start = time()
    my_result = multiprocess_multiplication(n, data1, data2)
    #print(my_result.shape)
    duration = time() - start
    diffs.append((np_result - my_result).sum())
    my_times.append(duration)



# %%
plt.scatter(range(1,16), my_times)
# %%

diffs

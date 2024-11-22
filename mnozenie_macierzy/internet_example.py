# %% importing

# example of tuned multiprocessing matrix multiplication with process pool
from multiprocessing.pool import Pool
from time import time

import matplotlib.pyplot as plt
from numpy import array, dot, ones

# %%
# function for performing operation on matrices
def operation(item1, item2):
    # matrix multiplication
    return item1.dot(item2)

# %%
# protect the entry point
if __name__ == "__main__":
    # record the start time
    # prepare lists of matrices
    n = 2000
    data1 = ones((n, n))
    data2 = ones((n, n))
    internet = []
    np = []
    for process_number in range(1, 17):
        internet_durations = []
        for n in range(10):
            start = time()
            # create thread pool
            with Pool(process_number) as pool:
                # prepare arguments
                args = [(item1, item2) for item1, item2 in zip(data1, data2)]
                # print(args[0])
                # issue tasks to thread pool
                results = array(pool.starmap(operation, args))
            # calculate and report duration
            duration = time() - start
            internet_durations.append(duration)
        else:
            internet.append(sum(internet_durations) / len(internet_durations))
            # print(f"Internet took: {duration:.3f} seconds")

        np_durations = []
        for n in range(10):
            start = time()
            results2 = dot(data1, data2)
            duration2 = time() - start
            np_durations.append(duration2)
        else:
            np.append(sum(np_durations) / len(np_durations))

        # print(f"Numpy took: {duration2:.3f} seconds")

        # print((results2 - results).sum())
    else:
        plt.scatter(range(1, 17), internet, label="internet")
        plt.scatter(range(1, 17), np, label="np")
        plt.legend()
        plt.show()

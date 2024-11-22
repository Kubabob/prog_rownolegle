import multiprocessing as mp
import time
from typing import List

import numpy as np

m_size = 10

m1 = np.random.randint(10, size=(m_size, m_size))
m2 = np.random.randint(10, size=(m_size, m_size))

processes_number = 10


def worker(m1, m2, row_idx, result):
    for col_idx in range(m_size):
        result[row_idx, col_idx] = np.dot(m1[row_idx, :], m2[:, col_idx])


# @overload
def operation(
    item1: List[np.int64] = [np.int64(1) for _ in range(m_size)],
    item2: List[List[np.int64]] = [
        [np.int64(1) for _ in range(m_size)] for _ in range(m_size)
    ],
) -> List[List[np.int64]]:
    r = [np.dot(item1, item2[i]) for i in range(len(item2))]

    # r = np.dot(item1, item2)
    # print(r)
    return r


if __name__ == "__main__":
    start = time.time()

    with mp.Pool(processes_number) as pool:
        # args = [(item1, item2) for item1, item2 in zip(m1, m2)]
        args = [(m1[i, :], m2[:, :]) for i in range(m_size)]
        # print(args[0])
        result = np.array(pool.map(operation, args))

    elapsed1 = time.time() - start

    start = time.time()
    result_np = np.dot(m1, m2)
    elapsed2 = time.time() - start

    # print(f"{result}")

    print(
        f"For M_{m1.shape} and {processes_number} it took: {elapsed1:.2f} seconds"
    )

    # print(f"{result}")

    print(f"For M_{m1.shape} and numpy it took: {elapsed2:.2f} seconds")
    print(result_np - result)

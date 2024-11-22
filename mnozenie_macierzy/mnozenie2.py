import numpy as np

m_size = 10


def worker(m1, m2, idx, result):
    result[idx] = np.dot(m1[idx], m2[idx])


result = np.zeros((10, 10))

# print(result)

result[:, 0] = [1 for _ in range(10)]

# print(result)

m1 = np.random.randint(10, size=(m_size, m_size))
m2 = np.random.randint(10, size=(m_size, m_size))

for idx in range()
print(np.dot(m1[0, :], m2[:, 0]))

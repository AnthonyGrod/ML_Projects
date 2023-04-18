import matplotlib.pyplot as plt
import numpy as np


def fn(arg):
    if arg == 0:
        return 0.5
    return 1 / (4 * np.absolute(arg) * (np.absolute(arg) + 1))


def sample(n):
    arr1 = np.floor(1 / (1.0 - np.random.rand(n)))
    arr2 = np.random.choice([0, 0, -1, 1], n)
    res = np.multiply(arr1, arr2)
    return res


xList = np.linspace(-10, 10, 21)
yList = [fn(x) for x in xList] 

n = 10000

result = sample(n)

prefix_sum = np.cumsum(result)
average = prefix_sum / np.arange(1, n + 1)

median = np.array([np.median(result[:(i+1)]) for i in range(1, n)])

plt.plot(xList, yList, 'o')
plt.show()

plt.plot(average)
plt.show()

plt.plot(median)
plt.show()

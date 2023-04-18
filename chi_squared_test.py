import numpy as np
import scipy
import matplotlib.pyplot as plt

# Rows: women, men
# Columns: PiS, PO, Kukiz, Nowoczesna, Lewica, PSL, Razem, KORWiN
data1 = np.array([[17508, 11642, 3308, 3131, 2911, 2205, 1852, 1235],
                  [17672, 9318, 4865, 3259, 3029, 2479, 1606, 3259]])


def test(data):
    votes_sum = np.sum(data)
    rows_sum = np.array([np.sum(data[0]), np.sum(data[1])])
    columns_sum = np.array([(data[0][i] + data[1][i]) for i in range(len(data[0]))])
    f = np.array([[(rows_sum[i] * columns_sum[j]) / votes_sum for j in range(len(columns_sum))] for i in range(len(rows_sum))])
    S = np.sum([((f[i][j] - data[i][j]) ** 2 / f[i][j]) for i in range(len(rows_sum)) for j in range(len(columns_sum))])
    # chi^2 test
    return 1 - scipy.stats.chi2.cdf(S, (len(rows_sum) - 1) * (len(columns_sum) - 1))


# funkcja agregująca dane partii o liczbie głosów mniejszej niż 5% wszystkich głosów
def removeLowest(data):
    sum = [0, 0]
    votes_sum = np.sum(data)
    columns_sum = [(data[0][i] + data[1][i]) for i in range(len(data[0]))]
    res = [[], []]
    for i, x in enumerate(columns_sum):
        if x < votes_sum * 0.05:
            # Dodajemy do votes_sum liczbę głosów, jeśli jest ona mniejsza niz 5%
            sum[0] += data[0][i]
            sum[1] += data[1][i]
        else:
            # Jeśli nie jest mniejsza niż 5%, to nie
            res[0].append(data[0][i])
            res[1].append(data[1][i])
    res[0].append(sum[0])
    res[1].append(sum[1])
    return np.array(res)


def attempt():
    # generate a similar dataset with 6 parties and two genders
    # this time the null hypothesis is true, i.e., gender has no effect on voting preferences
    data = np.zeros([2, 6])
    for k in range(10000):
        i = np.random.randint(2)
        j = int(np.sqrt(np.random.randint(36)))
        data[i][j] = data[i][j] + 1
    # replace np.random.random() with the p-value returned by your implementation of chi-square independence test
    # return chi_square_independence_test_pvalue(data)
    return np.random.random()


print(test(data1))
print(test(removeLowest(data1)))

pvalues = [attempt() for t in range(200)]
print(pvalues[:20])
# The values you get here should have (roughly) uniform distribution in [0,1].
# Note: this means that, in 20 attempts, we are likely to find one to rejecting the null hypothesis,
# even though the null hypothesis is true!
plt.hist(pvalues)

# to test whether the distribution of pvalue is indeed close to uniform distribution,
# we can use the Kolmogorov-Smirnov test:
scipy.stats.kstest(pvalues, "uniform")

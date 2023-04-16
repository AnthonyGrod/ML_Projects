import numpy as np
import matplotlib.pyplot as plt

w = np.mgrid[0:1:0.1,1:2:0.1]

data_set= np.array([1.0, 1.3, 2.6, 0, 
                   2.2, 1.1, 1.2, 1, 
                   2.0, 2.4, 3.8, 1,
                   1.5, 3.2, 2.1, 0,
                   3.2, 1.2, 4.2, 1])

data_set_2D = data_set.reshape((5, 4))
data_set_2D_AB = data_set_2D[:, [0, 1, 3]]
data_set_2D_BC = data_set_2D[:, [1, 2, 3]]

res_AB = np.zeros((10, 10))
res_BC = np.zeros((10, 10))

def calculate_MSE(data_set_variant, res_arr):
    res_arr += (data_set_variant[k][2] - (1 / (1 + np.exp(-(w[0,:,:]*data_set_variant[k][0] + w[1,:,:]*data_set_variant[k][1])))))**2


def plot_graph(res_arr, name):
    res_arr /= 5
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    ax.set(title='Medium Squared Error' + name,
       zlabel='MSE', xlabel='w0', ylabel='w1')
    ax.plot_surface(w[0,:,:], w[1,:,:], res_arr)
    plt.show()


# For each measurement
for k in range(5):
    calculate_MSE(data_set_2D_AB, res_AB)
    calculate_MSE(data_set_2D_BC, res_BC)

print(res_AB.min() / 5)
print(res_BC.min() / 5)

plot_graph(res_AB, " of AB dataset")
plot_graph(res_BC, " of BC dataset")


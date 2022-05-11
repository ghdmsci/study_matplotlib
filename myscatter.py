# load library
import matplotlib.pyplot as plt
import numpy as np


def plot():
    # スタイルを指定
    plt.style.use('_mpl-gallery')

    # make the data
    # indicate a seed value (=3)
    np.random.seed(3)

    # number of samples = 24
    num = 24

    x = 4 + np.random.normal(0, 2, num)
    y = 4 + np.random.normal(0, 2, num)
    # size and color:
    sizes = np.random.uniform(15, 80, num)
    colors = np.random.uniform(15, 80, num)

    # plot
    fig, ax = plt.subplots()

    ax.scatter(x, y, s=sizes, c=colors, vmin=0, vmax=100)

    ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
           ylim=(0, 8), yticks=np.arange(1, 8))

    plt.show()


if __name__ == '__main__':
    plot()
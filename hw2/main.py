import numpy as np
import matplotlib.pyplot as plt
from numpy.random import default_rng

rng = default_rng()

theta = 1.0


def uniform_sko(max_k, n, experiment_num):
    sko = []
    for k in range(1, max_k):
        diff = 0.0
        for i in range(experiment_num):
            m_k = 0.0
            sample_uni = rng.uniform(0, theta, n)
            for x in sample_uni:
                m_k += (x ** k) / n
            th_ = ((k + 1) * m_k) ** (1 / k)
            diff += (th_ - theta) ** 2
        sko.append(diff / experiment_num)
    return sko


def draw_uniform(max_k, n=1000, experiment_num=1000):
    y = uniform_sko(max_k, n, experiment_num)
    k = np.arange(1, max_k, 1)
    plt.plot(k, y)
    plt.savefig("uni.png")
    plt.show()


def exp_sko(max_k, n, experiment_num):
    sko = []
    for k in range(1, max_k):
        diff = 0.0
        for i in range(experiment_num):
            m_k = 0.0
            sample_exp = rng.exponential(theta, n)
            for x in sample_exp:
                m_k += (x ** k) / n
            th_ = (m_k / np.math.factorial(k)) ** (1 / k)
            diff += (th_ - theta) ** 2
        sko.append(diff / experiment_num)
    return sko


def draw_exp(max_k, n=300, experiment_num=1000):
    y = exp_sko(max_k, n, experiment_num)
    k = np.arange(1, max_k, 1)
    plt.plot(k, y)
    plt.savefig("exp.png")
    plt.show()


if __name__ == "__main__":
    #draw_uniform(200)
    draw_exp(100)

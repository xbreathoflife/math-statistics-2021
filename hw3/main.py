import numpy as np
import matplotlib.pyplot as plt
import heapq

experiment_num = 200
bank_windows = [100, 500, 1000]
alphas = [0.5, 1, 2, 5]


def count_a(alpha, n, exp_num):
    estimation = np.zeros(n)
    for _ in range(exp_num):
        estimation += np.sort(np.random.exponential(alpha, n))
    return [x / exp_num for x in estimation]


def count_one_exp(alpha, n, queue_len):
    queue = list(np.sort(np.random.exponential(alpha, n)))
    heapq.heapify(queue)
    waiting_times = []
    for i in range(queue_len):
        waiting_times.append(heapq.heappop(queue))
        heapq.heappush(queue, np.random.exponential(alpha) + waiting_times[i])
    return waiting_times


def count_b(alpha, n, queue_len, exp_num):
    estimation = np.zeros(queue_len)
    for _ in range(exp_num):
        estimation += count_one_exp(alpha, n, queue_len)
    return [x / exp_num for x in estimation]


def show_plot_a():
    for n in bank_windows:
        for alpha in alphas:
            y = count_a(alpha, n, experiment_num)
            plt.plot(range(0, n), y, label='alpha = ' + str(alpha))
        plt.xlabel('Номер человека в очереди')
        plt.ylabel('Среднее время ожидания')
        plt.title('Каждое окно принимает максимум 2 человека: n = ' + str(n))
        plt.legend()
        plt.savefig("a" + str(n) + ".png")
        plt.show()


def show_plot_b():
    for n in bank_windows:
        queue_len = n * 2
        for alpha in alphas:
            y = count_b(alpha, n, queue_len, experiment_num)
            plt.plot(range(0, queue_len), y, label='alpha = ' + str(alpha))
        plt.xlabel('Номер человека в очереди')
        plt.ylabel('Среднее время ожидания')
        plt.title('Без ограничений: n = ' + str(n))
        plt.legend()
        plt.savefig("b" + str(n) + ".png")
        plt.show()


if __name__ == "__main__":
    show_plot_a()
    show_plot_b()

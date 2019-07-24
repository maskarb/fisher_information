import random
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


def make_bin_edges(sos, k, x):
    middle, minim, maxim = np.mean(x), min(x), max(x)
    d_x = sos * k
    middle_low_edge, middle_high_edge = middle - d_x / 2, middle + d_x / 2
    edges = [middle_low_edge, middle_high_edge]
    temp = middle_low_edge
    while temp > minim:
        temp -= d_x
        edges.append(temp)
    temp = middle_high_edge
    while temp < maxim:
        temp += d_x
        edges.append(temp)
    return sorted(edges)


def size_of_state(x, k, window_size):
    sos_temp = []
    for i in range(1 + len(x) - window_size):
        A = x[i : i + window_size]
        sos_temp.append(np.std(A, ddof=1))
    if not sos_temp:
        sos = 0
    else:
        sos = min(sos_temp) * k
    return sos


def amp_sos_fisher(x_list, bins):
    hist = np.histogram(x_list, bins=bins, density=False)
    counts = [0] + list(hist[0] / len(x_list)) + [0]
    return sum(
        [
            (np.sqrt(counts[x + 1]) - np.sqrt(counts[x])) ** 2
            for x in range(len(counts) - 1)
        ]
    )


def discrete_amp(x_list, k):
    sos = np.std(x_list, ddof=1) * k
    bins = make_bin_edges(sos, k, x_list)
    return amp_sos_fisher(x_list, bins)


def temporal_amp(x_list, k, window_size, over):
    N = len(x_list)
    sos = size_of_state(x_list, k, window_size)
    fi = []
    for i in range(0, 1 + N - window_size, over):
        temp = x_list[i : i + window_size]
        bins = make_bin_edges(sos, k, temp)
        fi.append(amp_sos_fisher(temp, bins))
    return fi


if __name__ == "__main__":
    df = pd.read_csv("cantar2019.csv")
    x = list(df["storage"])

    k = 2
    dN = 48
    over = 1
    fi = temporal_amp(x, k, dN, over)

    fig, ax1 = plt.subplots(figsize=(5, 4))
    ax1.plot(x, "k")
    ax2 = ax1.twinx()
    ax2.plot(range(dN, 1 + len(x), over), fi, "b")
    plt.show()

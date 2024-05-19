import matplotlib.pyplot as plt


def plot_lists(list1, title="sensitivity analysis for parameter", xlabel="Parameter Value", ylabel="Objective Function"):
    iterations = range(1, len(list1)+1)

    plt.plot(iterations, list1, label="D [ 2 ]")

    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.show()

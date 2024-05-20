import matplotlib.pyplot as plt


def plot_lists(array, title="Sensitivity analysis", xlabel="Parameter Value", ylabel="Objective Function"):
    iterations = range(1, len(array)+1)

    plt.plot(iterations, array)

    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()

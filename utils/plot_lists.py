import matplotlib.pyplot as plt


def plot_lists(array, xticks, title="Sensitivity analysis", xlabel="Parameter Value", ylabel="Objective Function", ):
    plt.plot(xticks, array, marker='o')

    plt.xticks(xticks)

    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()

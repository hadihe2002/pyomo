import matplotlib.pyplot as plt
import matplotlib
import numpy as np
from pyomo.environ import value


def draw_answer(model):

    fig, ax = plt.subplots(figsize=(24, 10))

    products_dict = {1: "A", 2: "B", 3: "C"}
    products_color = {1: "#339af0", 2: "#fab005", 3: "#e64980"}

    for x in model.machines:
        for y in model.products:
            start = value(model.X[x, y])
            end = value(model.Y[x, y])
            ax.barh(f'Machine {x}', width=end - start,
                    left=start, color=products_color[y])
            if (start != end):
                ax.text(start + (end - start) / 2, x-1,
                        f'{products_dict[y]}', va='center', ha='center', fontsize=18)
                ax.text(start+2, x-1, f"{start}", ha='right',
                        va='center', fontweight=700, fontsize=11)
                ax.text(end-2, x-1, f"{end}", ha='left',
                        va='center', fontweight=700, fontsize=11)

    ax.set_xlabel('Time')
    ax.set_ylabel('Machine')
    ax.set_title('Gantt Chart')

    ax.xaxis.set_ticks(np.arange(1, 100, 1))

    matplotlib.rcParams['font.family'] = ["Comic Sans MS"]

    plt.show()

import matplotlib.pyplot as plt

def add_axis():
    fig = plt.figure(figsize=(6, 4))
    ax = fig.add_subplot()
    return ax

def plot(ax, x, y, plot_color="", plot_label=None, x_label="", y_label="", title="", grid=True, legend=True):
    ax.plot(x, y, color=plot_color, linewidth=2.5, label=plot_label)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.set_title(title)
    ax.grid(grid)

    if legend: ax.legend()
    
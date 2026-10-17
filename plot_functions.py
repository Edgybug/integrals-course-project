import matplotlib.pyplot as plt

def add_axis():
    """Create a figure and its plotting axes.

    Returns:
        Matplotlib axes object for creating plots.
    """
    fig = plt.figure(figsize=(6, 4))
    ax = fig.add_subplot()
    return ax

# Simple plotting function, can be made more customizable if needed
def plot(ax, x, y, plot_color=None, plot_label=None, x_label="", y_label="", title="", grid=True, legend=True):
    """Plot data and configure the chart's appearance.

    Args:
        ax: Matplotlib axes object to plot on.
        x: Values for the x-axis.
        y: Values for the y-axis.
        plot_color: Color of the plotted line.
        plot_label: Label used in the legend.
        x_label: Label for the x-axis.
        y_label: Label for the y-axis.
        title: Chart title.
        grid: Whether to display the grid.
        legend: Whether to display the legend.
    """
    ax.plot(x, y, color=plot_color, linewidth=2.5, label=plot_label)

    # Configure the chart labels and appearance
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.set_title(title)
    ax.grid(grid)

    # Display the legend only when requested
    if legend:
        ax.legend()
    
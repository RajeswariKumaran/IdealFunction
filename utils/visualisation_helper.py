from matplotlib import pyplot as plt
from matplotlib import style

def create_line_charts(line_df, title, columns=None, scatter_plot=False, scatter_df=None):

    for name, value in line_df.items():
        # print(name, type(name), value.to_numpy(), type(value))
        if (name=='x'): 
            x = value.to_numpy()
            continue
        y = value.to_numpy()
        if (columns==None):
            plt.plot(x, y, label=name, linewidth=2)
        elif (name in columns):
            plt.plot(x, y, label=name, linewidth=2)
    if (scatter_plot==True) and (not scatter_df.empty):
        plt.scatter(scatter_df['x'], scatter_df['y'], c='green')
    plt.legend()
    plt.grid(True,color="k")
    plt.ylabel('y axis')
    plt.xlabel('x axis')
    plt.title(title)
    plt.show()
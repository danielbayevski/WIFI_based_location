import matplotlib.pyplot as plt
import matplotlib.animation as animation

from Location.models.dataModels import WifiData
from Location.models.Point import Point


def paint(figure, chosenRouter, showPoints=True):
    font = {'family': 'serif', 'color': 'darkred', 'size': 15}
    figure.set_xlim((-150, 150))
    figure.set_ylim((-150, 150))
    figure.set_ylabel('Y  axis', fontdict=font)
    figure.set_xlabel('X axis', fontdict=font)

    colors = plt.get_cmap("Accent").colors
    circle = plt.Circle((chosenRouter.originPoint.x, chosenRouter.originPoint.y), chosenRouter.distance,
                        color='r', fill=False)
    figure.add_artist(circle)
    plotPoint(figure, chosenRouter.originPoint, 'r')


# Create figure for plotting
from Location.tests.MatplotHelper import plotPoint

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
xs = []
ys = []

# Initialize communication with TMP102

# This function is called periodically from FuncAnimation
def animate(i, xs, ys):
    ax.clear()
    ax.plot(xs, ys)

    paint(figure=ax, chosenRouter=WifiData(signal=5,networkName="", bssid="13", originPoint=Point(i,i)))
    # plt.plot(temp_c, temp_c, '.', color='r')

    # Format plot
    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.30)
    plt.title('TMP102 Temperature over Time')
    plt.ylabel('Temperature (deg C)')

# Set up plot to call animate() function periodically
ani = animation.FuncAnimation(fig, animate, fargs=(xs, ys), interval=1000)
plt.show()
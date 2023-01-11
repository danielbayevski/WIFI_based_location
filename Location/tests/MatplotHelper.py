import matplotlib.pyplot as plt

from Location.models.Point import Point


def annotate(figure, point, color):
    label = f"(circle {int(point.x)},{int(point.y)})"
    figure.annotate(label,  # this is the text
                    (point.x, point.y),  # these are the coordinates to position the label
                    textcoords="offset points",  # how to position the text
                    xytext=(0, 5),  # distance from text to points (x,y)
                    fontsize=5,
                    bbox=dict(boxstyle='round,pad=0.2', fc=color, alpha=0.3),
                    ha='center')
    plt.plot(point.x, point.y, '.', color=color)

def plotPoint(figure, point : Point, color = 'r'):
    label = f"({int(point.x)},{int(point.y)})"
    figure.annotate(label,  # this is the text
                    (point.x, point.y),  # these are the coordinates to position the label
                    textcoords="offset points",  # how to position the text
                    xytext=(0, 5),  # distance from text to points (x,y)
                    fontsize=5,
                    ha='center')

    figure.plot(point.x, point.y, '.', color=color)


from Location.models.LocationPoint import LocationPoint
from Location.models.Point import Point
import Location.MathUtil as raananMath
import matplotlib.pyplot as plt
import MatplotHelper as matplotHelper

PointInsideCircle = raananMath.isPointInsideCircle(LocationPoint(Point(9, 1), 60), Point(-18, 68))
print('PointInsideCircle =', PointInsideCircle)
print(raananMath.getDistanceBetweenPoints(Point(9, 1), Point(-18, 68)) < 60)

fig, ax = plt.subplots()
font = {'family': 'serif', 'color': 'darkred', 'size': 15}

figure = ax

figure.set_xlim((-150, 150))
figure.set_ylim((-150, 150))
figure.set_ylabel('Y  axis', fontdict=font)
figure.set_xlabel('X axis', fontdict=font)

font = {'family':'serif','color':'darkred','size':15}
circle = plt.Circle((9, 1), 60,
                    color='g', fill=False)
figure.add_patch(circle)
matplotHelper.plotPoint(ax, Point(-18, 68))
plt.show()

plt.close()
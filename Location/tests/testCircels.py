# intersection circles
import math
import matplotlib.pyplot as plt
from Location.MathUtil import getCiceleIntersections


from Location.models.Point import Point


def drawIntersaction(x0, y0, r0, x1, y1, r1):
    Point0 = Point()
    Point1 = Point()
    Point0.x = x0
    Point0.y = y0
    Point1.x = x1
    Point1.y = y1

    intersections: list[Point] = getCiceleIntersections(Point0, r0, Point1, r1)
    if len(intersections):
        plt.plot([intersections[0].x,intersections[1].x],
                 [intersections[0].y,intersections[1].y], '.', color='r')


x0, y0 = 0, 0
r0 = 5
x1, y1 = 2, 2
r1 = 5

# intersecting with (x1, y1) but not with (x0, y0)
x2, y2 = -1, 0
r2 = 2.5

circle1 = plt.Circle((x0, y0), r0, color='b', fill=False)
circle2 = plt.Circle((x1, y1), r1, color='b', fill=False)
circle3 = plt.Circle((x2, y2), r2, color='b', fill=False)

fig, ax = plt.subplots()
ax.set_xlim((-10, 10))
ax.set_ylim((-10, 10))
ax.add_artist(circle1)
ax.add_artist(circle2)
ax.add_artist(circle3)

drawIntersaction(x0, y0, r0, x1, y1, r1)
drawIntersaction(x0, y0, r0, x2, y2, r2)
drawIntersaction(x1, y1, r1, x2, y2, r2)
# intersections = get_intersections(x0, y0, r0, x1, y1, r1)
# if intersections is not None:
#     i_x3, i_y3, i_x4, i_y4 = intersections
#     plt.plot([i_x3, i_x4], [i_y3, i_y4], '.', color='r')
#
# intersections = get_intersections(x0, y0, r0, x2, y2, r2)
# if intersections is not None:
#     i_x3, i_y3, i_x4, i_y4 = intersections
#     plt.plot([i_x3, i_x4], [i_y3, i_y4], '.', color='r')
#
# intersections = get_intersections(x1, y1, r1, x2, y2, r2)
# if intersections is not None:
#     i_x3, i_y3, i_x4, i_y4 = intersections
#     plt.plot([i_x3, i_x4], [i_y3, i_y4], '.', color='r')

plt.gca().set_aspect('equal', adjustable='box')


plt.show()

plt.close()

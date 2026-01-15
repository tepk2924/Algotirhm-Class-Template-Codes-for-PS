import math
from enum import IntEnum

class Result(IntEnum):
    IN = True
    OUT = False
    ON_BOUNDARY = 0.5

def Pt_In_NonConvex_Polygon(pt, polygon):
    '''
    More resistant from floating point error since this uses integer arithmetic, but with longer code.
    Boundary checking is possible.
    '''
    winding_angle = 0
    ptx, pty = pt
    for idx in range(len(polygon)):
        pt1x, pt1y = polygon[idx - 1]
        pt2x, pt2y = polygon[idx]
        pt1rx, pt1ry = pt1x - ptx, pt1y - pty
        pt2rx, pt2ry = pt2x - ptx, pt2y - pty
        winding_angle += math.atan2(pt1ry*pt2rx - pt1rx*pt2ry, pt1rx*pt2rx + pt1ry*pt2ry)
        #Boundary check. Comment out if unwanted.
        if pt1rx*pt2rx <= 0 and pt1ry*pt2ry <= 0 and pt1rx*pt2ry == pt1ry*pt2rx: return 0.5
    return not (-math.pi <= winding_angle <= math.pi)

ptA = (0, 0)
ptB = (4, 0)
polygon = [(2, -2), (2, 2), (0, 1), (-2, 2), (-2, -2), (0, -1)]

print(Pt_In_NonConvex_Polygon(ptA, polygon))
print(Pt_In_NonConvex_Polygon(ptB, polygon))

ptC = (3, 3)
polygon2 = [(0, 0), (5, 5), (0, 10)]

print(Pt_In_NonConvex_Polygon(ptC, polygon2))
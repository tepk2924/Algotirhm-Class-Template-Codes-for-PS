import cmath

complexify = lambda P: P[0] + P[1]*1j

def Pt_In_NonConvex_Polygon(pt, polygon):
    '''
    Much shorter code implementation with complex arithmetic, but with possible floating point error.
    Boundary checking is impossible.
    '''
    winding_angle = 0
    Z = complexify(pt)
    for idx in range(len(polygon)):
        Z1 = complexify(polygon[idx - 1])
        Z2 = complexify(polygon[idx])
        S1 = Z1 - Z
        S2:complex = Z2 - Z
        winding_angle += cmath.phase(S1*S2.conjugate())
    return not (-cmath.pi <= winding_angle <= cmath.pi)

ptA = (0, 0)
ptB = (2, 0)
#polygon does not need to be convex, and whether it is CCW or CW
polygon = [(1, -1), (1, 1), (0, 0.5), (-1, 1), (-1, -1), (0, -0.5)]

print(Pt_In_NonConvex_Polygon(ptA, polygon))
print(Pt_In_NonConvex_Polygon(ptB, polygon))
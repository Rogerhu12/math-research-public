"""Exact finite identities for the two isotropic three-plane moment sections.

Only Python's standard library is used. This verifies the displayed small
matrices; the proof of the full moment statement is in the linked result.
No global Jacobian-membership or additional cyclicity claim is made.
"""
from fractions import Fraction as Q
import json


def transpose(A):
    return [list(a) for a in zip(*A)]


def multiply(A, B):
    return [[sum(a * b for a, b in zip(row, col))
             for col in zip(*B)] for row in A]


def determinant3(A):
    return (A[0][0] * (A[1][1]*A[2][2]-A[1][2]*A[2][1])
            - A[0][1] * (A[1][0]*A[2][2]-A[1][2]*A[2][0])
            + A[0][2] * (A[1][0]*A[2][1]-A[1][1]*A[2][0]))


def convolution(a, b):
    c = [Q(0)] * (len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            c[i+j] += x*y
    return c


def sum_poly(xs):
    a = [Q(0)] * max(map(len, xs), default=0)
    for x in xs:
        for i, y in enumerate(x):
            a[i] += y
    return a


K = [[0,0,0,0,5,-1],[0,0,0,-32,5,-1],[0,0,54,-4,5,0],
     [0,-32,-4,-8,0,0],[5,5,5,0,0,0],[-1,-1,0,0,0,0]]

DATA = [
    dict(sign="plus", s=Q(5), p=Q(32,5), q=Q(8,5),
         C=[[279,121,608],[121,-521,-608],[608,-608,-1024]],
         psi=[[Q(-32,5),0,-1],[Q(128,5),0,-1],[-19,5,0]],
         psi_det=-160, discriminant=Q(3488,125),
         # Q(E^T (A,B,0,0,0,1)), order A^2, AB, A, B^2, B, 1.
         restricted=[279,242,65856,-521,46784,-271360]),
    dict(sign="minus", s=Q(-27), p=Q(864,5), q=Q(-864,5),
         C=[[-1769,1369,5024],[1369,-969,-5024],[5024,-5024,-1024]],
         psi=[[Q(3456,5),32,-1],[Q(3296,5),32,-1],[77,5,0]],
         psi_det=160, discriminant=Q(153684864,125),
         restricted=[-1769,2738,-16087680,-969,19820160,140341248]),
]


def verify():
    results = []
    for data in DATA:
        s,p,q,C,psi = [data[k] for k in ["s","p","q","C","psi"]]
        E = [[Q(int(i==j)) for j in range(3)] for i in range(3)]
        for k in range(3,6):
            E.append([s*E[k-1][j]-p*E[k-2][j]+q*E[k-3][j]
                      for j in range(3)])
        assert multiply(multiply(transpose(E),K),E) == [[0]*3 for _ in range(3)]
        P = [-q,p,-s,Q(1)]
        projected = multiply(transpose(E),K)
        assert projected == [convolution(P, row) for row in psi]
        conic = sum_poly([[C[i][j]*v for v in convolution(psi[i],psi[j])]
                          for i in range(3) for j in range(3)])
        assert not any(conic)
        assert determinant3(C) == 163840000
        assert determinant3(psi) == data["psi_det"]
        disc = s*s*p*p-4*p*p*p-4*s*s*s*q-27*q*q+18*s*p*q
        assert disc == data["discriminant"] != 0
        a,b,c = E[5]
        # E^T r = (A+a,B+b,c), including both symmetric off-diagonal terms.
        restriction = [C[0][0],2*C[0][1],
                       2*(C[0][0]*a+C[0][1]*b+C[0][2]*c),
                       C[1][1],2*(C[1][0]*a+C[1][1]*b+C[1][2]*c),
                       sum(C[i][j]*E[5][i]*E[5][j]
                           for i in range(3) for j in range(3))]
        assert restriction == data["restricted"]
        results.append(dict(sign=data["sign"],all_pass=True,
                            isotropic_matrix_entries=9,
                            projected_curve_coefficients=18,
                            conic_coefficients=len(conic),
                            conic_determinant=163840000,
                            quadratic_parameter_determinant=data["psi_det"],
                            cubic_discriminant=str(disc),
                            matched_candidate_coefficients=6))
    return dict(all_pass=True,sections=results,
                scope="Exact displayed finite identities. The full section theorem follows from the accompanying proof. No classification of all critical points or global Jacobian membership is claimed.")


if __name__ == "__main__":
    print(json.dumps(verify(),ensure_ascii=False,indent=2))

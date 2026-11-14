#!/usr/bin/env python3
"""R447: complete two-reference intersection and exact degree-18 tests."""
import json
from pathlib import Path
import sympy as s

folder=Path(__file__).resolve().parent
raw=json.loads((folder/'check-r443-residual-quarter-core.json').read_text())
block=s.Matrix(raw['complete_blocks']['even2']['matrix_times_252'])
b,w=s.symbols('b w',nonzero=True)
A=s.Matrix(6,4,lambda a,j:block[a,j]*b**(7-a-j)/252)
S=s.Matrix([-s.Rational(128,7)*b**4,-s.Rational(80,7)*b**3,
            -s.Rational(12,7)*b**2,-s.Rational(53,7)*b,1,0])
H3=s.Matrix([-2048*b**5,12032*b**4,8128*b**3,400*b**2,-208*b,1])
H5=s.Matrix([1024*b**5,-6784*b**4,-14912*b**3,-272*b**2,272*b,1])
c3=s.Matrix([-s.Rational(287,12)/b**2,-s.Rational(7,3)/b,
              -s.Rational(56,3),-s.Rational(448,3)*b])
c5=s.Matrix([s.Rational(28,3)/b**2,-s.Rational(28,3)/b,
              s.Rational(28,3),s.Rational(2240,3)*b])
assert s.simplify(A*c3-H3+840*b*S)==s.zeros(6,1)
assert s.simplify(A*c5-H5+672*b*S)==s.zeros(6,1)
assert A.subs(b,1).rank()==4
assert A.row_join(S).subs(b,1).rank()==5

# x(z)=z^-2*f(z^6), and log(sigma(z)/z)=ell(z^6), through degree 18.
# These coefficients follow from x''=6x^2 and (log sigma)''=-x.
f=1-b*w/7+b**2*w**2/637-b**3*w**3/84721
ell=b*w/210-b**2*w**2/84084+b**3*w**3/25924626
A18=s.exp(18*ell).series(w,0,4).removeO().expand()
T=s.zeros(4,4)
for j in range(4):
    series=(A18*f**(3*j)).series(w,0,4).removeO().expand()
    for k in range(4):
        degree=k-3+j
        if degree>=0:
            T[k,j]=s.factor(series.coeff(w,degree))
assert T.det()==1
expected=s.Matrix([[0,0,0,1],[0,0,1,-6*b/5],
    [0,1,-27*b/35,1236*b**2/1925],
    [1,-12*b/35,43011*b**2/175175,-2997734*b**3/14889875]])
assert T==expected
h3=s.simplify(T.T.inv()*c3)
h5=s.simplify(T.T.inv()*c5)
expected3=s.Matrix([-4031937*b/s.Integer(23375),-s.Rational(6282301,300300),
                   -s.Rational(158,15)/b,-s.Rational(287,12)/b**2])
expected5=s.Matrix([17654112*b/s.Integer(23375),s.Rational(173444,75075),
                   -s.Rational(92,15)/b,s.Rational(28,3)/b**2])
assert h3==expected3 and h5==expected5
G=s.Matrix([-32*b**3,-144*b**2,-30*b,1])
assert s.factor((G.T*c3)[0])==1512*b
assert s.factor((G.T*c5)[0])==1512*b
for row in list(T)+list(h3)+list(h5):
    denominator=s.denom(s.factor(row))
    numeric=denominator.subs(b,1)
    assert all(p<=19 for p in s.factorint(numeric))
print('complete arithmetic intersections: exact')
print('divided-power moment determinant:',T.det())
print('h3 divided-power coefficients:',list(h3))
print('h5 divided-power coefficients:',list(h5))
print('both G18 integrals:',1512*b)

def strings(mat):
    return [[str(s.factor(v)) for v in row] for row in mat.tolist()]
report={
 'field':'QQ(b); b=17 in the original source',
 'scope':'complete six-coordinate identities and exact moments through degree 18',
 'intersection_basis':[
     {'source':'H3-840*b*S','A_coefficients':strings(c3)},
     {'source':'H5-672*b*S','A_coefficients':strings(c5)}],
 'divided_power_moment_matrix':strings(T),
 'moment_matrix_determinant':1,
 'h3_divided_power_coefficients':strings(h3),
 'h5_divided_power_coefficients':strings(h5),
 'G18_integral_both':'1512*b',
 'full_principal_rank':4,
 'rank_with_original_S':5,
 'intersection_with_S_H3_H5_dimension':2,
 'all_denominator_primes_at_most':19}
dest=Path(__file__).with_suffix('.json')
dest.write_text(json.dumps(report,indent=2)+'\n')
print('saved',dest)

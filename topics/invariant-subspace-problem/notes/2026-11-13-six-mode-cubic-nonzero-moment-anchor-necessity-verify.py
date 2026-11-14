"""Six exact complete critical points forcing the two original anchor quadrics.

All 33 original critical equations are checked in two rational cubic quotient
algebras.  No numerical root approximations or finite-field zero tests are used
for these identities.  Reduction modulo 103 certifies only NONZERO rational
determinants and separability of the two cubic parameter polynomials.
"""
from fractions import Fraction as Q
from pathlib import Path
import importlib.util
import itertools
import json

folder=Path(__file__).parent
data=json.loads((folder/'2026-11-13-six-mode-cubic-nonzero-moment-anchor-necessity-data.json').read_text())
path=folder/'2026-11-13-six-mode-cubic-local-jacobian-cube-verify.py'
spec=importlib.util.spec_from_file_location('original_six_mode_cubic',path)
alg=importlib.util.module_from_spec(spec)
spec.loader.exec_module(alg)
original_qh=[[z.d.get((0,0),Q(0)) for z in row] for row in alg.QH]


def quotient_class(relation):
    class E:
        def __init__(self,x=0):
            if isinstance(x,E):self.a=x.a
            elif isinstance(x,(list,tuple)):self.a=tuple(map(Q,x))
            else:self.a=(Q(x),Q(0),Q(0))
            assert len(self.a)==3
        def __add__(self,b):
            b=E(b);return E([x+y for x,y in zip(self.a,b.a)])
        __radd__=__add__
        def __neg__(self):return E([-x for x in self.a])
        def __sub__(self,b):return self+-E(b)
        def __rsub__(self,b):return E(b)+-self
        def __mul__(self,b):
            b=E(b);c=[Q(0)]*5
            for i in range(3):
                for j in range(3):c[i+j]+=self.a[i]*b.a[j]
            for k in [4,3]:
                for j in range(3):c[k-3+j]-=c[k]*relation[j]
            return E(c[:3])
        __rmul__=__mul__
        def __truediv__(self,b):return self*Q(1,b)
        def __pow__(self,n):
            out=E(1);base=self
            while n:
                if n%2:out=out*base
                base=base*base;n//=2
            return out
        def __bool__(self):return any(self.a)
        def __eq__(self,b):return self.a==E(b).a
    return E


def determinant3(A):
    return (A[0][0]*(A[1][1]*A[2][2]-A[1][2]*A[2][1])
            -A[0][1]*(A[1][0]*A[2][2]-A[1][2]*A[2][0])
            +A[0][2]*(A[1][0]*A[2][1]-A[1][1]*A[2][0]))


def residue(x):
    x=Q(x);assert x.denominator%103
    return x.numerator%103*pow(x.denominator%103,-1,103)%103


def verify_plane(plane):
    f=list(map(Q,plane['parameter_polynomial_integer_ascending']))
    f=[x/f[-1] for x in f]
    E=quotient_class(f[:3])
    rec=list(map(Q,plane['recurrence']))
    def tail(head,length):
        result=[E(x) for x in head]
        while len(result)<length:
            result.append(sum((rec[j]*result[-j-1] for j in range(3)),E()))
        return result
    y=tail(plane['mean_head'],6)
    H=tail(plane['second_moment_head'],11)
    V=tail(plane['third_cumulant_head'],16)
    linear=[E(x) for x in plane['conic_linear_factor']]
    C=plane['conic_matrix']
    assert y[0]==1 and y[1]==0 and y[2]==E([0,1,0])
    # Exact tensor identity T3=Q*L in the first-three-coordinate plane chart.
    for i,j,k in itertools.product(range(3),repeat=3):
        left=y[i]*y[j]*y[k]-2*(y[i]*H[j+k]+y[j]*H[i+k]+y[k]*H[i+j])+4*V[i+j+k]
        right=(C[i][j]*linear[k]+C[i][k]*linear[j]+C[j][k]*linear[i])/3
        assert left==right
    # Transport the original, already published full R3 matrix formula to this
    # finite rational coefficient algebra; no polynomial formula is changed.
    alg.P=E
    alg.QH=[[E(x) for x in row] for row in original_qh]
    R,gradient,ell=alg.formula(y+H)
    assert not R
    assert len(gradient)==17 and all(not x for x in gradient)
    third_equations=[x+4*z for x,z in zip(alg.mv(alg.Ji,ell),V)]
    assert len(third_equations)==16 and all(not x for x in third_equations)
    # Since J3 is invertible, these are exactly the sixteen original V-gradient
    # equations.  At Z=0 the other seventeen original gradients equal grad R3.
    bell_e0=y[0]**3-6*y[0]*H[0]+4*V[0]
    assert bell_e0==C[0][0]*linear[0] and bell_e0
    L=[[Q(x) for x in row] for row in plane['conic_linear_factor']]
    det=determinant3(L)
    assert det
    ff=[residue(x) for x in f]
    c,b,a,_=ff
    discriminant=(a*a*b*b-4*b**3-4*a**3*c-27*c*c+18*a*b*c)%103
    assert discriminant
    lmod=[[residue(x) for x in row] for row in L]
    determinant_mod=residue(det)
    expected={
        'plus':([97,11,96,1],[[91,80,20],[13,6,89],[54,85,76]],33),
        'minus':([24,38,36,1],[[22,96,66],[59,47,98],[21,39,17]],61)
    }[plane['name']]
    assert (ff,lmod,determinant_mod)==expected
    assert determinant3(C)==163840000
    return dict(name=plane['name'],all_pass=True,
                exact_reduced_gradient_zeros=17,exact_third_moment_gradient_zeros=16,
                exact_value_zero=True,exact_conic_times_linear_tensor_checks=27,
                parameter_monic_polynomial_mod103=ff,
                parameter_discriminant_mod103=discriminant,
                linear_coefficient_matrix_mod103=lmod,
                linear_coefficient_determinant_mod103=determinant_mod,
                bell_e0_coefficient_vector_mod103=[residue(x) for x in bell_e0.a],
                conic_determinant=163840000)


def verify():
    return dict(all_pass=True,planes=[verify_plane(x) for x in data['planes']],
                scope="Six exact complete critical points. Their ordinary third moments are nonzero and force both original conic conditions on any direction whose matching Bell power belongs to the global Jacobian ideal. This is a necessary condition, not a global membership or cyclicity theorem.")


if __name__=='__main__':
    print(json.dumps(verify(),ensure_ascii=False,indent=2))

#!/usr/bin/env python3
"""R446: exact three-state residual quarter closure and complete carry.

This uses the complete QQ(sqrt(3)) polynomial model, including odd-odd terms.
It does not run or modify the R443 script or its certificate.
"""
from pathlib import Path
import json

folder = Path(__file__).resolve().parent
source = (folder / 'check-r443-residual-quarter-core.py').read_text()
exec(source.split('out=[R2.zero for _ in range(4)]')[0])
report443 = json.loads((folder / 'check-r443-residual-quarter-core.json').read_text())

def read_terms(rows):
    return R2.from_dict({(d['x'], d['z']): K.convert(QQ(d['coefficient'])) for d in rows})

K1even = read_terms(report443['K1_even_terms'])
K1odd = read_terms(report443['K1_oddodd_terms'])
A1even, rem0 = K1even.div(zz-xx)
A1odd, rem1 = K1odd.div(zz-xx)
assert rem0 == rem1 == R2.zero

# f R_t y_t, where tau=f*y and f^2=F.  Use x'=2y and y'=3x^2.
base = num[0]
rt_yf = divide(mul(rt,
    (2*tau2*den.diff(x)-3*F*x*x*den,
     base.diff(x)*den-base*den.diff(x))), den**2)

def translated_odd_monomial(N, i):
    half = i//2
    if i%2:
        return mul(mul(mul(rt_yf, power(rt_x2,half)), rt_x),
                   power(rt,N//4-half-2))
    return mul(mul(rt_yf,power(rt_x2,half)),power(rt,N//4-half-1))

M32odd = [translated_odd_monomial(32,i) for i in range(15)]
M16odd = [translated_odd_monomial(16,j) for j in range(7)]
e32 = [tuple(embed(v,0) for v in a) for a in M32]
e16 = [tuple(embed(v,1) for v in a) for a in M16]
o32 = [tuple(embed(v,0) for v in a) for a in M32odd]
o16 = [tuple(embed(v,1) for v in a) for a in M16odd]

def rational(c):
    terms=c.to_list()
    assert len(terms)<=1, ('nonrational transport',terms)
    return Fraction(str(terms[-1])) if terms else Fraction(0)

def angular_three(poly):
    return R2.from_dict({ij:3*c for ij,c in poly.items() if sum(ij)%3==1})

def quarter_average(even, odd):
    """D_minus applied to even + y1*y2*odd in the anti-diagonal E2 fixed space."""
    out=[R2.zero for _ in range(4)]
    for (i,j),c in even.items():
        aa,ab=e32[i];ba,bb=e16[j]
        out[0]+=c*aa*ba
        out[1]-=c*aa*bb
        out[2]+=c*ab*ba
        out[3]-=c*ab*bb
    for (i,j),c in odd.items():
        aa,ab=o32[i];ba,bb=o16[j]
        # T_t(y*x^i)=(aa+tau*ab)/f,
        # T_-t(y*x^j)=(-ba+tau*bb)/f.
        out[0]-=c*aa*ba/F
        out[1]+=c*aa*bb/F
        out[2]-=c*ab*ba/F
        out[3]+=c*ab*bb/F
    out=[p*kappa_t**6 for p in out]
    assert out[1]==out[2]==R2.zero
    out[3]*=F
    for p in (out[0],out[3]):
        for c in p.values(): rational(c)
    return (even+angular_three(out[0]))/2,(odd+angular_three(out[3]))/2

# D_minus^2 A0=A0 is a direct nontrivial check of the odd lift signs.
back_even,back_odd=quarter_average(A1even,A1odd)
assert back_even==A and back_odd==R2.zero
print('D_minus^2 A0 = A0 (complete canonical polynomial)',flush=True)

# D_plus A0=R_Y A1.  Its second D_minus image is the fourth possible state.
A2even,A2odd=quarter_average(A1even,-A1odd)
assert A2odd==R2.zero
K0=(zz-xx)*A
K2=(zz-xx)*A2even
print('D_minus D_plus A0 is separately even',flush=True)

def coefficient_matrix(polys):
    indices=sorted(set().union(*(p.keys() for p in polys)))
    return sp.Matrix([[sp.Rational(str(rational(p.get(ij,K.zero))))
                       for p in polys] for ij in indices])

rank=coefficient_matrix([K0,K1even,K2]).rank()
print('rank(K0, even(K1), K2) =',rank,flush=True)
if rank<3:
    print('relations:',coefficient_matrix([K0,K1even,K2]).nullspace(),flush=True)

def terms(poly):
    return [{'x':i,'z':j,'coefficient':str(rational(c))}
            for (i,j),c in sorted(poly.items())]

def to_sympy(poly):
    sx,sz=sp.symbols('x z')
    return sum(sp.Rational(str(rational(c)))*sx**i*sz**j for (i,j),c in poly.items())

print('K2 factored:',sp.factor(to_sympy(K2)),flush=True)
principal=R2.from_dict({ij:c for ij,c in K2.items() if ij[0]%3==2})
print('K2 principal factored:',sp.factor(to_sympy(principal)),flush=True)
dest=folder/'check-r446-three-state-quarter-and-carry.json'
dest.write_text(json.dumps({
    'field':'QQ(sqrt(3)); rational final coefficients',
    'canonical_Dminus_square_identity':True,
    'second_state_separately_even':True,
    'span_rank_K0_evenK1_K2':rank,
    'K2_even_terms':terms(K2),
    'K2_principal_terms':terms(principal),
    'relations':[[str(c) for c in v]
                 for v in coefficient_matrix([K0,K1even,K2]).nullspace()]
},indent=2)+'\n')
print('saved',dest)

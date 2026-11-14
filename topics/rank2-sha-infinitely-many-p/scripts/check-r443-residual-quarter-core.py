#!/usr/bin/env python3
"""R443: exact residual quarter core on S32 tensor S16.

Complete polynomial transport in QQ(sqrt(3))[x,t]/(t^2=F*(x^3+1)).
No target-prime scan and no point interpolation.
"""
import json
from fractions import Fraction
from pathlib import Path
import sympy as sp
from sympy.polys.domains import QQ
from sympy.polys.rings import ring

K = QQ.algebraic_field(sp.sqrt(3))
R, x = ring("x", K)
R2, xx, zz = ring("x,z", K)
q = K.from_sympy(1 + sp.sqrt(3))
F = -6*q - 3
kappa_t = (1-q)/(12*F)
tau2 = F*(x**3+1)
one, zero = R.one, R.zero
rat = lambda a,b=1: K.convert(QQ(a,b))

def add(a,b): return a[0]+b[0],a[1]+b[1]
def scale(a,c): return a[0]*c,a[1]*c
def mul(a,b):
    return a[0]*b[0]+a[1]*b[1]*tau2,a[0]*b[1]+a[1]*b[0]
def power(a,n):
    out=one,zero
    while n:
        if n&1: out=mul(out,a)
        a=mul(a,a)
        n//=2
    return out
def divide(a,d):
    qa,ra=a[0].div(d);qb,rb=a[1].div(d)
    assert ra==rb==zero
    return qa,qb

# R_t=(normalized sigma_t/sigma)^4, including the actual quarter tangent.
rt=(x*x-q*q*x-2*q,rat(2,3)*(1-q)*one)
assert mul(rt,(rt[0],-rt[1])) == ((x+q)**4,zero)
num=(-q*x*x+q*q*x+2,-2*one)
den=(x+q)**2
rt_x=divide(mul(rt,num),den)
rt_x2=divide(mul(rt,mul(num,num)),den**2)
def translated_monomial(N,i):
    half=i//2
    if i%2:
        return mul(mul(power(rt_x2,half),rt_x),power(rt,N//4-half-1))
    return mul(power(rt_x2,half),power(rt,N//4-half))

M32=[translated_monomial(32,i) for i in range(17)]
M16=[translated_monomial(16,j) for j in range(9)]
def embed(poly,axis):
    return R2.from_dict({(i,0) if axis==0 else (0,i):c for (i,),c in poly.items()})

M0=[[512,-128,224],[-128,-832,1024],[224,1024,206]]
M12=[[-2432,-256,16],[-256,1144,-4],[16,-4,7]]
B=R2.zero
for i in range(3):
    for j in range(3):
        B+=M0[i][j]*xx**(3*i)*zz**(3*j)
        B+=M12[i][j]*xx**(1+3*i)*zz**(2+3*j)
        B+=M12[i][j]*xx**(2+3*j)*zz**(1+3*i)
G16=xx*(xx**3+1)*(xx**3-8)
A=rat(-2,21)*G16*B
out=[R2.zero for _ in range(4)]
e32=[tuple(embed(v,0) for v in a) for a in M32]
e16=[tuple(embed(v,1) for v in a) for a in M16]
for (i,j),c in A.items():
    aa,ab=e32[i];ba,bb=e16[j]
    out[0]+=c*aa*ba
    out[1]-=c*aa*bb
    out[2]+=c*ab*ba
    out[3]-=c*ab*bb
out=[p*kappa_t**6 for p in out]
assert out[1]==out[2]==R2.zero  # t and -t differ by the true E2 stabilizer.
# tau_y*tau_v=F*y(y)*y(v).
out[3]*=F
def rational(c):
    terms=c.to_list()
    assert len(terms)<=1, ("nonrational quarter transport",terms)
    return Fraction(str(terms[-1])) if terms else Fraction(0)
for p in (out[0],out[3]):
    for c in p.values(): rational(c)

def angular_three(poly):
    return R2.from_dict({ij:3*c for ij,c in poly.items() if sum(ij)%3==1})
A1even=(A+angular_three(out[0]))/2
A1odd=angular_three(out[3])/2
K0=(zz-xx)*A
K1even=(zz-xx)*A1even
K1odd=(zz-xx)*A1odd

# First principal mu6 projection: sigma^34*x^i has type zero iff i=2 mod3.
principal=R2.from_dict({(i,j):c for (i,j),c in K1even.items() if i%3==2})
S=xx**2*(xx**3+1)*(xx**3-8)*(xx**6-rat(4,7)*xx**3+rat(16,7))
G=zz**9-30*zz**6-144*zz**3-32
C=G16*(xx**9-30*xx**6-144*xx**3-32)
FF=zz*(zz**6-rat(4,7)*zz**3+rat(16,7))
assert K0==rat(-2,3)*(S*G-C*FF)

def sympy(poly):
    return sum(sp.Rational(rational(c).numerator,rational(c).denominator)
               *sp.Symbol("x")**i*sp.Symbol("z")**j for (i,j),c in poly.items())
def terms(poly):
    return [{"x":i,"z":j,"coefficient":str(rational(c))}
            for (i,j),c in sorted(poly.items())]

print("K1 even bidegrees",K1even.degree(xx),K1even.degree(zz))
print("K1 odd bidegrees",K1odd.degree(xx),K1odd.degree(zz))
print("K1 even factor",sp.factor(sympy(K1even)))
print("K1 odd factor",sp.factor(sympy(K1odd)))
print("principal factor",sp.factor(sympy(principal)))
print("Y marginal factor",sp.factor(sympy(R2.from_dict({(i,0):c for (i,j),c in K1even.items() if j==9}))))
report={"field":"QQ(sqrt(3)); all final coefficients rational",
        "scope":"complete canonical four-torsion transport",
        "quarter_even_terms":terms(out[0]),"quarter_oddodd_terms":terms(out[3]),
        "K1_even_terms":terms(K1even),"K1_oddodd_terms":terms(K1odd),
        "principal_first_axis_terms":terms(principal),
        "opposite_odd_parts_zero":True}
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ
blocks={}
expected_smith={
 "even0":[1,1944,31104],"even1":[1,5832,93312],
 "even2":[1,3,31104,279936],"odd0":[12,3456],
 "odd1":[12,864,373248],"odd2":[48,3456,746496]}
for label,poly,rows,cols in (("even",K1even,18,10),("odd",K1odd,16,8)):
    full=sp.Matrix([[252*sp.Rational(str(rational(poly.get((i,j),K.zero))))
                     for j in range(cols)] for i in range(rows)])
    for residue in range(3):
        rr=list(range(residue,rows,3))
        cc=[j for j in range(cols) if (residue+j)%3==2]
        block=full.extract(rr,cc)
        smith=smith_normal_form(block,domain=ZZ)
        diagonal=[int(abs(smith[i,i])) for i in range(len(cc))]
        assert diagonal==expected_smith[label+str(residue)]
        blocks[label+str(residue)]={"rows":rr,"columns":cc,
              "matrix_times_252":[[int(c) for c in row] for row in block.tolist()],
              "smith_diagonal":diagonal}
principal_matrix=sp.Matrix(blocks["even2"]["matrix_times_252"])
augmented=principal_matrix.row_join(sp.Matrix([-128,-80,-12,-53,7,0]))
smith=smith_normal_form(augmented,domain=ZZ)
aug_diagonal=[int(abs(smith[i,i])) for i in range(5)]
assert aug_diagonal==[1,1,81,31104,120932352]
report.update({"complete_blocks":blocks,"full_tensor_rank":18,
               "even_tensor_rank":10,"odd_tensor_rank":8,
               "principal_rank":4,"principal_with_original_S_rank":5,
               "principal_with_7S_smith_diagonal":aug_diagonal})
dest=Path(__file__).with_suffix(".json")
dest.write_text(json.dumps(report,indent=2)+"\n")
print("saved",dest)


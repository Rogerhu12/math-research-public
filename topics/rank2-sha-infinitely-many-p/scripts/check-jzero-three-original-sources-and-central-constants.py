#!/usr/bin/env python3
"""R307: three actual sextic sources, their central constants and connection.

The published R297 full CM13 matrix is the fixed input for the three source
lines.  The conductor-17 Weber polynomial and CM7 map are rebuilt from the
division recursion.  No numerical recognition, target-prime scan, or scratch
file is used.  The companion's complete odd CM13 block has its own certificate
check-jzero-odd-cm13-companion.py.
"""
from pathlib import Path
from fractions import Fraction
import json
import sympy as s
from sympy.polys.matrices import DomainMatrix
from flint import fmpq, fmpq_poly

checks=[]
def check(name, condition):
    assert condition, name
    checks.append(name)

base=Path(__file__).parent
old=json.loads((base/'check-jzero-actual-cm13-matrix-and-theta-source.json').read_text())
delta=s.sqrt(-3);omega=(-1+delta)/2;gamma=(7+delta)/2
field=s.QQ.algebraic_field(delta)
D=s.diag(*[s.Rational(1,4**j) for j in range(6)])
M=D*(s.Matrix(old['integer_matrix_real'])+delta*s.Matrix(old['integer_matrix_delta']))*D.inv()/old['integer_matrix_denominator']
M=M.applyfunc(s.expand)
X,b=s.symbols('X b',nonzero=True)
P={1:X**4-s.Rational(53,7)*b*X**3-s.Rational(12,7)*b**2*X**2-s.Rational(80,7)*b**3*X-s.Rational(128,7)*b**4,
   3:X**5-208*b*X**4+400*b**2*X**3+8128*b**3*X**2+12032*b**4*X-2048*b**5,
   5:X**5+272*b*X**4-272*b**2*X**3-14912*b**3*X**2-6784*b**4*X+1024*b**5}
out={'status':'PASS','curve':'common frame y^2=x^3+b; target b=17',
     'actual_twists':{'1':17,'3':4913,'5':1419857},'sources':{}}
for k in (1,3,5):
    poly=s.Poly(P[k].subs(b,1),X)
    v=s.Matrix([poly.nth(j) for j in range(6)])
    eigen=s.expand(-gamma*omega**(k-1))
    check(f'original full CM13 source eigenvector k={k}',(M*v-eigen*v).applyfunc(s.simplify)==s.zeros(6,1))
    rank=len(DomainMatrix.from_Matrix(M-eigen*s.eye(6)).convert_to(field).rref()[1])
    check(f'original CM13 eigenline is simple k={k}',rank==5)
    out['sources'][str(k)]={'P_b1_ascending':[str(a) for a in v],
       'P_general_b':str(P[k]),'CM13_eigenvalue':str(eigen),
       'mass':int(v[5]),'origin_order':6 if k==1 else 0}
check('three actual source columns are independent',s.Matrix.hstack(*[s.Matrix([s.Poly(P[k].subs(b,1),X).nth(j) for j in range(6)]) for k in (1,3,5)]).rank()==3)

# The actual first-order connection, with all of its origin and T_pm edges.
L=lambda R:s.expand(6*X*(X+b)*s.diff(R,X)-(25*X+28*b)*R)
L1=s.Matrix([[s.Poly(L(X**j).subs(b,1),X).nth(i) for j in range(5)] for i in range(6)])
ell=s.Matrix([[-6175,6916,-8008,9856,-14080,56320]])
check('natural connection is injective of rank five',L1.rank()==5)
check('primitive actual de Rham cokernel',ell*L1==s.zeros(1,5))
check('holomorphic differential has normalized cokernel',ell[5]==56320)
conn={}
for k in (1,3,5):
    pv=s.Matrix([s.Poly(P[k].subs(b,1),X).nth(j) for j in range(6)])
    cls=s.cancel((ell*pv)[0]/ell[5])
    rhs=pv-s.Matrix([0,0,0,0,0,cls])
    rv=L1[:5,:].inv()*rhs[:5,:]
    R1=sum(rv[j]*X**j for j in range(5))
    check(f'full six-column de Rham reduction k={k}',L1*rv==rhs)
    Rb=s.expand(b**(3 if k==1 else 4)*R1.subs(X,X/b))
    cb=cls/b if k==1 else cls
    check(f'actual common b connection k={k}',s.expand(L(Rb)+cb*X**5-P[k])==0)
    check(f'origin first derivative and mass k={k}',s.expand(-s.Poly(Rb,X).nth(4)-(int(pv[5])-cb))==0)
    conn[str(k)]={'ell_P':str((ell*pv)[0]),'class_b1':str(cls),'class_common_b':str(cb),
       'R_b1_ascending':[str(a) for a in rv],'R_common_b':str(Rb),
       'companion_origin_derivative':str(int(pv[5])-cb)}
check('two reference cokernels coprime away from two and three',s.igcd(37698048,59719680)==373248)
check('H3 and H5 exact cohomology combination',160*s.Rational(conn['3']['class_b1'])==101*s.Rational(conn['5']['class_b1']))
a13=-s.Rational(37,33936)/b;a15=-s.Rational(37,53760)/b
check('actual H1-H3 companion coefficient',s.simplify(s.sympify(conn['1']['class_common_b'],locals={'b':b})/s.sympify(conn['3']['class_common_b'],locals={'b':b})-a13)==0)
check('actual H1-H5 companion coefficient',s.simplify(s.sympify(conn['1']['class_common_b'],locals={'b':b})/s.sympify(conn['5']['class_common_b'],locals={'b':b})-a15)==0)
out['connection']={'L_matrix_b1':[[str(a) for a in row] for row in L1.tolist()],
 'ell_primitive':[int(a) for a in ell], 'sources':conn,
 'a13':str(a13),'a15':str(a15),'reference_exact_combination':'160*H3-101*H5',
 'reference_combination_origin_mass':59}

# A complete fixed conductor-17 Kronecker calculation at weight zero.
# psi_even=2*y*f_even in the ordinary division recurrence.
t=fmpq_poly([0,1]);V=t**3+1
fs={0:fmpq_poly([0]),1:fmpq_poly([1]),2:fmpq_poly([1]),
    3:3*t**4+12*t,4:2*(t**6+20*t**3-8)}
def dp(n):
    if n in fs:return fs[n]
    m=n//2
    if n%2:
        a=dp(m+2)*dp(m)**3;c=dp(m-1)*dp(m+1)**3
        if m%2==0:a*=16*V**2
        else:c*=16*V**2
        z=a-c
    else:z=dp(m)*(dp(m+2)*dp(m-1)**2-dp(m-2)*dp(m+1)**2)
    fs[n]=z
    return z
div17=dp(17)
check('original 17-division polynomial has Weber degree 48',div17.degree()==144 and all(not div17[j] for j in range(145) if j%3))
P48=fmpq_poly([div17[3*j]/17 for j in range(49)])
check('original Weber algebra is etale',P48.gcd(P48.derivative()).degree()==0)
class K:
    def __init__(self,a=0,b=0):
        if isinstance(a,K):self.a,self.b=a.a,a.b;return
        def cv(c):return c%P48 if isinstance(c,fmpq_poly) else fmpq_poly([fmpq(c)])
        self.a,self.b=cv(a),cv(b)
    def __add__(self,b):
        b=K(b);return K(self.a+b.a,self.b+b.b)
    __radd__=__add__
    def __neg__(self):return K(-self.a,-self.b)
    def __sub__(self,b):return self+-K(b)
    def __rsub__(self,b):return K(b)-self
    def __mul__(self,b):
        b=K(b);return K(self.a*b.a-3*self.b*b.b,self.a*b.b+self.b*b.a)
    __rmul__=__mul__
    def __truediv__(self,b):
        b=K(b);norm=(b.a*b.a+3*b.b*b.b)%P48;g,iv,_=norm.xgcd(P48)
        assert g==1,'every original denominator must be invertible'
        return self*K((b.a*iv)%P48,(-b.b*iv)%P48)
    def __pow__(self,n):
        if n<0:return (K(1)/self)**(-n)
        r,a=K(1),self
        while n:
            if n&1:r=r*a
            a=a*a;n//=2
        return r
    def __eq__(self,b):
        b=K(b);return self.a==b.a and self.b==b.b
    def comp(self,v):
        a,b=K(0),K(0)
        for j in range(47,-1,-1):a=a*v+K(self.a[j]);b=b*v+K(self.b[j])
        return a+dd*b
    def out(self):return [[str(c) for c in a] for a in (self.a,self.b)]
tt=K(fmpq_poly([0,1]));dd=K(0,1);ww=(dd-1)/2;gg=2-ww;lam=-ww*ww
cc=-(2+6*dd)/7
UU=tt*tt+(12-28*cc)*tt+7*cc*cc-24*cc
phi=tt*UU**3/(gg**6*(tt+cc)**6)
evalP=K(0)
for j in range(48,-1,-1):evalP=evalP*phi+K(P48[j])
check('actual CM7 Weber map preserves division algebra',evalP==0)
R0=6*ww*ww*(tt+4)/(tt-8)
xs=s.symbols('x')
mu6_trace=6*omega**2+sum(6/(omega**j*xs-2*omega) for j in range(3))
check('full six-unit Kronecker zero-weight trace',s.cancel(mu6_trace-6*omega**2*(xs**3+4)/(xs**3-8),extension=delta)==0)
def fm(a,b):return ((a[0]*b[0]-3*a[1]*b[1])%17,(a[0]*b[1]+a[1]*b[0])%17)
def fp(a,n):
    r=(1,0)
    while n:
        if n&1:r=fm(r,a)
        a=fm(a,a);n//=2
    return r
gmod=(11,8)
check('true CM7 element generates the 288 residue units',fp(gmod,288)==(1,0) and fp(gmod,144)!=(1,0) and fp(gmod,96)!=(1,0))
check('actual CM7 tame character is minus omega square',fp(gmod,48)==(9,9))
check('original two-three CRT sign for every odd twist',fp((0,2),48)==(16,0))
res={k:K(0) for k in (1,3,5)};cur=R0
for j in range(48):
    for k in res:res[k]+=lam**(k*j)*cur
    cur=cur.comp(phi)
check('all forty-eight actual Weber translates close',cur==R0)
constants={1:0,3:3,5:6}
out['Kronecker']={'original_Weber_P48':[str(a) for a in P48],
 'actual_CM7_Weber_map':phi.out(),'six_unit_trace':'6*omega^2*(t+4)/(t-8)',
 'CRT_formula':'L(psi_k,1)/Omega_k=-17^(k/6)*s*R_k/(34*delta)',
 'resolvents':{}}
for k in (1,3,5):
    check(f'original resolvent finite character k={k}',res[k].comp(phi)==lam**(-k)*res[k])
    sixth=res[k]**6
    central_sixth=sixth*K(fmpq(17**k,102**6))
    check(f'exact original central constant sixth power k={k}',central_sixth==constants[k]**6)
    check(f'original resolvent nonvanishing status k={k}',(res[k]==0)==(k==1))
    out['Kronecker']['resolvents'][str(k)]={'column':res[k].out(),'sixth_power':sixth.out(),
         'central_constant_sixth_power':constants[k]**6,'positive_central_constant':constants[k]}

# Exact generic Newton identities used for the entire inert transposition.
u,dv,h=s.symbols('u d h',integer=True)
# A basis term V=e^(kappa*z^d)*z^(d*h) contributes kappa^-h*(u)_h.
for j in range(8):
    fall=s.prod(u-a for a in range(j))
    nextfall=s.prod(u-a for a in range(j+1))
    check(f'complete Euler/Gaussian Newton identity h={j}',s.expand(dv*j*fall+dv*nextfall-dv*u*fall)==0)
check('negative-weight shift in derivative retains its mass',s.diff(dv*u*s.Function('J')(u-1),u).subs(u,0)==dv*s.Function('J')(-1))
out['ordinary_connection']='nu_H1-a*nu_Hj=Omega_p^-1*x*nu_C - nu_(Fprime/F)*nu_C; additive convolution'
out['inert_connection']='J_H1-a*J_Hj=(d*u+1)*J_V-d*u*J_V(u-1)-J_WhatV; V=C/z'
out['checks']=checks;out['check_count']=len(checks)
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'status':'PASS','check_count':len(checks),
 'actual_central_constants':{'4913':3,'1419857':6},
 'source_cokernels_b1':{k:v['class_b1'] for k,v in conn.items()}},indent=2),flush=True)

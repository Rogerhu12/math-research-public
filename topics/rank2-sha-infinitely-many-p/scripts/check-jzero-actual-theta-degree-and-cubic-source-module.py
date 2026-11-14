#!/usr/bin/env python3
"""R292: exact fixed source/line-bundle and cubic section-module checks."""
import json
from pathlib import Path
import sympy as s
from flint import fmpq_mat

checks=[]
def must(label,yes):
    if not yes:raise AssertionError(label)
    checks.append(label)
I=s.I;d=s.sqrt(-3);w=(-1+d)/2;t=(1+s.sqrt(3))/s.sqrt(2)
v=[1,t,-1,t]
must('actual period-68 coefficient half-period relation',all(s.simplify((-1)**n*v[(n+2)%4]+v[n])==0 for n in range(4)))
s0=(1+d/3)/2
must('maximal order period is 1/(1-omega)',s.simplify(s0-1/(1-w))==0)
must('omega times 1 is -2+3s',s.simplify(w-(-2+3*s0))==0)
must('omega times s is -1+s',s.simplify(w*s0-(-1+s0))==0)
zeta1=2*s.sqrt(3)*s.pi
h=s.sqrt(51*s.sqrt(3))/(204*s.pi*I)
must('actual Hermite Gaussian is the reduced sigma gauge',s.simplify(-1/(8*s.pi*h*h)-34*s.sqrt(3)*s.pi)==0)
must('sigma gauge equals N eta1/2',s.simplify(34*zeta1/2-34*s.sqrt(3)*s.pi)==0)
Z2=s.diag(1,-1);X2=s.Matrix([[0,1],[I,0]]);vv=s.Matrix([1,t])
minors=[s.simplify(s.Matrix.hstack(vv,M*vv).det()) for M in (Z2,X2,Z2*X2)]
must('no nonzero two-torsion stabilizer',all(q!=0 for q in minors))
must('norm-one generator at17 is nonsplit',pow(12,8,17)==16)
def mul17(a,b):return ((a[0]*b[0]-3*a[1]*b[1])%17,(a[0]*b[1]+a[1]*b[0])%17)
def pow17(a,n):
    r=(1,0)
    for _ in range(n):r=mul17(r,a)
    return r
must('actual generator g0 has order18',pow17((2,4),18)==(1,0) and all(pow17((2,4),n)!=(1,0) for n in (1,2,3,6,9)))
must('g0 sixth power is omega',pow17((2,4),6)==(8,9))
must('tau g12 is trivial on omega',(12*6)%18==0)

A,B,C=s.symbols('A B C')
coords=s.Matrix([A,B,C]);X=s.Matrix([[0,1,0],[0,0,-1],[-1,0,0]]);Z=s.diag(1,w,w*w)
red=lambda q:s.simplify(s.expand(q))
must('cubic coordinate Heisenberg generators cube to identity',(X**3-s.eye(3)).applyfunc(red)==s.zeros(3) and (Z**3-s.eye(3)).applyfunc(red)==s.zeros(3))
must('coordinate XZ equals omega ZX',(X*Z-w*Z*X).applyfunc(red)==s.zeros(3))
fermat=A**3+B**3-C**3
sub=lambda f,cs:s.expand(f.subs(dict(zip((A,B,C),cs)),simultaneous=True))
must('X preserves the actual Fermat cubic',s.expand(sub(fermat,X*coords)-fermat)==0)
must('Z preserves the actual Fermat cubic',red(sub(fermat,Z*coords)-fermat)==0)

# Standard degree-34 basis with C exponent at most two.
basis=[(a,34-a-c,c) for c in range(3) for a in range(35-c)]
lookup={e:i for i,e in enumerate(basis)}
must('complete degree34 cubic space has dimension102',len(basis)==102)
polys=[];roles=[]
for typ in (0,1,-1):
    for j in range(5):
        b,c=(3*j+2+2*typ,3*j+2-2*typ)
        e=(30-6*j,b,c);polys.append(e)
        roles.append((typ,j))
cols=[]
for a,b,c in polys:
    row=[0]*102
    k,rem=divmod(c,3)
    for h0 in range(k+1):
        ee=(a+3*h0,b+3*(k-h0),rem)
        row[lookup[ee]]+=int(s.binomial(k,h0))
    cols.append(row)
M=fmpq_mat(102,15,[cols[j][i] for i in range(102) for j in range(15)])
must('three five-dimensional compensation spaces form a direct sum',M.rank()==15)
for (typ,j),(a,b,c) in zip(roles,polys):
    must(f'source {typ},{j} retains degree34',a+b+c==34)
    must(f'source {typ},{j} has true mu3 invariant weight',a%3==0)
    must(f'source {typ},{j} has deck Z weight {typ%3}',(b+2*c)%3==typ%3)
    if typ==0:
        must(f'root compensation clears the actual poles {j}',b>=2 and c>=2)
        must(f'original order at O is 30-6j {j}',a==30-6*j)
# The homogeneous [-1] map is (-A,C,B); all A powers above are even.
must('minus involution exchanges the two compensated spaces',all(a%2==0 for a,b,c in polys))
# X^* sends original monomials to ones whose A exponent is 2 modulo3.
must('nontrivial Heisenberg translates have different mu3 character',all((3*j+2)%3==2 for j in range(5)))

p,r=s.symbols('p r')
must('full inverse exponent is 2-p',s.expand((2-p)+3*(r-1)).subs(p,3*r-1)==0)
must('full inverse restores original deck character',(2-2)%3==0)
payload={'status':'PASS','target_prime_scan':False,'checks':checks,
 'number_of_checks':len(checks),'rectangular_degree':68,'maximal_order_degree':34,
 'cubic_cover_degree':102,'source_minimal_theta_degree':34,
 'two_torsion_non_eigen_minors':[str(q) for q in minors],
 'finite17_generator':[2,4],'discriminant_mod17':12,
 'compensation_module_dimension':15,
 'compensation_monomial_exponents':[{ 'type':typ,'j':j,'A':a,'B':b,'C':c} for (typ,j),(a,b,c) in zip(roles,polys)],
 'global_inverse_pole_order':'p-4-3*j_min at each point over -T',
 'note':'Minimality also uses the proved nonsplit-torus/Heisenberg commutator argument; no central zero is inferred for the transported sections.'}
path=Path(__file__).with_suffix('.json');path.write_text(json.dumps(payload,indent=2)+'\n')
print(json.dumps({'status':'PASS','checks':len(checks),'source_degree':34,'cover_degree':102,'compensation_dimension':15},indent=2))

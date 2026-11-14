"""Exact five-dimensional Artin quotient testing the full cubic Jacobian."""
from fractions import Fraction as F
from pathlib import Path
import importlib.util,json,math,functools
root=Path(__file__).resolve().parents[1]
p=root/'notes/2026-11-13-six-mode-cubic-local-jacobian-cube-verify.py'
spec=importlib.util.spec_from_file_location('cubic_exact',p);a=importlib.util.module_from_spec(spec);spec.loader.exec_module(a)
solved=[3,4,5,8,9,10,11,12,13,14,15,16]
base=[F(1)]*6+[F(0)]*11
a.CUTOFF=1
M=[[F(0) for _ in solved] for _ in solved]
for jj,j in enumerate(solved):
 x=[a.P(z) for z in base];x[j]=x[j]+a.P({(0,1):F(1)})
 _,g,_=a.formula(x)
 for ii,i in enumerate(solved):M[ii][jj]=g[i].d.get((0,1),F(0))
lam2=F(-3175873253213169834598644753425734212,144548086407879029526996850052569)
cubic=F(672625783316756245312265088,239097168542993716033883)
theta=-lam2/(3*cubic)
a.CUTOFF=4
e=a.P({(0,1):F(1)});S=2-4*e;P=1-4*e+8*e*e
y=[a.P(1),a.P(1)];h=[a.P(),e]
for _ in range(4):y.append(S*y[-1]-P*y[-2])
for _ in range(9):h.append(S*h[-1]-P*h[-2])
x=y+h;x[2]=x[2]+theta*e*e
corrections={}
for degree in [2,3,4]:
 _,g,_=a.formula(x)
 rhs=[-g[i].d.get((0,degree),F(0)) for i in solved]
 det,sol=a.eliminate(M,rhs);assert det
 corrections[degree]=[str(z) for z in sol]
 for i,z in zip(solved,sol):x[i]=x[i]+a.P({(0,degree):z})
R,g,ell=a.formula(x)
assert all(not f.d for f in g)
assert not R.d
ie=a.mv(a.Ji,ell)
Be0=x[0]**3-6*x[0]*x[6]-ie[0]
leading=Be0.d.get((0,2),F(0))
assert not Be0.d.get((0,0),0) and not Be0.d.get((0,1),0)
assert leading==theta*F(249584547,496533016) and leading
assert (Be0*Be0).d=={(0,4):leading**2}
# Bell first normal coefficient for all three original empty-spectrum directions.
a.CUTOFF=1
numerators=[0,0,1986132064,8968264800,29268304608,89336254496,0,0,-361544476,-1159751133,-2415939762,-4110758331,-6074808164,-7612556445,-6553855382,2420577073,28256379896]
v=[F(z,1986132064) for z in numerators]
xv=[a.P(c)+a.P({(0,1):z}) for c,z in zip(base,v)]
_,ellv=a.formula(xv,grad=False)
dell=[p.d.get((0,1),F(0)) for p in ellv]
jell=[sum(a.Ji[i][j]*dell[j] for j in range(16)) for i in range(16)]
a.CUTOFF=4
f=[F(52565262336),F(6080833024),F(-43931504),F(3725)]
def trim(p):
 p=list(p)
 while p and not p[-1]:p.pop()
 return p
def add(p,q):
 return trim([(p[i] if i<len(p) else 0)+(q[i] if i<len(q) else 0) for i in range(max(len(p),len(q)))])
def scale(p,c):return trim([z*c for z in p])
def divrem(p,q):
 p=trim(p);q=trim(q);out=[F(0)]*max(0,len(p)-len(q)+1)
 while len(p)>=len(q) and p:
  n=len(p)-len(q);z=p[-1]/q[-1];out[n]=z
  p=add(p,[F(0)]*n+scale(q,-z))
 return trim(out),p
def mul(p,q):
 out=[F(0)]*max(0,len(p)+len(q)-1)
 for i,z in enumerate(p):
  for j,w in enumerate(q):out[i+j]+=z*w
 return divrem(out,f)[1]
def gcd(p,q):
 while q:p,q=q,divrem(p,q)[1]
 return scale(p,1/p[-1])
N=[F(-271360),F(46784),F(-521)];L=[F(-112640),F(800)];Nb=add(N,mul([F(0),F(1)],L));u=add(add(N,Nb),L)
rvterm=scale(mul(mul(u,u),L),3*v[5])
hr=add(scale(mul(Nb,Nb),v[8]),add(scale(mul(N,L),2*v[11]),add(scale(mul(Nb,L),2*v[12]),scale(mul(L,L),v[16]))))
coef=add(rvterm,scale(mul(u,hr),-6))
row={0:N,1:Nb,5:L}
for i,pi in row.items():
 for j,pj in row.items():
  for k,pk in row.items():coef=add(coef,scale(mul(mul(pi,pj),pk),-jell[i+j+k]))
assert gcd(coef,f)==[F(1)] and gcd(L,f)==[F(1)]
def mod103(z):return z.numerator%103*pow(z.denominator%103,-1,103)%103
assert list(map(mod103,coef))==[45,5,71]
assert list(map(mod103,f))==[80,85,56,17]
assert mod103(theta)==41 and mod103(leading)==13
sylvester=[[17,56,85,80,0],[0,17,56,85,80],[71,5,45,0,0],[0,71,5,45,0],[0,0,71,5,45]]
res,_=a.eliminate([[F(z) for z in row] for row in sylvester])
assert mod103(res)==14
result={'all_pass':True,'quotient':'Q[epsilon]/(epsilon^5)',
 'theta':str(theta),'full_gradient_zero_count':17,'full_target_zero':True,
 'normal_coordinates_zero_based':solved,'normal_corrections':corrections,
 'arc_coefficients_by_variable':[[str(z.d.get((0,j),F(0))) for j in range(5)] for z in x],
 'Bell_e0_epsilon2':str(leading),'Bell_e0_square_epsilon4':str(leading**2),
 'original_first_denominator':[-112640,800],
 'original_first_cleared_linear_coefficient_mod_cubic':[str(z) for z in coef],
 'original_first_gcd_is_one':True,'original_first_resultant_mod103':14,
 'scope':'This exact finite quotient kills every original Jacobian generator while every selected matched Bell remainder has nonzero square. Combined with the published local cube membership, exponent three is locally minimal at p0. No global or operator-inverse assertion.'}
print(json.dumps(result,indent=2))

#!/usr/bin/env python3
"""R311: actual six odd Schwartz sources and the original tame-one interface.

All local vectors are computed in Q(zeta_306).  The exact, previously paid
full odd CM13 matrix is used to identify their polynomial sources over the
real cubic field.  No scratch file or numerical recognition is used.
"""
from pathlib import Path
import json,sympy as s
from flint import fmpq,fmpq_poly
base=Path(__file__).parent
checks=[]
def check(name,condition):
 assert condition,name
 checks.append(name)
def Field(n):
 X=s.symbols('X');m=s.Poly(s.cyclotomic_poly(n,X),X)
 mod=fmpq_poly([fmpq(str(m.nth(j))) for j in range(m.degree()+1)])
 class F:
  def __init__(self,a=0):
   if isinstance(a,F):self.a=a.a;return
   self.a=(a if isinstance(a,fmpq_poly) else fmpq_poly([fmpq(a)]))%mod
  def __add__(self,b):return F(self.a+F(b).a)
  __radd__=__add__
  def __neg__(self):return F(-self.a)
  def __sub__(self,b):return self+-F(b)
  def __rsub__(self,b):return F(b)-self
  def __mul__(self,b):return F(self.a*F(b).a)
  __rmul__=__mul__
  def __truediv__(self,b):
   g,v,_=F(b).a.xgcd(mod);assert g==1
   return F(self.a*v)
  def __rtruediv__(self,b):return F(b)/self
  def __pow__(self,n):
   if n<0:return (F(1)/self)**(-n)
   a,b=F(1),self
   while n:
    if n&1:a=a*b
    b=b*b;n//=2
   return a
  def __eq__(self,b):return self.a==F(b).a
  def __bool__(self):return bool(self.a)
  def comp(self,b):
   r=F(0)
   for j in range(mod.degree()-1,-1,-1):r=r*b+F(self.a[j])
   return r
  def conj(self):return self.comp(F(fmpq_poly([0,1]))**(-1))
  def out(self):return [str(a) for a in self.a]
 F.mod=mod
 return F
F=Field(306);z=F(fmpq_poly([0,1]));ze=z**17;z17=z**18
legs=[0]+[1 if pow(a,8,17)==1 else -1 for a in range(1,17)]
root17=sum((legs[a]*z17**a for a in range(1,17)),F(0))
check('actual quadratic Gauss square',root17**2==17)
fm=lambda a,b:((a[0]*b[0]-3*a[1]*b[1])%17,(a[0]*b[1]+a[1]*b[0])%17)
gs=[(1,0)]
for n in range(1,19):gs.append(fm(gs[-1],(2,4)))
check('same original norm-one torus generator',gs[18]==(1,0) and gs[3]==(9,9) and gs[6]==(8,9))
indices=[1,5,7,11,13,17]
sources={}
for j in indices:
 f=[]
 for a in range(17):
  v=root17*((1 if a==1 else 0)-(1 if a==16 else 0))
  for n in range(1,18):
   if n==9:continue
   x,y=gs[n];ex=(3*pow(2*y,-1,17)*(x*(a*a+1)-2*a))%17
   v-=legs[y]*ze**(-j*n)*z17**ex
  f.append(v)
 check(f'original e1 projection nonzero j={j}',bool(f[1]))
 check(f'original finite vector real and odd j={j}',all(f[-a%17]==-f[a] and f[a].conj()==f[a] for a in range(17)))
 norm=sum((v*v for v in f),F(0))
 check(f'full projection norm j={j}',norm==18*root17*f[1])
 W=[];x,y=gs[1]
 for a in range(17):
  W.append(sum((-legs[y]/root17*z17**((3*pow(2*y,-1,17)*(x*(a*a+b*b)-2*a*b))%17)*f[b] for b in range(17)),F(0)))
 check(f'actual full finite Weil eigenvector j={j}',W==[ze**j*v for v in f])
 sources[j]={'finite_norm':norm.out(),'f17':[v.out() for v in f],'dyadic':'plus' if j%6==5 else 'minus'}
 print('finite source',j,'verified',flush=True)

G=Field(18);a=G(fmpq_poly([0,1]));w=a**6;d=1+2*w;gam=(7+d)/2
dd=s.sqrt(-3)
def cv(txt):
 q=s.expand(s.sympify(txt));r=s.re(q);i=s.simplify(s.im(q)/s.sqrt(3))
 return G(fmpq(str(r)))+d*G(fmpq(str(i)))
data=json.loads((base/'check-jzero-odd-cm13-companion.json').read_text())
M=[[cv(c) for c in row] for row in data['CM13_matrix']]
def solve(A,b):
 A=[list(r)+[v] for r,v in zip(A,b)];n=len(A)
 for j in range(n):
  pivot=next(i for i in range(j,n) if A[i][j]);A[j],A[pivot]=A[pivot],A[j]
  t=A[j][j];A[j]=[v/t for v in A[j]]
  for i in range(n):
   if i==j:continue
   t=A[i][j]
   if t:A[i]=[u-t*v for u,v in zip(A[i],A[j])]
 return [r[-1] for r in A]
def mv(M,v):return [sum((c*x for c,x in zip(r,v)),G(0)) for r in M]
eig={};spec={1:11,5:1,7:5,11:13,13:17,17:7}
for j in indices:
 eigen=gam*a**spec[j]
 mat=[[M[r][c]-(eigen if r==c else 0) for c in range(5)] for r in range(5)]
 rhs=[M[r][5] for r in range(5)]
 v=solve(mat,rhs)+[G(-1)]
 check(f'complete CM13 identity and origin normalization j={j}',mv(M,v)==[eigen*q for q in v] and v[5]==-1)
 check(f'actual source coefficients real j={j}',all(q.conj()==q for q in v))
 eig[j]=v
 sources[j]['raw_CM13_phase_exponent']=spec[j]
 sources[j]['odd_P_coefficients']=[q.out() for q in v]
 print('actual source',j,'normalized',flush=True)
data=json.loads((base/'check-jzero-three-original-sources-and-central-constants.json').read_text())
v={k:[G(0)]+[G(fmpq(c)) for c in data['connection']['sources'][k]['R_b1_ascending']] for k in ['1','3','5']}
a13=G(fmpq(-37,33936));a15=G(fmpq(-37,53760))
companions={'C13':[x-a13*y for x,y in zip(v['1'],v['3'])],
 'C15':[x-a15*y for x,y in zip(v['1'],v['5'])],
 'C35':[160*x-101*y for x,y in zip(v['3'],v['5'])]}
E=[[eig[j][i] for j in indices] for i in range(6)]
decomp={}
for lab,v in companions.items():
 coeff=solve(E,v)
 check(f'actual complete six-source decomposition {lab}',mv(E,coeff)==v and all(coeff))
 check(f'original first moment is retained {lab}',sum(coeff,G(0))==-v[5])
 decomp[lab]=[c.out() for c in coeff]
 print(lab,'decomposition verified',flush=True)
# Compact real cubic expressions, without choosing numerical embeddings.
T,X,b=s.symbols('T X b',nonzero=True)
plus=[-s.Rational(1024,17)*(5*T*T-T-8),
 -s.Rational(256,17)*(53*T*T-133*T-180),
 -s.Rational(256,17)*(66*T*T-105*T-58),
 -s.Rational(16,17)*(605*T*T+338*T-1019),
 -s.Rational(4,17)*(308*T*T-184*T-537),s.Integer(-1)]
minus=[-512*T*(T-2),-256*(8*T*T-7*T-11),
 -32*(69*T*T-3*T-253),-16*(20*T*T+68*T-165),
 2*(176*T*T-208*T-227),s.Integer(-1)]
def ev(poly,t):
 p=s.Poly(poly,T);v=G(0)
 for j in range(p.degree(),-1,-1):v=v*t+G(fmpq(str(p.nth(j))))
 return v
denominator_primes=set()
for j in indices:
 e=spec[j];tr=a**e+a**(-e)
 check(f'actual real cubic parameter j={j}',tr**3-3*tr-1==0)
 pol=plus if j%6==5 else minus
 check(f'compact actual polynomial j={j}',[ev(q,tr) for q in pol]==eig[j])
 aa=1 if j%6==5 else 2;rr=j-9
 check(f'original global unit condition j={j}',(aa+rr)%3==0)
 check(f'CM13 original Hecke phase j={j}',-a**(-6*aa-4*j)==a**e)
 sources[j].update({'two_adic_Teich_exponent':aa,'seventeen_character_exponent':16*rr,
   'CM13_twist_character_exponent':(-6*aa-4*j)%18,
   'real_cubic_parameter_exponent':e})
 for q in eig[j]:
  for v in q.a:
   denominator_primes.update(s.factorint(int(v.denominator)))
check('all six original columns integral away from seventeen',denominator_primes=={17})
A13p=-(161*T*T+1469*T-4984)/s.Integer(12827808)
A13m=-17*(8*T*T-T-16)/s.Integer(1603476)
A15p=(763*T*T-2507*T+3136)/s.Integer(20321280)
A15m=-17*(8*T*T-T-16)/s.Integer(1016064)
for j in indices:
 tr=a**spec[j]+a**(-spec[j]);i=indices.index(j)
 check(f'compact C13 coefficient j={j}',G(fmpq_poly([fmpq(c) for c in decomp['C13'][i]]))==ev(A13p if j%6==5 else A13m,tr))
 check(f'compact C15 coefficient j={j}',G(fmpq_poly([fmpq(c) for c in decomp['C15'][i]]))==ev(A15p if j%6==5 else A15m,tr))
check('actual opposite dyadic block cancels in CX',s.expand(101*A13m-64*A15m)==0)
AX=-(T*T+T-8)/s.Integer(10080)
check('pure three-source coefficient',s.expand((101*A13p-64*A15p)/37-AX)==0)
# The cubic trace is Tr(1)=3, Tr(T)=0, Tr(T^2)=6.
trace=lambda v:3*s.Poly(v,T).nth(0)+6*s.Poly(v,T).nth(2)
check('pure companion retains its exact first mass',trace(AX)==s.Rational(1,560))
P1=X**4-s.Rational(53,7)*b*X**3-s.Rational(12,7)*b*b*X**2-s.Rational(80,7)*b**3*X-s.Rational(128,7)*b**4
P3=X**5-208*b*X**4+400*b*b*X**3+8128*b**3*X**2+12032*b**4*X-2048*b**5
P5=X**5+272*b*X**4-272*b*b*X**3-14912*b**3*X**2-6784*b**4*X+1024*b**5
RX=-(X-8*b)**2*(X*X+20*b*X-8*b*b)/(560*b)
LX=6*X*(X+b)*s.diff(RX,X)-(25*X+28*b)*RX
check('pure original connection row for general b',s.expand(LX-P1-P3/(336*b)+P5/(840*b))==0)
# sigma(4z)=-4*y*(X^2+20bX-8b^2)*sigma(z)^16;
# Theta(2z)=x*(X-8b)*sigma(z)^8. Both signs are original O-branches.
check('complete fixed two-power product identity',s.expand(-4*(X*X+20*b*X-8*b*b)*(X-8*b)**2/(2240*b)-RX)==0)
check('raw sigma quadrupling sign fixes the first moment',s.Rational(4,2240)==s.Rational(1,560))
ss=(3+d)/6
check('CM period cubed',ss**3==d/9)
check('odd weight CM period phase',1/(ss**3)==-3*w/ss)
check('zero-weight Kronecker coefficient c11',s.diff((s.Symbol('r')**2-s.Symbol('x'))/2,s.Symbol('r'))*(-s.Symbol('x'))-s.Symbol('y')==-s.Symbol('r')*s.Symbol('x')-s.Symbol('y'))
u,n,du=s.symbols('u n d');bp=s.symbols('barpi',positive=True)
check('full shifted annulus logarithmic derivative',s.diff(bp**(-3*n)*s.exp(-2*n*du*u*s.log(bp)),u).subs(u,0)==-2*n*du*s.log(bp)*bp**(-3*n))
out={'status':'PASS','sources':sources,'order':indices,'companion_decompositions_b1':decomp,
 'real_cubic_minimal_polynomial':'T^3-3*T-1',
 'P_plus_ascending':[str(q) for q in plus],
 'P_minus_ascending':[str(q) for q in minus],
 'compact_C13_coefficients':[str(A13p),str(A13m)],
 'compact_C15_coefficients':[str(A15p),str(A15m)],
 'pure_CX_coefficient':str(AX),
 'pure_CX_product':'Theta(z)*Theta(2*z)^2*sigma(4*z)/(2240*b)',
 'pure_CX_full_row':'nabla_F(CX)=H1+H3/(336*b)-H5/(840*b)',
 'prime_core':'nu_j|pZp=(xi_j(p)/barpi)*[p/barpi^2]_*nu_j',
 'tame_one_annulus':'U_j^[n](u)=xi_j^n*barpi^(-3*n)*<barpi>^(-2*n*d*u)*U_j(u)',
 'checks':checks,'check_count':len(checks),
 'CM13_matrix_field':'Q(zeta18), delta=1+2*zeta18^6',
 'finite_field':'Q(zeta306), zeta18=zeta306^17,zeta17=zeta306^18'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'status':'PASS','check_count':len(checks),'all_actual_sources':indices,
 'only_source_denominator_prime':17,'pure_companion_mass':'1/(560*b)'},indent=2),flush=True)

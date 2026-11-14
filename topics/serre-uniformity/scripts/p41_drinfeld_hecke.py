"""Actual prime-to-41 isogeny phases on Drinfeld inertia blocks; geometry in R135."""
from pathlib import Path
from functools import lru_cache
import json, hashlib
from sympy import cyclotomic_poly, Poly, Symbol

p=41;ns=34;zero=(0,0);one=(1,0)
def add(x,y):return ((x[0]+y[0])%p,(x[1]+y[1])%p)
def neg(x):return ((-x[0])%p,(-x[1])%p)
def sub(x,y):return add(x,neg(y))
def mul(x,y):return ((x[0]*y[0]+ns*x[1]*y[1])%p,(x[0]*y[1]+x[1]*y[0])%p)
def sc(a,x):return (a*x[0]%p,a*x[1]%p)
def pw(x,n):
 z=one
 while n:
  if n&1:z=mul(z,x)
  x=mul(x,x);n//=2
 return z
def inv(x):return pw(x,1679)
def div(x,y):assert y!=zero;return mul(x,inv(y))
def jinv(A,B):return div(sc(1728*4,pw(A,3)),add(sc(4,pw(A,3)),sc(27,pw(B,2))))
field=[(a,b) for a in range(p) for b in range(p)]
labels=[0,3,28,32];weights=[3,1,1,1]
curves={}
for j in labels:
 if j==0:A,B=zero,one
 elif j==28:A,B=(6,0),(16,0)
 else:k=j*pow((1728-j)%41,-1,41)%41;A,B=(3*k%41,0),(2*k%41,0)
 curves[j]=(A,B)
isos={}
for j,(A,B) in curves.items():
 dd={}
 for c in field[1:]:dd.setdefault((mul(pw(c,4),A),mul(pw(c,6),B)),[]).append(c)
 isos[j]=dd
branches=[];Hs={}
for ell in [2,3]:
 H=[[0]*4 for _ in labels]
 for j,(A,B) in curves.items():
  if ell==2:
   roots=[x for x in field if add(add(pw(x,3),mul(A,x)),B)==zero]
  else:
   roots=[x for x in field if sub(add(add(sc(3,pw(x,4)),sc(6,mul(A,pw(x,2)))),sc(12,mul(B,x))),pw(A,2))==zero]
  assert len(roots)==ell+1
  for x in roots:
   if ell==2:
    AQ=add(sc(-4,A),sc(-15,pw(x,2)))
    BQ=add(sc(-22,pw(x,3)),sc(-8,mul(A,x)))
   else:
    AQ=add(sc(-9,A),sc(-30,pw(x,2)))
    BQ=add(add(sc(-27,B),sc(-42,mul(A,x))),sc(-70,pw(x,3)))
   ji=jinv(AQ,BQ);assert ji[1]==0 and ji[0] in labels;i=ji[0]
   cs=isos[i][AQ,BQ];assert len(cs)==2*weights[labels.index(i)]
   c=cs[0];t=sc(pow(ell,-1,41),pw(c,2));gamma=sc(pow(ell,-1,41),pw(c,42))
   H[labels.index(i)][labels.index(j)]+=1
   branches.append({'ell':ell,'source_j':j,'target_j':i,'kernel_x':x,'quotient_A':AQ,'quotient_B':BQ,'c':c,'t':t,'gamma':gamma})
 Hs[ell]=H
gauge={0:one}
while len(gauge)<4:
 for b in branches:
  if b['ell']==2 and b['source_j'] in gauge and b['target_j'] not in gauge:
   gauge[b['target_j']]=div(gauge[b['source_j']],b['t'])
zeta=next(x for x in field[1:] if pw(x,42)==one and pw(x,21)!=one and pw(x,14)!=one and pw(x,6)!=one)
logs={pw(zeta,k):k for k in range(42)};assert len(logs)==42
for b in branches:
 phase=div(mul(gauge[b['target_j']],b['t']),gauge[b['source_j']])
 assert pw(phase,42)==one,('phase norm',b,phase,gauge)
 assert pw(phase,21)==(pow(b['ell'],20,41),0),('phase parity',b,phase,gauge)
 b['phase_exponent']=logs[phase]
 assert mul(div(pw(gauge[b['target_j']],21),pw(gauge[b['source_j']],21)),b['gamma'])==one

class Ring:
 def __init__(self,d):
  self.d=d;x=Symbol('x');self.f=tuple(int(c) for c in reversed(Poly(cyclotomic_poly(d,x),x).all_coeffs()));self.n=len(self.f)-1
  self.zero=(0,)*self.n;self.one=(1,)+(0,)*(self.n-1);self.x=(0,1)+(0,)*(self.n-2)
  self.pows=[self.one]
  for _ in range(d):self.pows.append(self.mul(self.pows[-1],self.x))
  assert self.pows[-1]==self.one
 def add(self,a,b):return tuple(x+y for x,y in zip(a,b))
 def neg(self,a):return tuple(-x for x in a)
 def scale(self,a,n):return tuple(n*x for x in a)
 @lru_cache(maxsize=50000)
 def mul(self,a,b):
  c=[0]*(2*self.n-1)
  for i,x in enumerate(a):
   for j,y in enumerate(b):c[i+j]+=x*y
  for k in range(len(c)-1,self.n-1,-1):
   x=c[k]
   if x:
    for j,f in enumerate(self.f):c[k-self.n+j]-=x*f
  return tuple(c[:self.n])
 def ident(self,n):return [[self.one if i==j else self.zero for j in range(n)] for i in range(n)]
 def mm(self,A,B):
  C=[[self.zero for j in B[0]] for i in A]
  for i in range(len(A)):
   for k in range(len(B)):
    if A[i][k]!=self.zero:
     for j in range(len(B[0])):
      if B[k][j]!=self.zero:C[i][j]=self.add(C[i][j],self.mul(A[i][k],B[k][j]))
  return C
 def ma(self,A,B):return [[self.add(x,y) for x,y in zip(a,b)] for a,b in zip(A,B)]
 def ms(self,A,n):return [[self.scale(x,n) for x in a] for a in A]
 def evalmat(self,coeff,M):
  n=len(M);I=self.ident(n);A=[[self.zero]*n for _ in range(n)]
  for c in coeff:A=self.ma(self.mm(A,M),self.ms(I,c))
  return A
 def charpoly(self,M):
  n=len(M);P=self.ident(n);tr=[]
  for _ in range(n):P=self.mm(P,M);tr.append(tuple(sum(P[i][i][k] for i in range(n)) for k in range(self.n)))
  coeff=[self.one]
  for k in range(1,n+1):
   val=self.zero
   for i in range(1,k+1):val=self.add(val,self.mul(coeff[k-i],tr[i-1]))
   assert all(x%k==0 for x in val)
   coeff.append(tuple(-x//k for x in val))
  assert all(x==self.zero for row in self.evalmat_ring(coeff,M) for x in row)
  return coeff
 def evalmat_ring(self,coeff,M):
  n=len(M);A=[[self.zero]*n for _ in range(n)]
  for c in coeff:
   A=self.mm(A,M)
   for i in range(n):A[i][i]=self.add(A[i][i],c)
  return A

root=Path(__file__).resolve().parent/'data'
jac=json.loads((root/'p41_jacobi_cm_certificate.json').read_text());factors=[f['factor_descending'] for f in jac['fields']]
out={'branches':branches,'curves':curves,'gauge':gauge,'zeta42':zeta,'T2_Brandt':Hs[2],'T3_Brandt':Hs[3],'blocks':[]}
for d in [6,14,42]:
 R=Ring(d);active=labels if d==14 else labels[1:];n=len(active);Ms={}
 for ell in [2,3]:
  M=[[R.zero]*n for _ in range(n)]
  for b in branches:
   if b['ell']==ell and b['source_j'] in active and b['target_j'] in active:
    i=active.index(b['target_j']);j=active.index(b['source_j']);M[i][j]=R.add(M[i][j],R.pows[b['phase_exponent']%d])
  Ms[ell]=M
 assert R.mm(Ms[2],Ms[3])==R.mm(Ms[3],Ms[2]),('noncommuting',d)
 H=R.ma(Ms[2],R.ms(Ms[3],2));matches=[]
 for fi,f in enumerate(factors):
  V=R.evalmat(f,H)
  if all(x==R.zero for row in V for x in row):matches.append(fi)
 cp=R.charpoly(H)
 traces={ell:tuple(sum(Ms[ell][i][i][k] for i in range(n)) for k in range(R.n)) for ell in [2,3]}
 print('inertia',d,'matches',matches,'traces',traces,'charpoly',cp,flush=True)
 out['blocks'].append({'inertia_order':d,'cyclotomic_polynomial_ascending':R.f,'labels':active,'T2':Ms[2],'T3':Ms[3],'H':H,'H_characteristic_polynomial':cp,'R89_matching_factors':matches})
out['source_sha256']={'p41_jacobi_cm_certificate.json':hashlib.sha256((root/'p41_jacobi_cm_certificate.json').read_bytes()).hexdigest()}
out['status']='Actual geometric action proved in R135; all finite-field data and cyclotomic identities exact.'
(root/'p41_drinfeld_hecke_certificate.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print('T3 Brandt',Hs[3]);print('All finite phases, inertia blocks and commutation PASS.')

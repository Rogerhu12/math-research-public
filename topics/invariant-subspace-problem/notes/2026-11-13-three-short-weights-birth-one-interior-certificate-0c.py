"""Exact integer certificate for q=3, relative birth one, all interior heights and the true third edge. Requires Python 3, SymPy and python-flint. Run this file directly."""
import sys,itertools
from math import comb,prod
import sympy as sp
from flint import fmpz_mpoly_ctx
from time import monotonic

delta=2
assert delta in (1,2)
ctx=fmpz_mpoly_ctx.get(('x','y','z'),ordering='lex')
x,y,z=ctx.gens();one=ctx.from_dict({(0,0,0):1});zero=one*0
def rising(a,n):
 out=one
 for k in range(n):out*=a+k
 return out
def Z(weights,k):
 if k==0:return one
 out=zero
 for inds in itertools.combinations(range(4),k):
  factor=prod((i-j)**2 for i,j in itertools.combinations(inds,2));v=one*factor
  for j in inds:v*=weights[j]
  out+=v
 return out
C=[];B=[];A=[];M=[]
for i in range(4):
 ww=[comb(3,r)*z**r*rising(x+1,i+r)*rising(y+1,6-i-r) for r in range(4)]
 C.append(Z(ww,delta));B.append(Z(ww,delta+1));A.append(Z(ww,delta+2));M.append(z*B[-1].derivative('z'))
XP=M[0]*B[1]*B[2]-2*M[1]*B[0]*B[2]+M[2]*B[0]*B[1]
YP=-M[1]*B[2]*B[3]+2*M[2]*B[1]*B[3]-M[3]*B[1]*B[2]
p,q,r,t,aa,bb,cc,dd,xx,yy=sp.symbols('p q r t A B C D X Y')
V0=q*t-r*r;V1=p*t-q*r;V2=p*r-q*q
N1=(q*q*r*t*aa*cc-p*r*r*t*bb*bb)*V1+(p*q*q*r*aa*dd-p*p*q*t*bb*cc)*V0-q*t*cc*xx*xx-p*r*aa*yy*yy-2*p*t*bb*xx*yy
N2=aa*(cc*p*q*q*r**3*t*t-cc*q**4*r*r*t*t+dd*p*q**3*r**3*t-dd*q**4*r**4-yy*yy*q*q*r*r)+bb*bb*(-p*p*r**4*t*t+p*q*q*r**3*t*t)+bb*(-cc*p*p*q*q*r*r*t*t+cc*p*q**3*r**3*t+dd*p*p*q**3*r*r*t-dd*p*p*q*q*r**4-2*xx*yy*p*r*r*t-yy*yy*p*p*r*r)+cc*cc*(-p*p*q**4*t*t+p*p*q**3*r*r*t)+cc*(-xx*xx*q*q*t*t-2*xx*yy*p*q*q*t)-dd*xx*xx*q*q*r*r-xx*xx*yy*yy
N3=(q*r*r*t*aa*dd-p*r*t*t*bb*cc)*V2+(p*q*r*r*bb*dd-p*q*q*t*cc*cc)*V1-q*t*dd*xx*xx-p*r*bb*yy*yy-2*p*t*cc*xx*yy
vars=(p,q,r,t,aa,bb,cc,dd,xx,yy)
nums=B+A+[XP,YP]
unit=[tuple(int(i==j) for i in range(4)) for j in range(4)]
dens=unit+unit+[(1,1,1,0),(0,1,1,1)]

registry=[]; regkeys={}; basis=[]; contents=[]
start=monotonic()
for k,v in enumerate(nums+C):
 co,ff=v.factor();contents.append(int(co));e={}
 assert one*int(co)*prod((f**power for f,power in ff),start=one)==v
 for f,power in ff:
  key=str(f)
  if key not in regkeys:regkeys[key]=len(registry);registry.append(f)
  idx=regkeys[key];e[idx]=int(power)
 basis.append(e)
 print('FACTORED',k,'terms',len(v.to_dict()),'factors',len(e),'seconds',monotonic()-start,flush=True)
for label,N in [('P2',N2),('P1',N1),('P3',N3)]:
 terms=sp.Poly(N,*vars).terms()
 ds=[tuple(sum(exp[k]*dens[k][i] for k in range(10)) for i in range(4)) for exp,coeff in terms]
 common=tuple(max(v[i] for v in ds) for i in range(4))
 fterms=[]
 for (exp,co),de in zip(terms,ds):
  full=list(exp)+[common[i]-de[i] for i in range(4)]
  ee={};cc=int(co)
  for j,power in enumerate(full):
   cc*=contents[j]**power
   for k,v in basis[j].items():ee[k]=ee.get(k,0)+v*power
  fterms.append((ee,cc))
 gcdpowers={k:min(e.get(k,0) for e,cc in fterms) for k in range(len(registry))}
 gcdpowers={k:e for k,e in gcdpowers.items() if e}
 print('COMMON',label,[(str(registry[k]),v) for k,v in gcdpowers.items()],flush=True)
 for k,e in gcdpowers.items():assert all(co>0 for mon,co in registry[k].terms())
 ef={'P1':([28,23,15,6,1],[28,23,15,7,2],32),'P2':([34,28,18,8,2],[34,28,18,8,2],38),'P3':([28,23,15,7,2],[28,23,15,6,1],32)}[label]
 explicit=z**ef[2]
 for ii in range(5):explicit*=(x+ii+1)**ef[0][ii]*(y+ii+1)**ef[1][ii]
 assert prod((registry[k]**e for k,e in gcdpowers.items()),start=one)==explicit
 out=zero;cache={}
 for ee,cc in fterms:
  factors=[]
  for k,e in ee.items():
   power=e-gcdpowers.get(k,0)
   if power:
    key=(k,power)
    if key not in cache:cache[key]=registry[k]**power
    factors.append(cache[key])
  factors.sort(key=lambda f:len(f.to_dict()));v=one*cc
  for f in factors:v*=f
  out+=v
 tt=list(out.terms());neg=[(m,str(c)) for m,c in tt if c<0]
 print('REDUCED',label,'terms',len(tt),'negative',len(neg),'degree',out.total_degree(),'seconds',monotonic()-start,flush=True)
 assert not neg,(label,neg[:5])
 ex={'P1':(6084,56,6080,455,25,23837781756511459928930726707200),'P2':(8822,66,8819,624,31,199621251780066428746393433250201600),'P3':(6084,56,6080,455,25,4584188799329126909409755136000)}[label]
 assert (len(tt),out.total_degree())==ex[:2]
 if not neg:
  edge=out.compose(x-1,y,z);ee=list(edge.terms());eneg=[(m,str(c)) for m,c in ee if c<0]
  order=min(m[0] for m,c in ee);lead=[(m,c) for m,c in ee if m[0]==order]
  print('SHIFT',label,'terms',len(ee),'negatives',len(eneg),'order',order,'edge',len(lead),'edge negative',sum(c<0 for m,c in lead),'anchor',[(m,str(c)) for m,c in lead if m[1]==0][:1],flush=True)

  assert len(ee)==ex[2] and not eneg and order==0 and len(lead)==ex[3]
  assert dict(lead)[(0,0,ex[4])]==ex[5]
print("ALL_PASS q3 t1 complete interior and third edge",flush=True)

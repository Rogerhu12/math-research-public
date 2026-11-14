import sys,itertools
from math import comb,prod
import sympy as sp
from flint import fmpz_mpoly_ctx
from time import monotonic

delta=1
# q=3, relative birth t=2. All operations below are exact integers.
expected={"P1":(133311,166,91840,18,2159,45,938841866102605191047117851852800000),"P2":(232080,200,159603,22,3129,55,350420848839065182347954643968353894400000),"P3":(133311,166,93180,18,2091,45,375536746441042076418847140741120000)}
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
start=monotonic()
for label,N in [('P1',N1),('P2',N2),('P3',N3)]:
 terms=sp.Poly(N,*vars).terms()
 ds=[tuple(sum(exp[k]*dens[k][i] for k in range(10)) for i in range(4)) for exp,coeff in terms]
 common=tuple(max(v[i] for v in ds) for i in range(4))
 print('START',delta,label,'common denominator powers',common,flush=True)
 out=zero
 powers={}
 def power(polyid,exp):
  key=(polyid,exp)
  if key not in powers:powers[key]=(nums+C)[polyid]**exp
  return powers[key]
 for (exp,coeff),den in zip(terms,ds):
  factors=[power(k,e) for k,e in enumerate(exp) if e]+[power(10+i,common[i]-den[i]) for i in range(4) if common[i]!=den[i]]
  factors.sort(key=lambda v:len(v.to_dict()))
  value=one*int(coeff)
  for f in factors:value*=f
  out+=value
 tt=list(out.terms());neg=[(mon,str(c)) for mon,c in tt if c<0]
 print('RESULT',delta,label,'terms',len(tt),'negative',len(neg),'degree',out.total_degree(),'seconds',monotonic()-start,flush=True)
 assert not neg,(label,neg[:3])
 assert (len(tt),out.total_degree())==expected[label][:2]
 if not neg:
  edge=out.compose(x-1,y,z);ee=list(edge.terms());eneg=[(m,str(c)) for m,c in ee if c<0]
  order=min(m[0] for m,c in ee);lead=[(m,c) for m,c in ee if m[0]==order]
  print('SHIFT',label,'terms',len(ee),'negatives',len(eneg),'order',order,'edge',len(lead),'edge negative',sum(c<0 for m,c in lead),'anchor',[(m,str(c)) for m,c in lead if m[1]==0][:1],flush=True)

  ev=expected[label]
  assert len(ee)==ev[2] and not eneg and order==ev[3] and len(lead)==ev[4]
  assert dict(lead)[(order,0,ev[5])]==ev[6]
print('ALL_PASS q3 t2 interior and forced-root next-to-first endpoint',flush=True)

#!/usr/bin/env python3
"""FIRST new W positive-e, k=-2 residue, ell-pole normalized original center.
p=1009 is the already fixed place. No old projection/ray gcd is rerun.
The original q2, R6, COMPLETE N5 leading forms are reconstructed below.
Only the new finite-mu center beta/e=r!=0,-1 with A2!=0 is considered.
Return one exact two-source univariate Bezout after the displayed q2
substitution. All denominator supports are proved nonzero in this branch.
30 seconds / 256 MiB; standard Python only; no coefficient payload file.
"""
import hashlib,json,resource,signal,time
START=time.perf_counter()
resource.setrlimit(resource.RLIMIT_AS,(256*1024**2,256*1024**2))
signal.setitimer(signal.ITIMER_REAL,30)
P=1009
counts={'divisions':0,'bezoutReturns':0,'originalRationalReturns':0}
def say(stage,**kw):
 kw.update(stage=stage,seconds=time.perf_counter()-START)
 print(json.dumps(kw,separators=(',',':')),flush=True)
def tr(a):
 a=[int(x)%P for x in a]
 while a and not a[-1]:a.pop()
 return a
def add(a,b):
 return tr([(a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0)
            for i in range(max(len(a),len(b)))])
def neg(a):return tr([-x for x in a])
def sub(a,b):return add(a,neg(b))
def scale(a,c):return tr([x*c for x in a])
def mul(a,b):
 if not a or not b:return []
 c=[0]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):c[i+j]=(c[i+j]+x*y)%P
 return tr(c)
def power(a,n):
 out=[1]
 for _ in range(n):out=mul(out,a)
 return out
def dm(a,b):
 a0=tr(a);b=tr(b);assert b
 a=list(a0);q=[0]*max(0,(len(a)-len(b)+1))
 inv=pow(b[-1],P-2,P)
 while a and len(a)>=len(b):
  k=len(a)-len(b);v=a[-1]*inv%P;q[k]=v
  for j,c in enumerate(b):a[j+k]=(a[j+k]-v*c)%P
  a=tr(a)
 q=tr(q)
 assert add(mul(q,b),a)==a0
 counts['divisions']+=1
 return q,a
def exact(a,b):
 q,r=dm(a,b);assert not r;return q
def xgcd(a,b):
 aa,bb=tr(a),tr(b)
 r0,r1=aa,bb;s0,s1=[1],[];t0,t1=[],[1]
 while r1:
  q,r2=dm(r0,r1)
  r0,r1=r1,r2;s0,s1=s1,sub(s0,mul(q,s1));t0,t1=t1,sub(t0,mul(q,t1))
 if not r0:return [],[],[]
 c=pow(r0[-1],P-2,P)
 g,s,t=scale(r0,c),scale(s0,c),scale(t0,c)
 assert add(mul(s,aa),mul(t,bb))==g
 counts['bezoutReturns']+=1
 return g,s,t
def gcd(a,b):return xgcd(a,b)[0]
def pol(v):
 if isinstance(v,list):return tr(v)
 return tr([v])
class R:
 def __init__(self,n=0,d=None):
  if isinstance(n,R):self.n=n.n;self.d=n.d;return
  n=pol(n);d=[1] if d is None else pol(d);assert d
  if not n:self.n=[];self.d=[1];return
  g=gcd(n,d);n=exact(n,g);d=exact(d,g)
  c=pow(d[-1],P-2,P);self.n=scale(n,c);self.d=scale(d,c)
 def __neg__(self):return R(neg(self.n),self.d)
 def __add__(self,v):
  v=R(v);return R(add(mul(self.n,v.d),mul(v.n,self.d)),mul(self.d,v.d))
 __radd__=__add__
 def __sub__(self,v):return self+-R(v)
 def __rsub__(self,v):return R(v)+-self
 def __mul__(self,v):
  v=R(v);return R(mul(self.n,v.n),mul(self.d,v.d))
 __rmul__=__mul__
 def __truediv__(self,v):
  v=R(v);assert v.n;return R(mul(self.n,v.d),mul(self.d,v.n))
 def __rtruediv__(self,v):return R(v)/self
 def __pow__(self,n):return R(power(self.n,n),power(self.d,n))
 def __eq__(self,v):
  v=R(v);return mul(self.n,v.d)==mul(v.n,self.d)
def pp(p):
 return {'degree':len(p)-1,'terms':sum(bool(c) for c in p),
         'sha256':hashlib.sha256(json.dumps(p,separators=(',',':')).encode()).hexdigest()}
def form(p):
 if not p:return '0'
 return ' + '.join(str(c)+(('*mu^'+str(i)) if i else '') for i,c in enumerate(p) if c)
mu=R([0,1])
A2=(mu*mu+4*mu+5)/2
B3=(mu**3+6*mu*mu+12*mu+7)/2
f=3*mu*mu+8*mu+9
n=1-mu*mu
r=n/f
assert r*f+mu*mu-1==0
assert r+1==4*A2/f
# These are the COMPLETE original leading quantities, in one common point:
# beta=u/ell, v(beta)=v(e)>0, beta/e -> r, mu finite.
# The other beta valuations and the r=-1 deeper-M branch are separate paper cases.
Mell=2*(r+1)/r
z2=4/(r+1)-mu-5
z1=(r*mu*mu+r*mu-2*mu-r-1)/(r+1)
Z0=-mu*(mu+1)
Rlead=Mell*B3*B3-4*A2**3
Nlead=-2*A2*(Z0+A2*z2)+Mell*B3*z1
FR=2*B3*B3-n*A2*A2
H=mu**4+7*mu**3+17*mu*mu+25*mu+10
FN=n*A2*(mu+1)*(mu*mu+4*mu+7)-2*B3*H
assert r*Rlead/2==2*A2*FR/f
assert n*Nlead==FN
counts['originalRationalReturns']+=4
assert FR.d==[1] and FN.d==[1]
G=mul(mul(n.n,f.n),A2.n)
def paid(p):
 p=tr(p)
 while len(p)>1:
  gg=gcd(p,G)
  if len(gg)==1:break
  p=exact(p,gg)
 return len(p)==1
for v in (r,Mell,z2,z1,Z0,Rlead,Nlead,FR,FN):
 assert paid(v.d)
say('new_original_ell_pole_common_center',
 originalDefinitionsBlob='47281af16fdd0ad7500ecda377c3cb9f9d65e725',
 place=P,branch='v(beta)=v(e)>0; r=bar(beta/e)!=0,-1; A2!=0; mu integral',
 sameOriginal_q2='r*(3*mu^2+8*mu+9)+mu^2-1',
 q2Substitution='r=(1-mu^2)/(3*mu^2+8*mu+9)',
 R6Scale='R6/ell^5',N5Scale='complete_N5/ell^4',
 paidResidualProduct='(1-mu^2)*(3*mu^2+8*mu+9)*A2',
 fullOriginalRationalIdentitiesReturned=True,
 FR=pp(FR.n),FN=pp(FN.n),
 FRFormula=form(FR.n),FNFormula=form(FN.n))
def strip(p):
 original=tr(p);out=list(original);removed=[1]
 while len(out)>1:
  gg=gcd(out,G)
  if len(gg)==1:break
  out=exact(out,gg);removed=mul(removed,gg)
 assert mul(out,removed)==original and paid(removed)
 return out,removed
rr,sr=strip(FR.n);nn,sn=strip(FN.n)
d,a,b=xgcd(rr,nn)
left=mul(a,sn);right=mul(b,sr);support=mul(sr,sn);target=mul(support,d)
assert add(mul(left,FR.n),mul(right,FN.n))==target
assert paid(support)
say('new_two_original_residue_bezout_complete',
 gcd=pp(d),gcdFormula=form(d),leftMultiplier=pp(left),rightMultiplier=pp(right),
 paidTargetFactor=pp(support),leftFormula=form(left),rightFormula=form(right),
 paidTargetFormula=form(support),wholeIdentityReturned=True,
 onlyProvedNonzeroResidualFactorsRemoved=True,
 residueCenterExcluded=(d==[1]),
 noOtherEllOrWeightCenterClaim=True,counts=counts)

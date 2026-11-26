#!/usr/bin/env python3
"""R150 S0/IH0 sextic: native QQ finite algebra and original equations.
No RootOf arithmetic or symbolic fraction gcd is used. All 6*2*2
parameter fibers are retained. Every inverse is multiplied back.
A final explicit QQ linear identity of original resultants is required.
"""
import hashlib,itertools,json,resource,signal,time
from pathlib import Path
from flint import fmpq,fmpq_mat
started=time.perf_counter();inverse_checks=[];failed_inverse_attempts=0
def say(o):
 o['elapsedSeconds']=round(time.perf_counter()-started,6)
 print(json.dumps(o,sort_keys=True),flush=True)
def alarm_handler(signum,frame):
 say({'status':'timeout_unknown','claimExcluded':False})
 raise SystemExit(124)
signal.signal(signal.SIGALRM,alarm_handler);signal.alarm(600)
class E:
 def __init__(self,R,c):self.R=R;self.c=tuple(c)
 def __bool__(self):return any(bool(v) for v in self.c)
 def __add__(self,o):
  o=self.R(o);return E(self.R,[a+b for a,b in zip(self.c,o.c)])
 __radd__=__add__
 def __neg__(self):return E(self.R,[-a for a in self.c])
 def __sub__(self,o):return self+-self.R(o)
 def __rsub__(self,o):return self.R(o)+-self
 def __mul__(self,o):return self.R.mul(self,self.R(o))
 __rmul__=__mul__
 def __pow__(self,n):
  if n<0:return self.inv()**(-n)
  out=self.R.one;v=self
  while n:
   if n&1:out=out*v
   v=v*v;n//=2
  return out
 def __eq__(self,o):
  try:o=self.R(o)
  except (TypeError,ValueError):return False
  return self.c==o.c
 def inv(self,label='algebra unit'):return self.R.inv(self,label)
 def __truediv__(self,o):return self*self.R(o).inv()
 def __rtruediv__(self,o):return self.R(o)*self.inv()
 def flat(self):return self.R.flat(self)
class A6:
 dim=6
 def __init__(self):
  self.mod=[fmpq(v,1280) for v in [-693,5810,-17150,21020,-8496,-1344]]
  self.zero=E(self,[fmpq(0)]*6);self.one=E(self,[fmpq(1)]+[fmpq(0)]*5)
 def __call__(self,v):
  if isinstance(v,E):
   if v.R is self:return v
   raise TypeError('incompatible finite algebra')
  return E(self,[fmpq(v)]+[fmpq(0)]*5)
 def basis(self,j):return E(self,[fmpq(int(i==j)) for i in range(6)])
 def mul(self,a,b):
  out=[fmpq(0)]*11
  for i,x in enumerate(a.c):
   if x:
    for j,y in enumerate(b.c):
     if y:out[i+j]+=x*y
  for k in range(10,5,-1):
   if out[k]:
    v=out[k]
    for j,m in enumerate(self.mod):out[k-6+j]-=v*m
  return E(self,out[:6])
 def inv(self,a,label):
  global failed_inverse_attempts
  if not a:
   failed_inverse_attempts+=1;raise ZeroDivisionError(label)
  columns=[(a*self.basis(j)).c for j in range(6)]
  mat=fmpq_mat([[columns[j][i] for j in range(6)] for i in range(6)])
  try:iv=mat.inv()
  except ZeroDivisionError:
   failed_inverse_attempts+=1;raise
  answer=E(self,[iv[i,0] for i in range(6)])
  assert a*answer==self.one
  inverse_checks.append({'degree':6,'label':label})
  return answer
 def flat(self,a):return list(a.c)
 def from_flat(self,v):return E(self,v)
class A2:
 def __init__(self,base,C1,C0,label):
  self.base=base;self.C1=base(C1);self.C0=base(C0);self.dim=2*base.dim;self.label=label
  self.zero=E(self,[base.zero,base.zero]);self.one=E(self,[base.one,base.zero])
 def __call__(self,v):
  if isinstance(v,E) and v.R is self:return v
  return E(self,[self.base(v),self.base.zero])
 def basis(self,j):
  return E(self,[self.base.basis(j),self.base.zero]) if j<self.base.dim else E(self,[self.base.zero,self.base.basis(j-self.base.dim)])
 def mul(self,a,b):
  ac=a.c[0]*b.c[0];bd=a.c[1]*b.c[1]
  return E(self,[ac+self.C0*bd,a.c[0]*b.c[1]+a.c[1]*b.c[0]+self.C1*bd])
 def inv(self,a,label):
  aa,bb=a.c
  norm=aa*aa+aa*bb*self.C1-bb*bb*self.C0
  iv=norm.inv(label+' norm')
  out=E(self,[(aa+bb*self.C1)*iv,-bb*iv])
  assert a*out==self.one
  inverse_checks.append({'degree':self.dim,'label':label})
  return out
 def flat(self,a):return self.base.flat(a.c[0])+self.base.flat(a.c[1])
 def from_flat(self,v):
  d=self.base.dim
  return E(self,[self.base.from_flat(v[:d]),self.base.from_flat(v[d:])])
K=A6();lam=K.basis(1);o=K.one
assert 1280*lam**6-1344*lam**5-8496*lam**4+21020*lam**3-17150*lam**2+5810*lam-693==0
def trim(p):
 p=list(p)
 while p and not p[-1]:p.pop()
 return p
def add(p,z):
 out=[K.zero]*max(len(p),len(z))
 for i in range(len(out)):out[i]=(p[i] if i<len(p) else K.zero)+(z[i] if i<len(z) else K.zero)
 return trim(out)
def neg(p):return [-v for v in p]
def sub(p,z):return add(p,neg(z))
def mul(p,z):
 if not p or not z:return []
 out=[K.zero]*(len(p)+len(z)-1)
 for i,a in enumerate(p):
  for j,b in enumerate(z):out[i+j]=out[i+j]+a*b
 return trim(out)
def sc(a,p):return trim([a*v for v in p])
def rem(p,z):
 p=trim(p);z=trim(z);iv=z[-1].inv('z Euclidean leading coefficient')
 while len(p)>=len(z) and p:
  shift=len(p)-len(z);cc=p[-1]*iv
  for i,v in enumerate(z):p[i+shift]=p[i+shift]-cc*v
  p=trim(p)
 return p
def gcd(p,z):
 while z:p,z=z,rem(p,z)
 return sc(p[-1].inv('z gcd leading coefficient'),p)
Z=[K.zero,K.one]
A=2*lam*lam-2*lam+1;C=-4*lam*lam+5*lam-2;s=2*lam-3;R=3-4*lam;j=2*lam-1
D=[s*C,-A]
I=add(add(sc(2*(4*lam-1)*C,D),mul(Z,sub([2*C*(1-lam)*R],sc(2*(4*lam*lam-7*lam+2),D)))),sc(-2*lam*C+s*j*R,mul(Z,Z)))
H=add(add(mul(D,sub(sub(mul(Z,add([4*lam*(1-lam)],sc(2*lam,Z))),sc(4*j,D)),[2*s*C])),sc(-2*(lam-1)*C,mul(Z,Z))),add(sc(2*C*C,Z),add(sc(-2*j*R,mul(mul(Z,Z),Z)),sc(4*j,mul(mul(Z,Z),D)))))
gz=gcd(I,H)
assert len(gz)==2 and gz[1]==1
z=-gz[0]
def ev(p,x):
 out=K.zero
 for cc in p[::-1]:out=out*x+cc
 return out
assert not ev(I,z) and not ev(H,z)
iz=z.inv('nonzero z');delta=s*s-4*z;idelta=delta.inv('distinct value discriminant')
l=(s*C-A*z)*iz*iz;Tm=C*iz;w=lam-1-Tm
assert l!=1
B=A2(K,s,-z,'value x')
x=E(B,[K.zero,K.one]);y=B(s)-x
b=(B(Tm)-B(l)*y)*(2*x-B(s))*B(idelta)
c=B(l)-b
b.inv('b');c.inv('c')
a2=-B(z)*c*(1-2*c)
a1=B(R)-B(z)*(2*B(l)-4*b*c)
a0=-B(z)*b*(1-2*b)
ia2=a2.inv('q quadratic leading coefficient')
T=A2(B,-a1*ia2,-a0*ia2,'q')
q=E(T,[B.zero,B.one])
lam=T(lam);z=T(z);l=T(l);w=T(w);b=T(b);c=T(c);a=1-l
h=1+T(x);k=1+T(y)
u=b+c*q;V2=b+c*q*q;half=T(fmpq(1,2));quarter=T(fmpq(1,4))
P0=half*(b+c*q**3-3*u*V2+2*u**3);P02=2*P0
for label,v in [('q',q),('q-1',q-1),('q+1',q+1),('u',u),('P0',P0),('h-1',h-1),('k-1',k-1),('h-k',h-k)]:
 v.inv(label)
assert a+w+b*h+c*k==lam
assert a+2*w+b*h*h+c*k*k==2*lam*lam
assert a+3*w+b*h**3+c*k**3==4*lam**3
assert h+k+1-2*lam==0
assert 3-4*lam-z*(l+u*(q+1-2*u)*q.inv('Af q'))==0
source_sha=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
say({'stage':'native_QQ_parameter_algebra_and_units_verified','dimension':24,'sourceSha256':source_sha,'inverseChecks':len(inverse_checks),'claimExcluded':False})
# Sparse f,t polynomials with coefficients in the exact 24-dimensional algebra.
class P:
 def __init__(self,co=None):self.co={ij:T(v) for ij,v in (co or {}).items() if T(v)}
 def __add__(self,o):
  if not isinstance(o,P):o=cp(o)
  d=dict(self.co)
  for ij,v in o.co.items():d[ij]=d.get(ij,T.zero)+v
  return P(d)
 __radd__=__add__
 def __neg__(self):return P({ij:-v for ij,v in self.co.items()})
 def __sub__(self,o):return self+-o
 def __mul__(self,o):
  if not isinstance(o,P):return scale(T(o),self)
  d={}
  for ij,v in self.co.items():
   for kl,vv in o.co.items():
    ijkl=(ij[0]+kl[0],ij[1]+kl[1])
    d[ijkl]=d.get(ijkl,T.zero)+v*vv
  return P(d)
 __rmul__=__mul__
 def __pow__(self,n):
  out=cp(1)
  for _ in range(n):out=out*self
  return out
 def __bool__(self):return bool(self.co)
 def degree(self):return max((sum(ij) for ij in self.co),default=-1)
def cp(v):return P({(0,0):T(v)})
def scale(v,p):return P({ij:v*vv for ij,vv in p.co.items()})
fp=P({(1,0):T.one});tp=P({(0,1):T.one});zero=P()
one=[cp(1),zero,cp(1),cp(1)]
def va(v,z):return [x+y for x,y in zip(v,z)]
def vs(p,v):return [p*x for x in v]
def vm(v,z):return [v[0]*z[0],v[0]*z[1]+v[1]*z[0],v[2]*z[2],v[3]*z[3]]
def tau(v):return scale(a,v[0])+v[1]+scale(b,v[2])+scale(c,v[3])
W1=cp(half*V2-u*u)+scale(2*u,fp)
W2=cp(u*V2-2*u**3+2*lam*P0)+scale(V2+2*u*u,fp)-scale(b*c*q,tp)
ib=(b*(q-1)).inv('b(q-1)');ic=(c*q*(q-1)).inv('cq(q-1)')
bx=scale(q*ib,W1)-scale(ib,W2);cy=scale(ic,W2-W1)
r=bx-cp(a)-scale(c,tp);ss=cy-cp(a*q)-scale(b,tp)
A1=scale(T(2),fp)-scale(2*b,bx)-scale(2*c,cy)+scale(2*b*c,tp)
rows=[[zero,zero,cp(1),cp(q)],[zero,A1,r,ss],[cp(1),r,zero,tp],[cp(q),ss,tp,zero]]
def DK(v):return [tau(vm(row,v)) for row in rows]
d=DK(one);F2=tau(d)
assert not (F2-scale(T(2),fp))
def P2(v):
 cen=va(v,vs(-tau(v),one))
 return tau(vm(vm(cen,cen),cen))
def N4(v):
 return scale(T(2),tau(vm(d,vm(v,v))))-F2*tau(vm(v,v))-scale(T(4),tau(v)*tau(vm(d,v)))+scale(T(2),F2*tau(v)**2)+tau(vm(v,DK(v)))
def Pjet2(v,z):
 v0=va(v,vs(-tau(v),one));z0=va(z,vs(-tau(z),one))
 return scale(T(3),tau(vm(vm(v0,v0),z0)))
def Njet4(v,z):return N4(va(v,z))-N4(v)-N4(z)
evv=[tau(vm(rows[0],rows[0])),scale(T(2),tau(vm(rows[0],rows[1]))),tau(vm(rows[2],rows[2])),tau(vm(rows[3],rows[3]))]
Emean=va(va(evv,vs(cp(-2),DK(d))),va(vs(cp(-2),vm(d,d)),vs(scale(T(2),F2),d)))
VV=[cp(1),cp(w),cp(h),cp(k)]
assert not Emean[0]
assert not (P2(rows[0])-cp(P02))
assert not (N4(rows[0])-cp(2*lam*P02))
assert not P2(VV) and not N4(VV)
polys=Emean[1:]+[Pjet2(rows[0],rows[1])-cp(3*w*P02),P2(rows[2])-cp(h**3*P02),P2(rows[3])-cp(k**3*P02),Njet4(rows[0],rows[1])-cp(4*lam*w*P02),N4(rows[2])-cp(2*lam*h*h*P02),N4(rows[3])-cp(2*lam*k*k*P02)]
names=['E1','EB','EC','P1','PB','PC','N1','NB','NC']
assert polys[3].degree()<=1
dig=hashlib.sha256()
for name,p in zip(names,polys):
 for ij,v in sorted(p.co.items()):dig.update((name+str(ij)+str([str(x) for x in v.flat()])+'\n').encode())
say({'stage':'all_original_nine_equations_verified','sourceSha256':source_sha,'inputSha256':dig.hexdigest(),'degrees':[p.degree() for p in polys],'inverseChecks':len(inverse_checks),'claimExcluded':False})
# A shear t=c*f+T allows a global invertible P1 coefficient. Each trial
# is tested inside the entire algebra; no parameter component is dropped.
aa=polys[3].co.get((1,0),T.zero);bb=polys[3].co.get((0,1),T.zero);cc=polys[3].co.get((0,0),T.zero)
iv=None;shear=None
for m in range(25):
 try:iv=(aa+m*bb).inv('P1 sheared f coefficient')
 except ZeroDivisionError:continue
 shear=m;break
if iv is None:
 say({'status':'P1_unit_cover_unresolved','claimExcluded':False})
 raise SystemExit(2)
def utrim(p):
 p=list(p)
 while p and not p[-1]:p.pop()
 return p
def ua(p,z):
 out=[T.zero]*max(len(p),len(z))
 for i in range(len(out)):out[i]=(p[i] if i<len(p) else T.zero)+(z[i] if i<len(z) else T.zero)
 return utrim(out)
def um(p,z):
 if not p or not z:return []
 out=[T.zero]*(len(p)+len(z)-1)
 for i,v in enumerate(p):
  for j,wv in enumerate(z):out[i+j]=out[i+j]+v*wv
 return utrim(out)
def up(p,n):
 out=[T.one]
 for _ in range(n):out=um(out,p)
 return out
fbar=[-cc*iv,-bb*iv]
tbar=ua([shear*v for v in fbar],[T.zero,T.one])
def substitute(p):
 out=[]
 for (i,j),v in p.co.items():out=ua(out,[v*x for x in um(up(fbar,i),up(tbar,j))])
 return out
ups=[substitute(p) for p in polys]
assert not ups[3]
def determinant(mat):
 n=len(mat)
 if n==0:return T.one
 if n==1:return mat[0][0]
 out=T.zero
 for j in range(n):
  if mat[0][j]:
   minor=[row[:j]+row[j+1:] for row in mat[1:]]
   out=out+((-1)**j)*mat[0][j]*determinant(minor)
 return out
def resultant(p,z):
 p=utrim(p);z=utrim(z)
 if not p or not z:return T.zero
 n=len(p)-1;m=len(z)-1
 if n==0:return p[0]**m if m else p[0]
 if m==0:return z[0]**n
 mat=[]
 for i in range(m):mat.append([T.zero]*i+p[::-1]+[T.zero]*(m-1-i))
 for i in range(n):mat.append([T.zero]*i+z[::-1]+[T.zero]*(n-1-i))
 return determinant(mat)
def unit_identity(elements):
 n=T.dim;columns=[]
 for v in elements:
  columns.extend([(v*T.basis(j)).flat() for j in range(n)])
 mat=fmpq_mat([[col[i] for col in columns]+[fmpq(int(i==0))] for i in range(n)])
 rr,rank=mat.rref()
 solution=[fmpq(0)]*len(columns)
 for i in range(n):
  pivot=next((j for j in range(len(columns)+1) if rr[i,j]),None)
  if pivot is None:continue
  if pivot==len(columns):return None
  solution[pivot]=rr[i,len(columns)]
 multipliers=[T.from_flat(solution[j*n:(j+1)*n]) for j in range(len(elements))]
 value=sum((m*v for m,v in zip(multipliers,elements)),T.zero)
 assert value==T.one
 hh=hashlib.sha256('\n'.join(str(v) for v in solution).encode()).hexdigest()
 return {'matrixRows':n,'matrixColumns':len(columns),'rank':int(rank),'multiplierSha256':hh,'identityMultipliedBack':True}
pairs=[(0,1),(0,2),(1,2)]
others=[4,5,6,7,8]
pairs.extend((i,j) for j in others for i in [0,1,2])
pairs.extend(itertools.combinations(others,2))
elements=[];used=[];certificate=None
for i,j in pairs:
 value=resultant(ups[i],ups[j]);elements.append(value);used.append([names[i],names[j]])
 certificate=unit_identity(elements)
 if certificate is not None:break
 if len(elements) in [3,6,12]:say({'stage':'resultant_identity_not_yet_unit','resultantCount':len(elements),'claimExcluded':False})
signal.alarm(0)
say({'schema':'r150-unit211-S0-IH0-native-QQ-algebra-v1','status':'exact_original_finite_fiber_excluded' if certificate else 'exact_resultant_candidates_remain','claimExcluded':certificate is not None,'claimLambdaLayerEmpty':False,'ordinaryISPClaim':False,'sourceSha256':source_sha,'inputSha256':dig.hexdigest(),'parameterAlgebraDimension':24,'inverseChecks':len(inverse_checks),'failedGlobalInverseTrials':failed_inverse_attempts,'P1Shear':shear,'univariateDegrees':[len(p)-1 for p in ups],'resultantPairs':used,'certificate':certificate,'peakRssKiB':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss})
raise SystemExit(0 if certificate else 2)

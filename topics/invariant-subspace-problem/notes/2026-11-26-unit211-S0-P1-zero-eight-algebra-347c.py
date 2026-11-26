#!/usr/bin/env python3
"""R150 S0: the entire zero-variable-coefficient P1 fiber.
All quartic lambda fibers and both value assignments are kept in QQ dimension 8.
The original N(V) coefficient is a genuine unit, so f is fixed; original
mean/highest/second-gradient equations remain in t. No numeric embedding.
"""
import hashlib,itertools,json,resource,signal,time
from pathlib import Path
from flint import fmpq,fmpq_mat,fmpq_poly
started=time.perf_counter();inverse_checks=[];failed_inverse_attempts=0
def say(o):
 o['elapsedSeconds']=round(time.perf_counter()-started,6)
 print(json.dumps(o,sort_keys=True),flush=True)
def alarm_handler(signum,frame):
 say({'status':'timeout_unknown','claimExcluded':False})
 raise SystemExit(124)
signal.signal(signal.SIGALRM,alarm_handler);signal.alarm(300)
# Exact polynomial cover: no assumption of irreducibility is needed.
L=fmpq_poly([0,1]);sp=2*L-3;Ap=2*L*L-2*L+1;Cp=-4*L*L+5*L-2
Dp=Ap-Cp;jp=2*L-1
M4=72*L**4-156*L**3+136*L**2-54*L+9
F6=(-8*Dp-3*sp)*Dp*jp*jp-sp**3*Dp+4*sp*sp*Cp
assert F6==-4*jp*jp*M4
assert Dp.gcd(sp*Cp).degree()==0
assert M4.gcd(jp*(4*L-1)*(L-1)).degree()==0
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
class A4:
 dim=4
 def __init__(self):
  self.mod=[fmpq(v,72) for v in [9,-54,136,-156]]
  self.zero=E(self,[fmpq(0)]*4);self.one=E(self,[fmpq(1)]+[fmpq(0)]*3)
 def __call__(self,v):
  if isinstance(v,E):
   if v.R is self:return v
   raise TypeError('incompatible finite algebra')
  return E(self,[fmpq(v)]+[fmpq(0)]*3)
 def basis(self,j):return E(self,[fmpq(int(i==j)) for i in range(4)])
 def mul(self,a,b):
  out=[fmpq(0)]*7
  for i,x in enumerate(a.c):
   if x:
    for j,y in enumerate(b.c):
     if y:out[i+j]+=x*y
  for k in range(6,3,-1):
   if out[k]:
    v=out[k]
    for j,m in enumerate(self.mod):out[k-4+j]-=v*m
  return E(self,out[:4])
 def inv(self,a,label):
  global failed_inverse_attempts
  if not a:
   failed_inverse_attempts+=1;raise ZeroDivisionError(label)
  columns=[(a*self.basis(j)).c for j in range(4)]
  mat=fmpq_mat([[columns[j][i] for j in range(4)] for i in range(4)])
  try:iv=mat.inv()
  except ZeroDivisionError:
   failed_inverse_attempts+=1;raise
  answer=E(self,[iv[i,0] for i in range(4)])
  assert a*answer==self.one
  inverse_checks.append({'degree':4,'label':label})
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
K=A4();la=K.basis(1)
assert 72*la**4-156*la**3+136*la**2-54*la+9==0
s0=2*la-3;Al=2*la*la-2*la+1;Cl=-4*la*la+5*la-2
D0=Al-Cl;j0=2*la-1
z0=s0*Cl*D0.inv('A-C');l0=-D0*s0.inv('s');Tm0=-l0
delta0=s0*s0-4*z0
assert delta0==(8*l0-3)*j0*j0
delta0.inv('value discriminant')
T=A2(K,0,delta0,'value difference')
dd=E(T,[K.zero,K.one])
lam=T(la);s=T(s0);z=T(z0);l=T(l0);Tm=T(Tm0);j=T(j0)
delta=T(delta0)
ij=j.inv('2lambda-1');idelta=delta.inv('value difference square')
p=1-dd*ij;q=1+dd*ij
b=(l-l*j*dd*idelta)*T(fmpq(1,2));c=l-b;a=1-l
h=1+(s+dd)*T(fmpq(1,2));k=1+(s-dd)*T(fmpq(1,2))
w=lam-1+l
u=b*p+c*q;Q=p*q;V2=b*p*p+c*q*q
half=T(fmpq(1,2));P0=half*(b*p**3+c*q**3-3*u*V2+2*u**3);P02=2*P0
assert u==2*l and Q==4*(1-2*l) and V2==2*u*u
assert P0==Q*l*(2*l-1)
assert a+w+b*h+c*k==lam
assert a+2*w+b*h*h+c*k*k==2*lam*lam
assert a+3*w+b*h**3+c*k**3==4*lam**3
assert h+k+1==2*lam
assert b*(h-1)+c*(k-1)==-l
Af=3-4*lam-z*(l+2*u*(1-u)*Q.inv('pq'))
assert Af==-(4*lam-1)*(2*lam-1)
Lval=q*(h-1)-p*(k-1)
assert Lval==4*dd*(lam-1)*ij
for label,v in [('lambda',lam),('z',z),('b',b),('c',c),('p',p),('q',q),('q-p',q-p),('u',u),('u-1',u-1),('P0',P0),('h-1',h-1),('k-1',k-1),('h-k',h-k),('L',Lval)]:
 v.inv(label)
cross=b*p*(k-1)+c*q*(h-1)
assert cross==2*l*(2*l*j-1)
fbar=(w*cross-z*lam*P02*Q.inv('pq in NV'))*Af.inv('original NV f coefficient')
source_sha=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
say({'stage':'all_eight_parameter_fibers_and_original_NV_unit_verified','dimension':8,'sourceSha256':source_sha,'inverseChecks':len(inverse_checks),'claimExcluded':False})
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
fp=cp(fbar);tp=P({(0,1):T.one});zero=P()
one=[cp(1),zero,cp(1),cp(1)]
def va(v,z):return [x+y for x,y in zip(v,z)]
def vs(p,v):return [p*x for x in v]
def vm(v,z):return [v[0]*z[0],v[0]*z[1]+v[1]*z[0],v[2]*z[2],v[3]*z[3]]
def tau(v):return scale(a,v[0])+v[1]+scale(b,v[2])+scale(c,v[3])
W1=cp(half*V2-u*u)+scale(2*u,fp)
W2=cp(u*V2-2*u**3+lam*P02)+scale(V2+2*u*u,fp)-scale(b*c*p*q,tp)
ib=(b*p*(q-p)).inv('bp(q-p)');ic=(c*q*(q-p)).inv('cq(q-p)')
bx=scale(q*ib,W1)-scale(ib,W2);cy=scale(ic,W2-scale(p,W1))
r=bx-cp(a*p)-scale(c,tp);ss=cy-cp(a*q)-scale(b,tp)
A1=scale(T(2),fp)-scale(2*b,bx)-scale(2*c,cy)+scale(2*b*c,tp)
rows=[[zero,zero,cp(p),cp(q)],[zero,A1,r,ss],[cp(p),r,zero,tp],[cp(q),ss,tp,zero]]
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
assert not polys[3]
dig=hashlib.sha256()
for name,po in zip(names,polys):
 assert all(ij[0]==0 for ij in po.co)
 for ij,v in sorted(po.co.items()):dig.update((name+str(ij)+str([str(x) for x in v.flat()])+'\n').encode())
def utrim(pp):
 pp=list(pp)
 while pp and not pp[-1]:pp.pop()
 return pp
ups=[utrim([po.co.get((0,j),T.zero) for j in range(po.degree()+1)]) for po in polys]
say({'stage':'all_original_nine_equations_verified','sourceSha256':source_sha,'inputSha256':dig.hexdigest(),'degrees':[len(po)-1 for po in ups],'P1IdenticallyZero':True,'inverseChecks':len(inverse_checks),'claimExcluded':False})
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
say({'schema':'r150-unit211-S0-P1zero-native-QQ-algebra-v1','status':'exact_original_eight_fibers_excluded' if certificate else 'exact_resultant_candidates_remain','claimExcluded':certificate is not None,'claimS0LayerEmpty':False,'claimLambdaLayerEmpty':False,'ordinaryISPClaim':False,'sourceSha256':source_sha,'inputSha256':dig.hexdigest(),'parameterAlgebraDimension':8,'inverseChecks':len(inverse_checks),'failedGlobalInverseTrials':failed_inverse_attempts,'P1IdenticallyZero':True,'univariateDegrees':[len(po)-1 for po in ups],'resultantPairs':used,'certificate':certificate,'peakRssKiB':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss})
raise SystemExit(0 if certificate else 2)

#!/usr/bin/env python3
"""R150 L=0,w=1: FLINT quadratic algebra and a paid unit denominator ledger.
The two lambda embeddings are kept over QQ[lambda]/(8lambda^2-6lambda-1).
All original nine equations are generated before projection. Both P1
elimination directions retain leading-coefficient zero fibers.
"""
import hashlib,itertools,json,resource,signal,time
from pathlib import Path
from flint import fmpq,fmpq_poly
started=time.perf_counter()
def say(o):
 o['elapsedSeconds']=round(time.perf_counter()-started,6)
 print(json.dumps(o,sort_keys=True),flush=True)
def alarm_handler(signum,frame):
 say({'status':'timeout_unknown','claimExcluded':False})
 raise SystemExit(124)
signal.signal(signal.SIGALRM,alarm_handler);signal.alarm(600)
QQ0=fmpq_poly([]);QQ1=fmpq_poly([1])
class Q:
 """Polynomial in rho with coefficients in the exact quadratic field."""
 def __init__(self,a=0,b=0):
  if isinstance(a,Q):self.a=a.a;self.b=a.b;return
  self.a=a if isinstance(a,fmpq_poly) else fmpq_poly([a])
  self.b=b if isinstance(b,fmpq_poly) else fmpq_poly([b])
 def __bool__(self):return bool(self.a) or bool(self.b)
 def __add__(self,o):o=Q(o);return Q(self.a+o.a,self.b+o.b)
 __radd__=__add__
 def __neg__(self):return Q(-self.a,-self.b)
 def __sub__(self,o):return self+-Q(o)
 def __rsub__(self,o):return Q(o)+-self
 def __mul__(self,o):
  o=Q(o);bd=self.b*o.b
  return Q(self.a*o.a+fmpq(1,8)*bd,self.a*o.b+self.b*o.a+fmpq(3,4)*bd)
 __rmul__=__mul__
 def __pow__(self,n):
  assert n>=0
  out=Q(1);v=self
  while n:
   if n&1:out=out*v
   v=v*v;n//=2
  return out
 def __eq__(self,o):return not (self-Q(o))
 def degree(self):return max(int(self.a.degree()),int(self.b.degree()))
 def conj(self):return Q(self.a+fmpq(3,4)*self.b,-self.b)
 def norm(self):return self.a*self.a+fmpq(3,4)*self.a*self.b-fmpq(1,8)*self.b*self.b
 def invconst(self):
  assert self.degree()<=0 and self
  nn=self.norm()[0];assert nn
  out=Q(self.conj().a/nn,self.conj().b/nn)
  assert self*out==1
  return out
 def shift(self,n):return Q(self.a.left_shift(n),self.b.left_shift(n))
 def leading(self):
  d=self.degree();return Q(self.a[d],self.b[d]) if d>=0 else Q()
 def serial(self):return str(self.a)+' |lambda| '+str(self.b)
def qdivexact(p,z):
 if not p:return Q()
 nn=z.norm();vv=p*z.conj()
 aa,ar=divmod(vv.a,nn);bb,br=divmod(vv.b,nn)
 if ar or br:return None
 out=Q(aa,bb);assert out*z==p
 return out
def qdivrem(p,z):
 assert z
 quo=Q();rem=Q(p);iv=z.leading().invconst();d=z.degree()
 while rem and rem.degree()>=d:
  sh=rem.degree()-d;cc=(rem.leading()*iv).shift(sh)
  quo=quo+cc;rem=rem-cc*z
 return quo,rem
def qgcd(p,z):
 while z:p,z=z,qdivrem(p,z)[1]
 return p*p.leading().invconst() if p else p
lamq=Q(0,1);rhoq=Q(fmpq_poly([0,1]))
assert 8*lamq*lamq-6*lamq-1==0
Al=2*lamq**2-2*lamq+1;Bl=4*lamq**3-6*lamq**2+3*lamq-1;Rc=lamq-2
Cc=Rc*Bl-Al*Al
assert Cc==3*(7-10*lamq)*Q(fmpq(1,16))
assert Cc
Dq=Al-Rc*rhoq;Nq=Bl-Al*rhoq
Mq=Bl-2*Al*rhoq+Rc*rhoq*rhoq
Jq=Bl-Rc*rhoq*rhoq
units=[rhoq,Dq,Nq,Mq,Jq]
power_cache={(i,0):Q(1) for i in range(5)}
product_cache={(0,0,0,0,0):Q(1)}
def denpoly(exps):
 exps=tuple(exps)
 if exps in product_cache:return product_cache[exps]
 out=Q(1)
 for i,e in enumerate(exps):
  if (i,e) not in power_cache:power_cache[i,e]=units[i]**e
  out=out*power_cache[i,e]
 product_cache[exps]=out
 return out
class R:
 def __init__(self,n=0,e=(0,0,0,0,0)):
  if isinstance(n,R):self.n=n.n;self.e=n.e;return
  self.n=Q(n);self.e=tuple(e) if self.n else (0,0,0,0,0)
 def __bool__(self):return bool(self.n)
 def __add__(self,o):
  o=R(o);ee=tuple(max(i,j) for i,j in zip(self.e,o.e))
  return R(self.n*denpoly(tuple(i-j for i,j in zip(ee,self.e)))+o.n*denpoly(tuple(i-j for i,j in zip(ee,o.e))),ee)
 __radd__=__add__
 def __neg__(self):return R(-self.n,self.e)
 def __sub__(self,o):return self+-R(o)
 def __rsub__(self,o):return R(o)+-self
 def __mul__(self,o):
  o=R(o);return R(self.n*o.n,tuple(i+j for i,j in zip(self.e,o.e)))
 __rmul__=__mul__
 def __pow__(self,n):return R(self.n**n,tuple(e*n for e in self.e))
 def __eq__(self,o):return not (self-R(o))
lam=R(lamq);rho=R(rhoq)
q=R(Nq,(1,1,0,0,0))
b=R(Cc,(1,0,0,1,0))
c=R(Dq**3,(0,0,1,1,0))
a=1-b-c
u=R(Rc,(1,0,0,0,0));V2=R(Al,(2,0,0,0,0))
P0=R(6*lamq-Q(fmpq(11,2)),(3,0,0,0,0));P02=2*P0
h=1+rho;k=1+rho*q;w=R(1)
half=R(fmpq(1,2));quarter=R(fmpq(1,4))
assert b+c*q==u and b+c*q*q==V2
assert half*(b+c*q**3-3*u*V2+2*u**3)==P0
assert a+1+b*h+c*k==lam
assert a+2+b*h*h+c*k*k==2*lam*lam
assert a+3+b*h**3+c*k**3==4*lam**3
assert q*(h-1)-(k-1)==0
# No norm denominator is introduced: every denominator belongs to the
# paid list rho,Dq,Nq,Mq,Jq. In particular Dq=0 was already excluded by Cc!=0.
ib=R(rhoq*rhoq*Dq*Cc.invconst())
ic=R(rhoq*rhoq,(0,1,0,0,0))
assert ib*b*(q-1)==1 and ic*c*q*(q-1)==1
source_sha=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
say({'stage':'paid_unit_parameter_graph_verified','sourceSha256':source_sha,'unitDegrees':[v.degree() for v in units],'claimExcluded':False})
class P:
 def __init__(self,co=None):self.co={ij:R(v) for ij,v in (co or {}).items() if R(v)}
 def __bool__(self):return bool(self.co)
 def __add__(self,o):
  if not isinstance(o,P):o=cp(o)
  dd=dict(self.co)
  for ij,v in o.co.items():dd[ij]=dd.get(ij,R())+v
  return P(dd)
 __radd__=__add__
 def __neg__(self):return P({ij:-v for ij,v in self.co.items()})
 def __sub__(self,o):return self+-o
 def __mul__(self,o):
  if not isinstance(o,P):return scale(R(o),self)
  dd={}
  for ij,v in self.co.items():
   for kl,vv in o.co.items():
    key=(ij[0]+kl[0],ij[1]+kl[1]);dd[key]=dd.get(key,R())+v*vv
  return P(dd)
 __rmul__=__mul__
 def __pow__(self,n):
  out=cp(1)
  for _ in range(n):out=out*self
  return out
def cp(v):return P({(0,0):R(v)})
def scale(v,p):return P({ij:v*vv for ij,vv in p.co.items()})
fp=P({(1,0):R(1)});tp=P({(0,1):R(1)});zero=P()
one=[cp(1),zero,cp(1),cp(1)]
def va(v,z):return [x+y for x,y in zip(v,z)]
def vs(p,v):return [p*x for x in v]
def vm(v,z):return [v[0]*z[0],v[0]*z[1]+v[1]*z[0],v[2]*z[2],v[3]*z[3]]
def tau(v):return scale(a,v[0])+v[1]+scale(b,v[2])+scale(c,v[3])
W1=cp(half*V2-u*u)+scale(2*u,fp)
W2=cp(u*V2-2*u**3+2*lam*P0)+scale(V2+2*u*u,fp)-scale(b*c*q,tp)
bx=scale(q*ib,W1)-scale(ib,W2);cy=scale(ic,W2-W1)
r=bx-cp(a)-scale(c,tp);s=cy-cp(a*q)-scale(b,tp)
A1=scale(R(2),fp)-scale(2*b,bx)-scale(2*c,cy)+scale(2*b*c,tp)
rows=[[zero,zero,cp(1),cp(q)],[zero,A1,r,s],[cp(1),r,zero,tp],[cp(q),s,tp,zero]]
def DK(v):return [tau(vm(row,v)) for row in rows]
d=DK(one);F2=tau(d)
assert not (F2-scale(R(2),fp))
def P2(v):
 cen=va(v,vs(-tau(v),one))
 return tau(vm(vm(cen,cen),cen))
def N4(v):
 return scale(R(2),tau(vm(d,vm(v,v))))-F2*tau(vm(v,v))-scale(R(4),tau(v)*tau(vm(d,v)))+scale(R(2),F2*tau(v)**2)+tau(vm(v,DK(v)))
def Pjet2(v,z):
 v0=va(v,vs(-tau(v),one));z0=va(z,vs(-tau(z),one))
 return scale(R(3),tau(vm(vm(v0,v0),z0)))
def Njet4(v,z):return N4(va(v,z))-N4(v)-N4(z)
ev=[tau(vm(rows[0],rows[0])),scale(R(2),tau(vm(rows[0],rows[1]))),tau(vm(rows[2],rows[2])),tau(vm(rows[3],rows[3]))]
E=va(va(ev,vs(cp(-2),DK(d))),va(vs(cp(-2),vm(d,d)),vs(scale(R(2),F2),d)))
VV=[cp(1),cp(1),cp(h),cp(k)]
assert not E[0] and not (P2(rows[0])-cp(P02)) and not (N4(rows[0])-cp(2*lam*P02))
assert not P2(VV) and not N4(VV)
polys=E[1:]+[Pjet2(rows[0],rows[1])-cp(3*P02),P2(rows[2])-cp(h**3*P02),P2(rows[3])-cp(k**3*P02),Njet4(rows[0],rows[1])-cp(4*lam*P02),N4(rows[2])-cp(2*lam*h*h*P02),N4(rows[3])-cp(2*lam*k*k*P02)]
names=['E1','EB','EC','P1','PB','PC','N1','NB','NC']
def strip_list(vs0):
 vs0=list(vs0)
 for unit in units:
  while any(bool(v) for v in vs0):
   quot=[qdivexact(v,unit) for v in vs0]
   if any(v is None for v in quot):break
   vs0=quot
 return vs0
cleared=[]
for poly in polys:
 ee=tuple(max((v.e[i] for v in poly.co.values()),default=0) for i in range(5))
 keys=sorted(poly.co)
 nums=[poly.co[key].n*denpoly(tuple(i-j for i,j in zip(ee,poly.co[key].e))) for key in keys]
 nums=strip_list(nums)
 cleared.append({key:v for key,v in zip(keys,nums) if v})
assert max((sum(ij) for ij in cleared[3]),default=-1)<=1
dig=hashlib.sha256()
profiles=[]
for name,poly in zip(names,cleared):
 for ij,v in sorted(poly.items()):dig.update((name+str(ij)+v.serial()+'\n').encode())
 profiles.append({'name':name,'ftDegree':max((sum(ij) for ij in poly),default=-1),'rhoDegree':max((v.degree() for v in poly.values()),default=-1),'termsFT':len(poly)})
say({'stage':'all_original_equations_generated_and_verified','sourceSha256':source_sha,'inputSha256':dig.hexdigest(),'profiles':profiles,'claimExcluded':False})
def utr(p):
 p=list(p)
 while p and not p[-1]:p.pop()
 return p
def ua(p,z):
 out=[Q()]*max(len(p),len(z))
 for i in range(len(out)):out[i]=(p[i] if i<len(p) else Q())+(z[i] if i<len(z) else Q())
 return utr(out)
def um(p,z):
 if not p or not z:return []
 out=[Q()]*(len(p)+len(z)-1)
 for i,v in enumerate(p):
  for j,vv in enumerate(z):out[i+j]=out[i+j]+v*vv
 return utr(out)
def up(p,n):
 out=[Q(1)]
 for _ in range(n):out=um(out,p)
 return out
def project(poly,orientation):
 pp={((ij[0],ij[1]) if orientation==0 else (ij[1],ij[0])):v for ij,v in poly.items()}
 line={((ij[0],ij[1]) if orientation==0 else (ij[1],ij[0])):v for ij,v in cleared[3].items()}
 aa=line.get((1,0),Q());bb=line.get((0,1),Q());cc=line.get((0,0),Q())
 dd=max((ij[0] for ij in pp),default=0)
 out=[]
 for (i,j),v in pp.items():
  term=[v*aa**(dd-i)*vv for vv in up([-cc,-bb],i)]
  out=ua(out,[Q()]*j+term)
 return utr(strip_list(out))
def det(mat):
 n=len(mat)
 if n==0:return Q(1)
 if n==1:return mat[0][0]
 out=Q()
 for j in range(n):
  if mat[0][j]:out=out+((-1)**j)*mat[0][j]*det([row[:j]+row[j+1:] for row in mat[1:]])
 return out
def res(p,z):
 p=utr(p);z=utr(z)
 if not p or not z:return Q()
 n=len(p)-1;m=len(z)-1
 if n==0:return p[0]**m if m else p[0]
 if m==0:return z[0]**n
 mat=[]
 for i in range(m):mat.append([Q()]*i+p[::-1]+[Q()]*(m-1-i))
 for i in range(n):mat.append([Q()]*i+z[::-1]+[Q()]*(n-1-i))
 return strip_list([det(mat)])[0]
projected=[[project(poly,o) for poly in cleared] for o in [0,1]]
pairs=[(0,1),(0,2),(1,2)]
others=[4,5,6,7,8]
pairs.extend((i,j) for j in others for i in [0,1,2])
pairs.extend(itertools.combinations(others,2))
history=[];resultants=[];normg=QQ0;excluded=False
for pair in pairs:
 for orientation in [0,1]:
  i,j=pair;rr=res(projected[orientation][i],projected[orientation][j])
  resultants.append(rr)
  nn=rr.norm()
  normg=normg.gcd(nn) if normg else nn
  history.append({'orientation':orientation,'pair':[names[i],names[j]],'rhoDegree':rr.degree(),'normGcdDegree':int(normg.degree())})
  if normg and normg.degree()==0:
   excluded=True;break
 if excluded:break
 if len(history) in [6,12,24]:say({'stage':'exact_projection_norm_gcd','last':history[-1],'claimExcluded':False})
# A QQ norm gcd is only a necessary projection. If it retains conjugate
# cross-intersections, compute the actual quadratic-field gcd as well.
field_gcd=None
if not excluded and normg:
 field_gcd=Q(normg)
 for rr in resultants:
  aa=divmod(rr.a,normg)[1];bb=divmod(rr.b,normg)[1]
  field_gcd=qgcd(field_gcd,Q(aa,bb))
  field_gcd=strip_list([field_gcd])[0]
  if field_gcd and field_gcd.degree()==0:
   excluded=True;break
signal.alarm(0)
report={'schema':'r150-unit211-L0-w1-native-unit-ledger-v1','status':'exact_original_fiber_excluded' if excluded else 'exact_projection_candidates_remain','claimExcluded':excluded,'claimLambdaLayerEmpty':False,'ordinaryISPClaim':False,'sourceSha256':source_sha,'inputSha256':dig.hexdigest(),'projectionHistory':history,'finalNormGcdDegree':int(normg.degree()),'finalFieldGcdDegree':None if field_gcd is None else field_gcd.degree(),'peakRssKiB':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}
if field_gcd is not None and 0<field_gcd.degree()<=12 and len(field_gcd.serial())<8000:report['remainingFieldPolynomial']=field_gcd.serial()
say(report)
raise SystemExit(0 if excluded else 2)

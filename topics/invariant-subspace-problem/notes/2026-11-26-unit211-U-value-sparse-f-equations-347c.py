#!/usr/bin/env python3
"""R150 U-value chart, sparse in f with four-variable rational coefficients.
The matrix selects ISP_U_CONDITION; the fallback is the t/f graph.
--condition NAME generates
one original necessary polynomial; --condition all generates all nine.
No claim of physical sufficiency or emptiness is made.
"""
import argparse,hashlib,json,os,resource,signal,time
from pathlib import Path
from flint import fmpq,fmpq_mpoly_ctx
started=time.perf_counter()
ap=argparse.ArgumentParser()
ap.add_argument('--condition',default=os.environ.get('ISP_U_CONDITION','chart'),choices=['chart','E1','EB','EC','P1','PB','PC','N1','NB','NC','jet','all'])
ap.add_argument('--seconds',type=int,default=180)
args=ap.parse_args()
def say(o):
 o['elapsedSeconds']=round(time.perf_counter()-started,6)
 print(json.dumps(o,sort_keys=True),flush=True)
def alarm_handler(signum,frame):
 say({'status':'timeout_unknown','target':args.condition,'claimExcluded':False})
 raise SystemExit(124)
signal.signal(signal.SIGALRM,alarm_handler);signal.alarm(args.seconds)
ctx=fmpq_mpoly_ctx.get(('q','lam','h','k'),'lex')
qp,lp,hp,kp=ctx.gens();zero=ctx.constant(0);unit=ctx.constant(1)
class R:
 def __init__(self,n=0,d=None,reduce=True):
  if isinstance(n,R):self.n=n.n;self.d=n.d;return
  n=n if hasattr(n,'to_dict') else ctx.constant(n)
  d=unit if d is None else d
  assert d
  if not n:self.n=zero;self.d=unit;return
  if reduce:
   gg=n.gcd(d);n=n/gg;d=d/gg
  self.n=n;self.d=d
 def __add__(self,o):o=R(o);return R(self.n*o.d+o.n*self.d,self.d*o.d)
 __radd__=__add__
 def __neg__(self):return R(-self.n,self.d,False)
 def __sub__(self,o):return self+-R(o)
 def __rsub__(self,o):return R(o)+-self
 def __mul__(self,o):o=R(o);return R(self.n*o.n,self.d*o.d)
 __rmul__=__mul__
 def __truediv__(self,o):o=R(o);return R(self.n*o.d,self.d*o.n)
 def __rtruediv__(self,o):return R(o)/self
 def __pow__(self,n):return R(self.n**n,self.d**n,False) if n>=0 else R(self.d**(-n),self.n**(-n),False)
 def iszero(self):return not self.n
def eq(x,y):assert (R(x)-R(y)).iszero()
def degrees(p):return [int(max((mm[j] for mm in p.to_dict()),default=-1)) for j in range(4)]
q=R(qp);lam=R(lp);h=R(hp);k=R(kp)
Al=2*lam**2-2*lam+1;Bl=4*lam**3-6*lam**2+3*lam-1
b=(Bl-(k-1)*Al)/((h-1)**2*(h-k))
c=((h-1)*Al-Bl)/((k-1)**2*(h-k))
a=1-b-c;l=b+c
w=lam-a-b*h-c*k
u=b+c*q;V2=b+c*q*q
P0=(b+c*q**3-3*u*V2+2*u**3)/2
L=q*(h-1)-(k-1);S=h+k+1-2*lam
# All rows of the E0/N0 graph are affine in f,t.
rf=(2*q*u-V2-2*u*u)/(b*(q-1))
sf=(V2+2*u*u-2*u)/(c*q*(q-1))
rt=c/(q-1);st=-b*q/(q-1)
rc=(q*(V2/2-u*u)-(u*V2-2*u**3+2*lam*P0))/(b*(q-1))-a
sc=((u*V2-2*u**3+2*lam*P0)-(V2/2-u*u))/(c*q*(q-1))-a*q
Af=2*(1-l-u*(q+1-2*u)/q)
Ac=((2*u-q-1)*(V2-2*u*u)+4*lam*P0)/q
def CC(z):return 1+z+z*z-2*lam*(1+z)
nvf=(3-4*lam)*Af+2*b*CC(h)*rf+2*c*CC(k)*sf
nvc=(3-4*lam)*Ac+2*b*CC(h)*rc+2*c*CC(k)*sc+2*b*(a*CC(h)+w*(2+h-2*lam))+2*c*q*(a*CC(k)+w*(2+k-2*lam))
nvt=2*b*c*L*S/(q-1)
tf=-nvf/nvt;tc=-nvc/nvt
units=[qp,qp-1,qp+1,lp,hp-1,kp-1,hp-kp,b.n,c.n,P0.n,L.n,S.n]
def strip_units(po):
 for atom in units:
  while po:
   g=po.gcd(atom)
   if g.total_degree()==0:break
   po=po/g
 return po
for ex in [rf,sf,rt,st,rc,sc,Af,Ac,tf,tc]:
 assert strip_units(ex.d).total_degree()==0
eq(nvf+nvt*tf,0);eq(nvc+nvt*tc,0)
source_sha=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
say({'stage':'four_parameter_linear_t_graph_verified','sourceSha256':source_sha,'target':args.condition,'rationalCoefficientVariables':['q','lambda','h','k'],'remainingPolynomialVariable':'f','tSlope':{'numeratorDegrees':degrees(tf.n),'numeratorTerms':len(tf.n.to_dict()),'denominatorDegrees':degrees(tf.d),'denominatorTerms':len(tf.d.to_dict())},'tConstant':{'numeratorDegrees':degrees(tc.n),'numeratorTerms':len(tc.n.to_dict()),'denominatorDegrees':degrees(tc.d),'denominatorTerms':len(tc.d.to_dict())},'claimExcluded':False})
if args.condition=='chart':
 signal.alarm(0)
 say({'status':'original_linear_chart_verified_only','sourceSha256':source_sha,'claimNineEquationsGenerated':False,'claimLambdaLayerEmpty':False,'ordinaryISPClaim':False,'peakRssKiB':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss})
 raise SystemExit(0)
# Polynomial arithmetic only in f; coefficient gcds never involve f or t.
def trim(p):
 p=list(p)
 while p and p[-1].iszero():p.pop()
 return p
def cp(x):return trim([R(x)])
def plus(p,z):
 out=[R(0) for _ in range(max(len(p),len(z)))]
 for j in range(len(out)):out[j]=(p[j] if j<len(p) else R(0))+(z[j] if j<len(z) else R(0))
 return trim(out)
def neg(p):return [-v for v in p]
def minus(p,z):return plus(p,neg(z))
def times(p,z):
 if not p or not z:return []
 out=[R(0) for _ in range(len(p)+len(z)-1)]
 for i,v in enumerate(p):
  for j,vv in enumerate(z):out[i+j]=out[i+j]+v*vv
 return trim(out)
def scale(c0,p):return trim([c0*v for v in p])
def power(p,n):
 out=cp(1)
 for _ in range(n):out=times(out,p)
 return out
fp=[R(0),R(1)];zp=[]
one=[cp(1),zp,cp(1),cp(1)]
trow=[tc,tf]
rrow=[rc+rt*tc,rf+rt*tf]
srow=[sc+st*tc,sf+st*tf]
Arow=[Ac,Af]
rows=[[zp,zp,cp(1),cp(q)],[zp,Arow,rrow,srow],[cp(1),rrow,zp,trow],[cp(q),srow,trow,zp]]
def va(v,z):return [plus(x,y) for x,y in zip(v,z)]
def vs(p,v):return [times(p,x) for x in v]
def vm(v,z):return [times(v[0],z[0]),plus(times(v[0],z[1]),times(v[1],z[0])),times(v[2],z[2]),times(v[3],z[3])]
def tau(v):return plus(plus(scale(a,v[0]),v[1]),plus(scale(b,v[2]),scale(c,v[3])))
def DK(v):return [tau(vm(row,v)) for row in rows]
d=DK(one);F2=tau(d)
assert not minus(F2,scale(R(2),fp))
def P2(v):
 cen=va(v,vs(neg(tau(v)),one))
 return tau(vm(vm(cen,cen),cen))
def N4(v):
 value=scale(R(2),tau(vm(d,vm(v,v))))
 value=minus(value,times(F2,tau(vm(v,v))))
 value=minus(value,scale(R(4),times(tau(v),tau(vm(d,v)))))
 value=plus(value,scale(R(2),times(F2,power(tau(v),2))))
 return plus(value,tau(vm(v,DK(v))))
def Pjet2(v,z):
 v0=va(v,vs(neg(tau(v)),one));z0=va(z,vs(neg(tau(z)),one))
 return scale(R(3),tau(vm(vm(v0,v0),z0)))
def Njet4(v,z):return minus(minus(N4(va(v,z)),N4(v)),N4(z))
P02=2*P0
def original_condition(name):
 if name.startswith('E'):
  j={'E1':1,'EB':2,'EC':3}[name]
  e=scale(R(2),tau(vm(rows[0],rows[1]))) if j==1 else tau(vm(rows[j],rows[j]))
  term=minus(e,scale(R(2),DK(d)[j]))
  term=minus(term,scale(R(2),vm(d,d)[j]))
  return plus(term,scale(R(2),times(F2,d[j])))
 if name=='P1':return minus(Pjet2(rows[0],rows[1]),cp(3*w*P02))
 if name=='PB':return minus(P2(rows[2]),cp(h**3*P02))
 if name=='PC':return minus(P2(rows[3]),cp(k**3*P02))
 if name=='N1':return minus(Njet4(rows[0],rows[1]),cp(4*lam*w*P02))
 if name=='NB':return minus(N4(rows[2]),cp(2*lam*h*h*P02))
 if name=='NC':return minus(N4(rows[3]),cp(2*lam*k*k*P02))
 if name=='jet':return minus(scale(R(3),Njet4(rows[0],rows[1])),scale(4*lam,Pjet2(rows[0],rows[1])))
 raise ValueError(name)
targets=['E1','EB','EC','P1','PB','PC','N1','NB','NC','jet'] if args.condition=='all' else [args.condition]
for name in targets:
 po=original_condition(name)
 assert len(po)<= (3 if name.startswith('E') or name=='jet' else 4)
 den=unit
 for co in po:
  assert strip_units(co.d).total_degree()==0
  den=den*(co.d/den.gcd(co.d))
 nums=[co.n*(den/co.d) for co in po]
 # Remove only common coefficient factors made from paid chart units.
 for atom in units:
  while nums:
   g=atom
   for num in nums:g=g.gcd(num)
   if g.total_degree()==0:break
   nums=[num/g for num in nums]
 hh=hashlib.sha256()
 for num in nums:hh.update((str(sorted(num.to_dict().items()))+'\n').encode())

 if name=='P1':
  assert len(nums)<=2
  ffactors=[]
  if len(nums)==2:
   for fac,mult in nums[1].factor()[1]:
    spelling=str(fac)
    ffactors.append({'degrees':degrees(fac),'multiplicity':int(mult),'terms':len(fac.to_dict()),'polynomial':spelling if len(spelling.encode())<6000 else None,'sha256':hashlib.sha256(spelling.encode()).hexdigest()})
  say({'stage':'original_highest_jet_f_coefficient_factors','fDegree':len(nums)-1,'factors':ffactors,'claimExcluded':False})
 say({'stage':'original_condition_generated','name':name,'fDegree':len(nums)-1,'coefficientProfiles':[{'degrees':degrees(num),'terms':len(num.to_dict())} for num in nums],'clearedInputSha256':hh.hexdigest(),'sourceSha256':source_sha,'claimExcluded':False})
signal.alarm(0)
say({'status':'requested_original_conditions_generated','target':args.condition,'sourceSha256':source_sha,'claimPhysicalSufficiency':False,'claimLambdaLayerEmpty':False,'ordinaryISPClaim':False,'peakRssKiB':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss})

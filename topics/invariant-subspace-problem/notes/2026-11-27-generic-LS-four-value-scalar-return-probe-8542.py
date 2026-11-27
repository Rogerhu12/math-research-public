#!/usr/bin/env python3
"""R150 general LS, original two-line determinant zero: global monic value
quadratic and three original linear returns, with no ell/T/equal-weight division.
All reductions are multiplied back; four original Gram quadratics give further
necessary parameter minors. This is a reduction certificate, not exclusion.
"""
import json,time,os,sys,hashlib,subprocess,shutil,tempfile,resource
from pathlib import Path
from flint import fmpq,fmpq_mpoly_ctx
import signal
signal.alarm(60)
resource.setrlimit(resource.RLIMIT_AS,(4*1024**3,4*1024**3))
start=time.perf_counter()
def say(x):x['seconds']=time.perf_counter()-start;print(json.dumps(x),flush=True)
ctx=fmpq_mpoly_ctx.get(('s','z','eps','lam','f','t','unused0','unused1'),'lex');lp,up,Qp,Lp,fp,tp,eta0p,z0p=ctx.gens();zz=ctx.constant(0);oo=ctx.constant(1)
def poly(v):return v if hasattr(v,'to_dict') else ctx.constant(v)
class R:
 def __init__(self,n=0,d=None,reduce=True):
  if isinstance(n,R):self.n=n.n;self.d=n.d;return
  n=poly(n);d=oo if d is None else poly(d);assert d
  if not n:self.n=zz;self.d=oo;return
  if reduce:
   g=n.gcd(d);n=n/g;d=d/g
  lc=d.coefficient(0);self.n=n/lc;self.d=d/lc
 def __bool__(self):return bool(self.n)
 def __add__(self,o):
  o=R(o)
  if not self:return o
  if not o:return self
  g=self.d.gcd(o.d);a=self.d/g;b=o.d/g
  return R(self.n*b+o.n*a,a*o.d)
 __radd__=__add__
 def __neg__(self):return R(-self.n,self.d,False)
 def __sub__(self,o):return self+-R(o)
 def __rsub__(self,o):return R(o)+-self
 def __mul__(self,o):
  o=R(o)
  if not self or not o:return R()
  g=self.n.gcd(o.d);h=o.n.gcd(self.d)
  return R((self.n/g)*(o.n/h),(self.d/h)*(o.d/g),False)
 __rmul__=__mul__
 def __truediv__(self,o):o=R(o);assert o;return self*R(o.d,o.n,False)
 def __rtruediv__(self,o):return R(o)/self
 def __pow__(self,n):return R(self.d**(-n),self.n**(-n),False) if n<0 else R(self.n**n,self.d**n,False)
 def __eq__(self,o):o=R(o);return self.n*o.d==o.n*self.d
sm,zm,eps,lam,f,t=map(R,ctx.gens()[:6])
A2=2*lam*lam-2*lam+1;B3=4*lam**3-6*lam*lam+3*lam-1
Tnew=(sm*A2-B3)/zm
l=(A2*(sm*sm-zm)-sm*B3)/(zm*zm)
deltaValue=sm*sm-4*zm
u=l+eps*(2*Tnew-l*sm)
Q=1-eps*eps*deltaValue
Delta=1-Q

# Exact substitution into the previously proved scalar identities only;
# the large original Gram is not expanded again in these rational coordinates.
T=Tnew;v0=sm/2;v1=1/(2*eps);zeta=v0-v1
bc=(l*l-(2*T-l*sm)**2/deltaValue)/4
assert l*A2-T*T==bc*deltaValue
S=sm+3-2*lam;V2=2*u-l*Q;T0=V2-2*u*u
P02=(2-3*u)*V2-Q*u+2*u**3
J=2*u*(1-u)+l*Q;Phi=T0+4*u-4+Q;Pf=T0*(J-Q);Pt=bc*Q*Phi
G=lam*P02-(1-u)*T0;ww=lam-1-T;Pc=Q*P02*(l+T)-G*T0
say({'stage':'new_scalar_substitution_weights_and_moments_built','sourceOfScalarIdentities':'ea0ffae265bd5f89cbbb98edf58c7dbc6375a36698a5a5e0508483de669a17ba','peakRssKiB':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss})
NF=(3-4*lam)*Q-zm*J+S*(2*u*Q*v1+zeta*J)
NT=bc*Q*S*zeta
R1=u*(3-2*lam+v0+v1)-l*Q*v1
NC=G*(zm-S*zeta)+S*Q*T0*v1/2+Q*ww*R1
DE=Phi*NF-S*zeta*Pf
say({'stage':'new_scalar_original_Delta_built','terms':len(DE.n.to_dict()),'peakRssKiB':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss})
CO=Phi*NC-S*zeta*Pc
W=(Phi*(J-2*u*Q)-Pf)/2
units=[('eps',eps.n),('value_z',zm.n),('distinct_values',deltaValue.n),('pq',Q.n),('u',u.n),('u-1',(u-1).n),('bc',bc.n),('P02',P02.n),('lambda',lam.n),('physical_L',(1-eps*sm).n),('physical_S',S.n),('Phi_on_Delta0',Phi.n)]
returns=[]
for name,rr in [('Delta',DE),('compatibility',CO),('W',W)]:
 pp=rr.n;dd=rr.d;removed=oo;hist=[]
 for label,atom in units:
  while dd:
   gg=dd.gcd(atom)
   if gg.total_degree()==0:break
   qq=dd/gg;assert qq*gg==dd;dd=qq
  count=0
  while pp:
   gg=pp.gcd(atom)
   if gg.total_degree()==0:break
   qq=pp/gg;assert qq*gg==pp;pp=qq;removed*=gg;count+=1
  if count:hist.append([label,count])
 assert dd.total_degree()==0 and pp*removed==rr.n
 returns.append({'name':name,'poly':[[list(map(int,m)),str(a)] for m,a in pp.to_dict().items()]})
 say({'stage':'new_four_value_scalar_original_return','name':name,'degrees':list(map(int,pp.degrees())),'terms':len(pp.to_dict()),'paidRemoved':hist,'sha256':hashlib.sha256(str(sorted(pp.to_dict().items())).encode()).hexdigest(),'claimExcluded':False})
Path('/workspace/scratch/8542378f2b73/general_LS_four_value_scalar_returns.json').write_text(json.dumps(returns))
signal.alarm(0)
say({'stage':'complete_four_value_scalar_substitution','sourceSha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'peakRssKiB':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,'claimExcluded':False})

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
signal.alarm(120)
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
class E:
 def __init__(self,a=0,b=0):
  if isinstance(a,E):self.a=a.a;self.b=a.b;return
  self.a=R(a);self.b=R(b)
 def __bool__(self):return bool(self.a) or bool(self.b)
 def __add__(self,o):o=E(o);return E(self.a+o.a,self.b+o.b)
 __radd__=__add__
 def __neg__(self):return E(-self.a,-self.b)
 def __sub__(self,o):return self+-E(o)
 def __rsub__(self,o):return E(o)+-self
 def __mul__(self,o):o=E(o);return E(self.a*o.a+Delta*self.b*o.b,self.a*o.b+self.b*o.a)
 __rmul__=__mul__
 def __pow__(self,n):
  out=E(1)
  for _ in range(n):out=out*self
  return out
 def __eq__(self,o):o=E(o);return self.a==o.a and self.b==o.b
 def conj(self):return E(self.a,-self.b)
b=E(l/2,(u-l)/(2*Delta));c=b.conj();a=E(1-l)
p=E(1,1);q=p.conj();bc=(l*l-(u-l)**2/Delta)/4
ivdiff=E(0,-1/(2*Delta));ivbp=c*q*ivdiff*E(1/(bc*Q));ivcq=b*p*ivdiff*E(1/(bc*Q))
assert ivbp*b*p*(q-p)==1 and ivcq*c*q*(q-p)==1
V2=2*u-l*Q;T0=V2-2*u*u;P02=(2-3*u)*V2-Q*u+2*u**3
W1=E(T0/2+2*u*f);W2=E(u*T0+lam*P02+(V2+2*u*u)*f-bc*Q*t)
X=ivbp*(q*W1-W2);Y=ivcq*(W2-p*W1)
r=X-a*p-c*E(t);s=Y-a*q-b*E(t);A=E(2*f)-2*b*X-2*c*Y+E(2*bc*t)
rows=[[E(),E(),p,q],[E(),A,r,s],[p,r,E(),E(t)],[q,s,E(t),E()]]
one=[E(1),E(),E(1),E(1)]
def va(v,z):return [a+b for a,b in zip(v,z)]
def vs(a,v):return [a*b for b in v]
def vm(v,z):return [v[0]*z[0],v[0]*z[1]+v[1]*z[0],v[2]*z[2],v[3]*z[3]]
def tau(v):return a*v[0]+v[1]+b*v[2]+c*v[3]
def DK(v):return [tau(vm(row,v)) for row in rows]
d=DK(one);F2=tau(d);Kd=DK(d)
assert F2==E(2*f)
def mean(j):
 ee=2*tau(vm(rows[0],rows[1])) if j==1 else tau(vm(rows[j],rows[j]))
 return ee-2*Kd[j]-2*vm(d,d)[j]+2*F2*d[j]
assert not mean(0)
E1,EB,EC=mean(1),mean(2),mean(3)
assert not E1.b and EB.conj()==EC

def N4(v):
 return 2*tau(vm(d,vm(v,v)))-F2*tau(vm(v,v))-4*tau(v)*tau(vm(d,v))+2*F2*tau(v)**2+tau(vm(v,DK(v)))
v=rows[0];zzv=rows[1]
Nv=N4(va(v,zzv))-N4(v)-N4(zzv)
vc=va(v,vs(-tau(v),one));zc=va(zzv,vs(-tau(zzv),one))
Pj=3*tau(vm(vm(vc,vc),zc))
NH=Nv-E(lam*fmpq(4,3))*Pj
assert not NH.b



# The general prefix above precedes every S0 specialization in its source.
v0c=va(rows[0],vs(-tau(rows[0]),one))
assert tau(vm(vm(v0c,v0c),v0c))==E(P02)
assert N4(rows[0])==E(2*lam*P02)

T=Tnew;v0=sm/2;v1=1/(2*eps);zeta=v0-v1
hh=E(1+v0,v1);kk=hh.conj();ww=lam-1-T;VV=[E(1),E(ww),hh,kk]
assert b*(hh-1)+c*(kk-1)==T
assert tau(VV)==E(lam) and tau(vm(VV,VV))==E(2*lam*lam)
assert tau(vm(VV,vm(VV,VV)))==E(4*lam**3)
assert (hh-1)*(kk-1)==E(zm)
assert (hh-kk)**2==E(deltaValue)
assert q*(hh-1)-p*(kk-1)==E(0,(1-eps*sm)/eps)
D=l*A2-T*T;M=l*(2*u-l*Q)-u*u
assert E(D)==b*c*(hh-kk)**2 and M==4*bc*(1-Q)
S=sm+3-2*lam
J=2*u*(1-u)+l*Q;Phi=T0+4*u-4+Q;Pf=T0*(J-Q);Pt=bc*Q*Phi
G=lam*P02-(1-u)*T0;Pc=Q*P02*(l+T)-G*T0
PV=Pj-3*E(ww*P02)
assert not PV.b and PV.a*Q==3*(Pf*f+Pt*t+Pc)
NF=(3-4*lam)*Q-zm*J+S*(2*u*Q*v1+zeta*J)
NT=bc*Q*S*zeta
R1=u*(3-2*lam+v0+v1)-l*Q*v1
NC=G*(zm-S*zeta)+S*Q*T0*v1/2+Q*ww*R1
NV=N4(VV);assert not NV.b and NV.a*Q/2==NF*f+NT*t+NC
DE=Phi*NF-S*zeta*Pf;CO=Phi*NC-S*zeta*Pc
assert Phi*(NF*f+NT*t+NC)-S*zeta*(Pf*f+Pt*t+Pc)==DE*f+CO
W=(Phi*(J-2*u*Q)-Pf)/2
units=[('eps',eps.n),('value_z',zm.n),('distinct_values',deltaValue.n),('pq',Q.n),('u',u.n),('u-1',(u-1).n),('bc',bc.n),('P02',P02.n),('lambda',lam.n),('physical_L',(1-eps*sm).n),('physical_S',S.n),('Phi_on_Delta0',Phi.n)]
def paid_denominator(rr):
 dd=rr.d
 for name,atom in units:
  while dd:
   gg=dd.gcd(atom)
   if gg.total_degree()==0:break
   qq=dd/gg;assert qq*gg==dd;dd=qq
 assert dd.total_degree()==0,(str(rr.d),str(dd))
def stripped(rr):
 paid_denominator(rr);pp=rr.n;removed=oo;history=[]
 for name,atom in units:
  count=0
  while pp:
   gg=pp.gcd(atom)
   if gg.total_degree()==0:break
   qq=pp/gg;assert qq*gg==pp;pp=qq;removed*=gg;count+=1
  if count:history.append([name,count])
 assert pp*removed==rr.n
 return pp,history
returns=[]
for name,rr in [('original_Delta',DE),('original_compatibility',CO),('W',W),('Phi',Phi),('P02',P02),('Hankel_D',D)]:
 pp,hist=stripped(rr)
 returns.append({'name':name,'poly':[[list(map(int,m)),str(aa)] for m,aa in pp.to_dict().items()]})
 say({'stage':'new_four_parameter_exact_value_coordinates','name':name,'variables':['s','z','eps','lambda','f','t','unused0','unused1'],'degrees':list(map(int,pp.degrees())),'terms':len(pp.to_dict()),'paidRemoved':hist,'sha256':hashlib.sha256(str(sorted(pp.to_dict().items())).encode()).hexdigest(),'claimExcluded':False})
Path('/workspace/scratch/8542378f2b73/general_LS_four_value_parameter_returns.json').write_text(json.dumps(returns))
signal.alarm(0)
say({'stage':'complete_new_four_value_parameter_original_identities','allThreeMomentsIdenticallyReturned':True,'originalTwoLinesMultipliedBack':True,'sourceSha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'peakRssKiB':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,'claimExcluded':False})

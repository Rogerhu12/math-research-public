#!/usr/bin/env python3
"""R150 S=Af=0, L!=0, (I,H)!=0: exact two-parameter original equations.
Keep both roots d^2=s^2-4z. B/C equations become their even/odd parts.
Default project: generate all original equations and both P1 projections.
--stage eliminate also computes exact QQ lambda resultants.
Every discarded coefficient factor is an explicitly paid chart unit.
"""
import argparse,hashlib,itertools,json,os,resource,signal,time
from pathlib import Path
from flint import fmpq,fmpq_mpoly_ctx
started=time.perf_counter()
ap=argparse.ArgumentParser()
ap.add_argument('--stage',choices=['graph','generate','project','eliminate'],default=os.environ.get('ISP_S0_STAGE','project'))
ap.add_argument('--seconds',type=int,default=600)
args=ap.parse_args()
def say(o):
 o['elapsedSeconds']=round(time.perf_counter()-started,6)
 print(json.dumps(o,sort_keys=True),flush=True)
def alarm_handler(signum,frame):
 say({'status':'timeout_unknown','stageRequested':args.stage,'claimExcluded':False})
 raise SystemExit(124)
signal.signal(signal.SIGALRM,alarm_handler);signal.alarm(args.seconds)
ctx=fmpq_mpoly_ctx.get(('lam','z'),'lex')
lp,zp=ctx.gens();zz=ctx.constant(0);oo=ctx.constant(1)
def poly(v):return v if hasattr(v,'to_dict') else ctx.constant(v)
class R:
 def __init__(self,n=0,d=None,reduce=True):
  if isinstance(n,R):self.n=n.n;self.d=n.d;return
  n=poly(n);d=oo if d is None else poly(d)
  assert d
  if not n:self.n=zz;self.d=oo;return
  if reduce:
   g=n.gcd(d);n=n/g;d=d/g
  self.n=n;self.d=d
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
 def __truediv__(self,o):
  o=R(o);assert o
  return self*R(o.d,o.n,False)
 def __rtruediv__(self,o):return R(o)/self
 def __pow__(self,n):
  if n<0:assert self;return R(self.d**(-n),self.n**(-n),False)
  return R(self.n**n,self.d**n,False)
 def __eq__(self,o):
  o=R(o);return self.n*o.d==o.n*self.d
lam=R(lp);z=R(zp)
sp=2*lp-3;Ap=2*lp*lp-2*lp+1;Cp=-4*lp*lp+5*lp-2;Rp=3-4*lp;jp=2*lp-1
Dp=sp*Cp-Ap*zp
I2=2*(4*lp-1)*Cp*Dp+zp*(2*Cp*(1-lp)*Rp-2*(4*lp*lp-7*lp+2)*Dp)+zp*zp*(-2*lp*Cp+sp*jp*Rp)
H3=Dp*((4*lp*(1-lp)+2*lp*zp)*zp-4*jp*Dp-2*sp*Cp)-2*(lp-1)*Cp*zp*zp+2*Cp*Cp*zp-2*jp*Rp*zp**3+4*jp*Dp*zp*zp
Denp=2*zp*I2+sp*H3
s=R(sp);A=R(Ap);C=R(Cp);RR=R(Rp);j=R(jp)
l=R(Dp,zp*zp);T=R(Cp,zp);w=lam-1-T
I=R(I2,zp*zp);H=R(H3,zp**3)
Ku=2*(1-lam)*RR+4*z*j*l-2*lam*z
Kv=j*(RR-2*z*l)
assert I==T*Ku-2*w*l*z+s*Kv
assert H==-l*Ku-2*w*T+2*w*s*l-2*Kv
Delta=s*s-4*z;theta=R(H3,Denp);B=2*T-l*s
u=l+theta*B;Q=1-theta*theta*Delta
bc=(l*l-B*B/Delta)/4
V2=2*u-l*Q;P02=(2-3*u)*V2-Q*u+2*u**3;P0=P02/2
Af=RR-z*(l+2*u*(1-u)/Q)
# L!=0 is exactly I2!=0 on this graph. The separate L=0 task retains it.
# u-1 is paid by the registered entire p+q=2,u=1 exclusion.
units=[lp,zp,Delta.n,I2,H3,Denp,Q.n,bc.n,P0.n,u.n,(u-1).n]
def strip_units(p):
 p=poly(p)
 if not p:return p
 for atom in units:
  assert atom
  while True:
   g=p.gcd(atom)
   if int(g.total_degree())==0:break
   p=p/g
 return p
def paid(r):
 assert int(strip_units(R(r).d).total_degree())==0
def deg(p):
 dd=p.to_dict()
 return [max((int(mm[j]) for mm in dd),default=-1) for j in range(2)]
def profile(p):return {'degrees':deg(p),'terms':len(p.to_dict())}
F=strip_units(Af.n);assert F and int(F.total_degree())>0
for v in [l,T,w,I,H,Delta,theta,B,u,Q,bc,V2,P0,Af]:paid(v)
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
 def __mul__(self,o):
  o=E(o);return E(self.a*o.a+Delta*self.b*o.b,self.a*o.b+self.b*o.a)
 __rmul__=__mul__
 def __pow__(self,n):
  assert n>=0
  out=E(1);v=self
  while n:
   if n&1:out=out*v
   v=v*v;n//=2
  return out
 def __eq__(self,o):o=E(o);return self.a==o.a and self.b==o.b
 def conj(self):return E(self.a,-self.b)
b=E(l/2,B/(2*Delta));c=b.conj();a=E(1-l)
p=E(1,theta);q=p.conj()
h=E(1+s/2,R(fmpq(1,2)));k=h.conj()
assert b*c==E(bc) and p*q==E(Q) and b*p+c*q==E(u)
assert b*p*p+c*q*q==E(V2)
assert (b*p**3+c*q**3-E(3*u*V2)+E(2*u**3))==E(P02)
assert a+E(w)+b*h+c*k==E(lam)
assert a+E(2*w)+b*h*h+c*k*k==E(2*lam*lam)
assert a+E(3*w)+b*h**3+c*k**3==E(4*lam**3)
assert h+k+1==E(2*lam)
ivdiff=E(0,-1/(2*theta*Delta))
ivbp=c*q*ivdiff*E(1/(bc*Q))
ivcq=b*p*ivdiff*E(1/(bc*Q))
assert ivbp*b*p*(q-p)==1 and ivcq*c*q*(q-p)==1
for v in [b,c,p,q,h,k,ivdiff,ivbp,ivcq]:
 paid(v.a);paid(v.b)
sha=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
say({'stage':'exact_two_parameter_graph_verified','sourceSha256':sha,'parameterCurve':profile(F),'curveInputSha256':hashlib.sha256(str(sorted(F.to_dict().items())).encode()).hexdigest(),'retainedQuadraticRoots':2,'scope':'S=Af=0,L!=0,(I,H)!=0','claimExcluded':False})
def finish(status,extra=None):
 signal.alarm(0)
 out={'schema':'r150-unit211-S0-nonsimultaneous-native-two-parameter-v1','status':status,'sourceSha256':sha,'claimExcluded':False,'claimS0LayerEmpty':False,'claimLambdaLayerEmpty':False,'ordinaryISPClaim':False,'peakRssKiB':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}
 if extra:out.update(extra)
 say(out)
if args.stage=='graph':
 finish('exact_two_parameter_graph_only');raise SystemExit(0)
class P:
 def __init__(self,co=None):self.co={ij:E(v) for ij,v in (co or {}).items() if E(v)}
 def __bool__(self):return bool(self.co)
 def __add__(self,o):
  if not isinstance(o,P):o=cp(o)
  dd=dict(self.co)
  for ij,v in o.co.items():dd[ij]=dd.get(ij,E())+v
  return P(dd)
 __radd__=__add__
 def __neg__(self):return P({ij:-v for ij,v in self.co.items()})
 def __sub__(self,o):return self+-o
 def __rsub__(self,o):return cp(o)+-self
 def __mul__(self,o):
  if not isinstance(o,P):return scale(E(o),self)
  dd={}
  for ij,v in self.co.items():
   for kl,vv in o.co.items():
    key=(ij[0]+kl[0],ij[1]+kl[1]);dd[key]=dd.get(key,E())+v*vv
  return P(dd)
 __rmul__=__mul__
 def __pow__(self,n):
  out=cp(1)
  for _ in range(n):out=out*self
  return out
 def conj(self):return P({ij:v.conj() for ij,v in self.co.items()})
def cp(v):return P({(0,0):E(v)})
def scale(v,pp):return P({ij:E(v)*vv for ij,vv in pp.co.items()})
fp=P({(1,0):E(1)});tp=P({(0,1):E(1)});zero=P()
one=[cp(1),zero,cp(1),cp(1)]
def va(v,z0):return [x+y for x,y in zip(v,z0)]
def vs(v0,v):return [v0*x for x in v]
def vm(v,z0):return [v[0]*z0[0],v[0]*z0[1]+v[1]*z0[0],v[2]*z0[2],v[3]*z0[3]]
def tau(v):return scale(a,v[0])+v[1]+scale(b,v[2])+scale(c,v[3])
T0=V2-2*u*u
W1=cp(T0/2)+scale(E(2*u),fp)
W2=cp(u*T0+lam*P02)+scale(E(V2+2*u*u),fp)-scale(E(bc*Q),tp)
XX=scale(ivbp,scale(q,W1)-W2);YY=scale(ivcq,W2-scale(p,W1))
r=XX-cp(a*p)-scale(c,tp);ss=YY-cp(a*q)-scale(b,tp)
Arow=scale(E(2),fp)-scale(2*b,XX)-scale(2*c,YY)+scale(E(2*bc),tp)
assert not (r.conj()-ss) and not (Arow.conj()-Arow)
rows=[[zero,zero,cp(p),cp(q)],[zero,Arow,r,ss],[cp(p),r,zero,tp],[cp(q),ss,tp,zero]]
def DK(v):return [tau(vm(row,v)) for row in rows]
d=DK(one);F2=tau(d);DKd=DK(d);dd=vm(d,d)
assert not (F2-scale(E(2),fp))
def P2(v):
 cen=va(v,vs(-tau(v),one))
 return tau(vm(vm(cen,cen),cen))
def N4(v):
 return scale(E(2),tau(vm(d,vm(v,v))))-F2*tau(vm(v,v))-scale(E(4),tau(v)*tau(vm(d,v)))+scale(E(2),F2*tau(v)**2)+tau(vm(v,DK(v)))
def Pjet2(v,z0):
 v0=va(v,vs(-tau(v),one));z1=va(z0,vs(-tau(z0),one))
 return scale(E(3),tau(vm(vm(v0,v0),z1)))
def Njet4(v,z0):return N4(va(v,z0))-N4(v)-N4(z0)
def mean(jj):
 ev=scale(E(2),tau(vm(rows[0],rows[1]))) if jj==1 else tau(vm(rows[jj],rows[jj]))
 return ev-scale(E(2),DKd[jj])-scale(E(2),dd[jj])+scale(E(2),F2*d[jj])
assert not mean(0) and not (P2(rows[0])-cp(P02)) and not (N4(rows[0])-cp(2*lam*P02))
VV=[cp(1),cp(w),cp(h),cp(k)]
assert not P2(VV)
NV=N4(VV)
assert (NV.co.get((1,0),E())==E(2*Af)) and not NV.co.get((0,1),E())
for vv in NV.co.values():
 assert not vv.b
 assert not vv.a.n or int(vv.a.n.gcd(F).total_degree())==int(F.total_degree())
 paid(vv.a)
raw=[mean(1),mean(2),Pjet2(rows[0],rows[1])-cp(3*w*P02),P2(rows[2])-cp(h**3*E(P02)),Njet4(rows[0],rows[1])-cp(4*lam*w*P02),N4(rows[2])-cp(h*h*E(2*lam*P02))]
assert not (mean(3)-raw[1].conj())
Lf=T0*(l-1+2*u*(1-u)/Q);Lt=bc*(T0+4*u-4+Q)
Lc=(1-u)*T0*T0/Q+P02*(l+T-lam*T0/Q)
assert not (raw[2]-scale(E(3),scale(E(Lf),fp)+scale(E(Lt),tp)+cp(Lc)))
def parts(pp,part):
 dd={}
 for ij,v in pp.co.items():
  rr=v.a if part==0 else v.b
  if rr:dd[ij]=rr
 return dd
for jj in [0,2,4]:assert not parts(raw[jj],1)
names=['E1','EBe','EBo','P1','PBe','PBo','N1','NBe','NBo']
basepolys=[parts(raw[0],0),parts(raw[1],0),parts(raw[1],1),parts(raw[2],0),parts(raw[3],0),parts(raw[3],1),parts(raw[4],0),parts(raw[5],0),parts(raw[5],1)]
def strip_common(vv):
 vv=list(vv)
 for atom in units:
  while any(bool(v) for v in vv):
   gg=atom
   for v in vv:gg=gg.gcd(v)
   if int(gg.total_degree())==0:break
   vv=[v/gg for v in vv]
 return vv
cleared=[];hh=hashlib.sha256()
for name,pp in zip(names,basepolys):
 den=oo
 for vv in pp.values():
  paid(vv);den=den*(vv.d/den.gcd(vv.d))
 keys=sorted(pp);nums=strip_common([pp[ij].n*(den/pp[ij].d) for ij in keys])
 po={ij:v for ij,v in zip(keys,nums) if v};cleared.append(po)
 for ij,v in sorted(po.items()):hh.update((name+str(ij)+str(sorted(v.to_dict().items()))+'\n').encode())
 say({'stage':'original_condition_generated','name':name,'ftDegree':max((sum(ij) for ij in po),default=-1),'coefficientProfiles':[profile(v) for ij,v in sorted(po.items())],'claimExcluded':False})
inputsha=hh.hexdigest()
say({'stage':'all_original_nine_equivalent_conditions_generated','sourceSha256':sha,'inputSha256':inputsha,'parameterCurve':profile(F),'claimExcluded':False})
if args.stage=='generate':
 finish('original_nine_and_parameter_curve_generated',{'inputSha256':inputsha});raise SystemExit(0)
def utr(vv):
 vv=list(vv)
 while vv and not vv[-1]:vv.pop()
 return vv
def ua(vv,ww):
 out=[zz]*max(len(vv),len(ww))
 for ii in range(len(out)):out[ii]=(vv[ii] if ii<len(vv) else zz)+(ww[ii] if ii<len(ww) else zz)
 return utr(out)
def um(vv,ww):
 if not vv or not ww:return []
 out=[zz]*(len(vv)+len(ww)-1)
 for ii,v in enumerate(vv):
  for jj,vv0 in enumerate(ww):out[ii+jj]=out[ii+jj]+v*vv0
 return utr(out)
def up(vv,n):
 out=[oo]
 for _ in range(n):out=um(out,vv)
 return out
def project(pp,o):
 pp={((ij[0],ij[1]) if o==0 else (ij[1],ij[0])):v for ij,v in pp.items()}
 line={((ij[0],ij[1]) if o==0 else (ij[1],ij[0])):v for ij,v in cleared[3].items()}
 aa=line.get((1,0),zz);bb=line.get((0,1),zz);cc=line.get((0,0),zz)
 dd=max((ij[0] for ij in pp),default=0);out=[]
 for (ii,jj),v in pp.items():
  term=[v*aa**(dd-ii)*vv for vv in up([-cc,-bb],ii)]
  out=ua(out,[zz]*jj+term)
 return utr(strip_common(out))
def det(mat):
 n=len(mat)
 if n==0:return oo
 if n==1:return mat[0][0]
 out=zz
 for jj in range(n):
  if mat[0][jj]:out=out+((-1)**jj)*mat[0][jj]*det([row[:jj]+row[jj+1:] for row in mat[1:]])
 return out
def resultant(vv,ww):
 vv=utr(vv);ww=utr(ww)
 if not vv or not ww:return zz
 n=len(vv)-1;m=len(ww)-1
 if n==0:return vv[0]**m if m else vv[0]
 if m==0:return ww[0]**n
 mat=[]
 for ii in range(m):mat.append([zz]*ii+vv[::-1]+[zz]*(m-1-ii))
 for ii in range(n):mat.append([zz]*ii+ww[::-1]+[zz]*(n-1-ii))
 return strip_units(det(mat))
projected=[[project(pp,o) for pp in cleared] for o in [0,1]]
pairs=[(0,1),(0,2),(1,2),(0,6),(1,6),(2,6)]
lambda_gcd=zz;history=[]
for ii,jj in pairs:
 for orientation in [0,1]:
  rr=resultant(projected[orientation][ii],projected[orientation][jj])
  entry={'orientation':orientation,'pair':[names[ii],names[jj]],'resultant':profile(rr),'commonCurve':profile(F.gcd(rr)),'resultantSha256':hashlib.sha256(str(sorted(rr.to_dict().items())).encode()).hexdigest()}
  say({'stage':'exact_original_P1_mean_projection','projection':entry,'claimExcluded':False})
  if args.stage=='eliminate' and rr:
   ee=F.resultant(rr,'z')
   assert all(int(m[1])==0 for m in ee.to_dict())
   lambda_gcd=lambda_gcd.gcd(ee) if lambda_gcd else ee
   entry['lambdaResultant']=profile(ee);entry['lambdaGcd']=profile(lambda_gcd)
   say({'stage':'exact_QQ_parameter_projection','projection':entry,'claimExcluded':False})
  history.append(entry)
  if args.stage=='eliminate' and lambda_gcd and int(lambda_gcd.total_degree())==0:
   finish('exact_two_parameter_original_fiber_excluded',{'inputSha256':inputsha,'projectionHistory':history,'claimExcluded':True,'claimS0LayerEmpty':False});raise SystemExit(0)
out={'inputSha256':inputsha,'projectionHistory':history}
if args.stage=='eliminate':
 out['lambdaGcd']=profile(lambda_gcd)
 if lambda_gcd and int(lambda_gcd.total_degree())<=100:out['remainingLambdaPolynomial']=str(lambda_gcd)
finish('exact_original_projections_generated_candidates_unresolved',out)

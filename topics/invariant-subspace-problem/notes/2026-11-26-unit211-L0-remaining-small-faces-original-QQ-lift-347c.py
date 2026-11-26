#!/usr/bin/env python3
"""Original L0 with b+c!=0, after the complete zero-weight-sum theorem.
Use p+q=2 and the entire kappa^2=1-pq algebra in three rational parameters.
All original nine conditions and all P1 leading-zero fibers are retained.
Use two new characteristic-zero inputs: the original G curve and the entire
P1 double-zero face. Only an actual original-unit lift proves exclusion.
"""
import hashlib,json,resource,signal,time,os,shutil,subprocess,tempfile,math
from pathlib import Path
from flint import fmpq,fmpq_mpoly_ctx,fmpq_poly
started=time.perf_counter()
def say(stage,**kw):
 print(json.dumps(dict(stage=stage,elapsedSeconds=round(time.perf_counter()-started,6),**kw),sort_keys=True),flush=True)
def alarm(signum,frame):
 say("timeout_unknown",claimExcluded=False);raise SystemExit(124)
signal.signal(signal.SIGALRM,alarm);signal.alarm(1100)
ctx=fmpq_mpoly_ctx.get(("rho","lam","w"),"lex")
rp,lp,wp=ctx.gens();zz=ctx.constant(0);oo=ctx.constant(1)
def poly(v):return v if hasattr(v,"to_dict") else ctx.constant(v)
class R:
 def __init__(self,n=0,d=None,reduce=True):
  if isinstance(n,R):self.n=n.n;self.d=n.d;return
  n=poly(n);d=oo if d is None else poly(d)
  assert d
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
 def __truediv__(self,o):
  o=R(o);assert o
  return self*R(o.d,o.n,False)
 def __rtruediv__(self,o):return R(o)/self
 def __pow__(self,n):
  if n<0:assert self;return R(self.d**(-n),self.n**(-n),False)
  return R(self.n**n,self.d**n,False)
 def __eq__(self,o):
  o=R(o);return self.n*o.d==o.n*self.d

rho=R(rp);lam=R(lp);w=R(wp)
A=2*lam*lam-2*lam+1;BB=4*lam**3-6*lam*lam+3*lam-1
RR=lam-1-w;Cmom=RR*BB-A*A
u=RR/rho;V2=A/(rho*rho)
Q=(2*A*rho-BB)/(rho*rho*RR);Delta=1-Q
l=(2*u-V2)/Q;T=RR
bc=(l*l*Delta-(u-l)**2)/(4*Delta)
P02=(2-3*u)*V2-Q*u+2*u**3;P0=P02/2
T0=V2-2*u*u
fsol=-(u*(w/2-w*w)+rho*T0/4+lam*rho*rho*P0)/(w*(w-1))
assert Cmom==4*rho**4*bc*Q*Delta
assert P02==(BB-3*RR*A+2*RR**3)/(rho**3)
# l!=0 is paid by the complete L0,b+c=0 theorem, not by a generic assumption.
# A may be zero on this complement and is never inverted.
units=[rp,lp,wp,wp-1,RR.n,Cmom.n,Delta.n,Q.n,P0.n,(u-1).n,l.n]
def strip_units(po):
 po=poly(po)
 for atom in units:
  assert atom
  while po:
   gg=po.gcd(atom)
   if int(gg.total_degree())==0:break
   po=po/gg
 return po
denominators=set()
def paid(rr):
 dd=R(rr).d;key=str(dd)
 if key not in denominators:
  assert int(strip_units(dd).total_degree())==0
  denominators.add(key)
def profile(po):
 return dict(degrees=list(map(int,po.degrees())) if po else [-1,-1],terms=len(po.to_dict()),sha256=hashlib.sha256(str(po).encode()).hexdigest())
for val in [A,BB,RR,rho,u,V2,Q,Delta,bc,P02,fsol]:paid(val)
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

b=E(l/2,(u-l)/(2*Delta));c=b.conj();a=E(1-l)
p=E(1,1);q=p.conj()
h=E(1+rho,rho);k=h.conj()
assert b+c==E(l) and b*c==E(bc) and p*q==E(Q)
assert b*p+c*q==E(u) and b*p*p+c*q*q==E(V2)
assert b*p**3+c*q**3==E(2*V2-Q*u)
assert a+E(w)+b*h+c*k==E(lam)
assert a+E(2*w)+b*h*h+c*k*k==E(2*lam*lam)
assert a+E(3*w)+b*h**3+c*k**3==E(4*lam**3)
assert q*(h-1)-p*(k-1)==0
ivdiff=E(0,-1/(2*Delta))
ivbp=c*q*ivdiff*E(1/(bc*Q));ivcq=b*p*ivdiff*E(1/(bc*Q))
assert ivbp*b*p*(q-p)==1 and ivcq*c*q*(q-p)==1
for val in [b,c,p,q,h,k,ivdiff,ivbp,ivcq]:paid(val.a);paid(val.b)
sha=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
say("complete_original_L0_symmetric_nonzero_l_two_parameter_graph",sourceSha256=sha,retainedQuadraticRoots=2,paid_l_reason="complete original L0 zero-weight-sum theorem; A is retained including zero",claimExcluded=False)
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
fp=cp(fsol);tp=P({(0,1):E(1)});zero=P()
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
assert not P2(VV) and not N4(VV)
raw=[mean(1),mean(2),Pjet2(rows[0],rows[1])-cp(3*w*P02),P2(rows[2])-cp(h**3*E(P02)),Njet4(rows[0],rows[1])-cp(4*lam*w*P02),N4(rows[2])-cp(h*h*E(2*lam*P02))]
assert not (mean(3)-raw[1].conj())
Lf=T0*(l-1+2*u*(1-u)/Q);Lt=bc*(T0+4*u-4+Q)
Lc=(1-u)*T0*T0/Q+P02*(l+T-lam*T0/Q)
assert not (raw[2]-scale(E(3),scale(E(Lf),fp)+scale(E(Lt),tp)+cp(Lc)))
def parts(pp,part):
 dd={}
 for ij,v in pp.co.items():
  assert ij[0]==0
  rr=v.a if part==0 else v.b
  if rr:dd[ij[1]]=rr
 return dd
for jj in [0,2,4]:assert not parts(raw[jj],1)
names=["E1","EBe","EBo","P1","PBe","PBo","N1","NBe","NBo"]
base=[parts(raw[0],0),parts(raw[1],0),parts(raw[1],1),parts(raw[2],0),parts(raw[3],0),parts(raw[3],1),parts(raw[4],0),parts(raw[5],0),parts(raw[5],1)]
cleared=[]
for name,pp in zip(names,base):
 den=oo
 for vv in pp.values():
  paid(vv);den=den*(vv.d/den.gcd(vv.d))
 nums=[pp[j].n*(den/pp[j].d) if j in pp else zz for j in range(max(pp,default=-1)+1)]
 for atom in units:
  while any(nums):
   gg=atom
   for nn in nums:gg=gg.gcd(nn)
   if int(gg.total_degree())==0:break
   nums=[nn/gg for nn in nums]
 if any(nums):
  first=next(nn for nn in nums if nn)
  scale0=next(iter(first.to_dict().values()))
  nums=[nn/scale0 for nn in nums]
 while nums and not nums[-1]:nums.pop()
 cleared.append(nums)
 say("original_L0_symmetric_nonzero_l_condition",name=name,tDegree=len(nums)-1,coefficientProfiles=[profile(nn) for nn in nums],claimExcluded=False)
assert len(cleared[3])<=2
def norm(po):
 po=strip_units(po)
 return po/next(iter(po.to_dict().values())) if po else po
def det(mm):
 if not mm:return oo
 if len(mm)==1:return mm[0][0]
 return sum(((-1)**j*mm[0][j]*det([row[:j]+row[j+1:] for row in mm[1:]]) for j in range(len(mm)) if mm[0][j]),zz)
def resultant(p0,q0):
 if not p0 or not q0:return zz
 n=len(p0)-1;m=len(q0)-1
 if n==0:return p0[0]**m if m else p0[0]
 if m==0:return q0[0]**n
 matrix=[[zz]*i+p0[::-1]+[zz]*(m-1-i) for i in range(m)]
 matrix.extend([[zz]*i+q0[::-1]+[zz]*(n-1-i) for i in range(n)])
 return det(matrix)
alpha=cleared[3][1] if len(cleared[3])==2 else zz
beta=cleared[3][0] if cleared[3] else zz
eqs=[]
if not alpha and beta:eqs.append(("P1_constant",norm(beta)))
for name,co in zip(names,cleared):
 if not co or name=="P1":continue
 degree=len(co)-1
 value=norm(sum((v*(-beta)**j*alpha**(degree-j) for j,v in enumerate(co)),zz))
 if value:eqs.append(("P1_"+name,value))
for i,j in [(0,1),(0,2),(1,2),(0,6),(1,6),(2,6)]:
 value=norm(resultant(cleared[i],cleared[j]))
 if value:eqs.append((names[i]+"_"+names[j],value))
for name,po in eqs:say("original_L0_symmetric_nonzero_l_two_parameter_projection",name=name,profile=profile(po),allP1ZeroLeadingFibersRetained=True,claimExcluded=False)
assert eqs
eqs.sort(key=lambda item:(int(item[1].degrees()[1]),int(item[1].total_degree()),len(item[1].to_dict())))



# Change the input to the remaining small original curve / zero-coefficient face.
# These are necessary original ideals. A closure is accepted only from a true
# characteristic-zero transformation vector remultiplied to one.
mode=os.environ.get("ISP_U_CONDITION","curveG")
assert mode in ("curveG","P1double")
lookup=dict(eqs)
curveG=384*lp**7*wp**3 + 576*lp**7*wp**2 + 192*lp**7*wp - 128*lp**6*wp**4 - 1472*lp**6*wp**3 - 1904*lp**6*wp**2 - 464*lp**6*wp + 32*lp**6 + 352*lp**5*wp**4 + 2304*lp**5*wp**3 + 2592*lp**5*wp**2 + 368*lp**5*wp - 96*lp**5 - 400*lp**4*wp**4 - 1936*lp**4*wp**3 - 1916*lp**4*wp**2 - 20*lp**4*wp + 120*lp**4 + 248*lp**3*wp**4 + 952*lp**3*wp**3 + 828*lp**3*wp**2 - 156*lp**3*wp - 84*lp**3 - 88*lp**2*wp**4 - 264*lp**2*wp**3 - 194*lp**2*wp**2 + 120*lp**2*wp + 36*lp**2 + 16*lp*wp**4 + 28*lp*wp**3 + 10*lp*wp**2 - 42*lp*wp - 9*lp + 4*wp**3 + 4*wp**2 + 6*wp + 1
assert hashlib.sha256(str(curveG).encode()).hexdigest()=="9422bed84800d7ed6a6dcf1910e6c1baebf5c50b8c2c37324361824d269f8c84"
curveW=4*lp*wp+2*lp-2*wp*wp-4*wp-1
if mode=="curveG":
 selected=[("original_G_curve",curveG)]+eqs
else:
 # Alpha and beta are the original cleared coefficients, not their gcd.
 # Their common zero face is retained in its entirety.
 selected=[("P1_t_coefficient_zero",alpha),("P1_constant_coefficient_zero",beta)]
 selected += [(label,po) for label,po in eqs if not label.startswith("P1_")]
# Physical units were all checked in the original atlas above. The complete W
# curve is now independently excluded, so its intersection may be localized.
product=curveW
for atom in units:product*=atom
assert product
labels=[];expressions=[]
for label,po in selected:
 if not po:continue
 po=po/po.coefficient(0)
 labels.append(label);expressions.append(str(po))
 say("original_small_face_generator",mode=mode,label=label,profile=profile(po),claimExcluded=False)
labels.append("only_original_units_and_separately_excluded_W")
expressions.append("iv*("+str(product)+")-1")
say("original_small_face_input_complete",mode=mode,generators=len(expressions),physicalVariables=["rho","lam","w"],curveWAlreadyClosed=True,allZeroLeadingFibersRetained=True,claimExcluded=False)
singular=shutil.which("Singular");assert singular
ver=subprocess.run([singular,"--version"],capture_output=True,text=True,timeout=15)
say("singular_version",returncode=ver.returncode,text=(ver.stdout+ver.stderr).splitlines()[0])
script="ring isp=0,(iv,rho,w,lam),dp;\noption(redSB);\n"
script+='ideal smoke=lam,lam-1;matrix smokeU;matrix smokeC=lift(smoke,ideal(1),smokeU,"slimgb");matrix smokeP=matrix(smoke)*smokeC;\n'
script+='if(nrows(smokeP)!=1 || ncols(smokeP)!=1 || smokeP[1,1]!=1){print("ISP_L0_SMALL_SMOKE_FAILED");quit;}\nprint("ISP_L0_SMALL_SMOKE_VERIFIED");\n'
script+="ideal I="+",\n".join(expressions)+";\n"
script+='print("ISP_BEGIN_L0_SMALL_ORIGINAL_TRUE_QQ_LIFT");\nmatrix unitU;matrix certificate=lift(I,ideal(1),unitU,"slimgb");\n'
script+='print("ISP_BEGIN_L0_SMALL_ORIGINAL_REMULTIPLICATION");\nmatrix product=matrix(I)*certificate;\n'
script+='if(nrows(product)==1 && ncols(product)==1 && product[1,1]==1){print("ISP_L0_SMALL_ORIGINAL_UNIT_VERIFIED");print(nrows(certificate));int ii;for(ii=1;ii<=nrows(certificate);ii++){print("ISP_CERT_PART");print(ii);print(deg(certificate[ii,1]));print(size(certificate[ii,1]));}}else{print("ISP_L0_SMALL_ORIGINAL_UNIT_NOT_OBTAINED");}\nquit;\n'
say("singular_L0_small_original_input",mode=mode,bytes=len(script.encode()),sha256=hashlib.sha256(script.encode()).hexdigest(),generators=len(expressions),field="QQ",wallLimitSeconds=900,addressSpaceLimitBytes=4294967296,claimExcluded=False)
def child_limits():
 resource.setrlimit(resource.RLIMIT_AS,(4294967296,4294967296))
with tempfile.TemporaryDirectory(prefix="isp-L0-small-original-") as td:
 path=Path(td)/"input.sing";path.write_text(script)
 try:
  run=subprocess.run([singular,"-q",str(path)],capture_output=True,text=True,timeout=900,preexec_fn=child_limits)
  output=run.stdout+run.stderr;lines=set(run.stdout.splitlines())
  markers=("ISP_L0_SMALL_SMOKE_VERIFIED","ISP_L0_SMALL_ORIGINAL_UNIT_VERIFIED")
  verified=run.returncode==0 and all(s0 in lines for s0 in markers) and not any(s0.lstrip().startswith("?") for s0 in output.splitlines())
  say("singular_L0_small_original_output",mode=mode,returncode=run.returncode,identityVerified=verified,text=output[:30000],stdoutSha256=hashlib.sha256(output.encode()).hexdigest(),claimExcluded=verified)
  if not verified:raise SystemExit(2)
 except subprocess.TimeoutExpired as ex:
  output=(ex.stdout or b"")+(ex.stderr or b"")
  if isinstance(output,bytes):output=output.decode(errors="replace")
  say("L0_small_original_bounded_timeout",mode=mode,outcome="unresolved",limitSeconds=900,text=output[:30000],stdoutSha256=hashlib.sha256(output.encode()).hexdigest(),claimExcluded=False)
  raise SystemExit(124)
signal.alarm(0)
say("complete_L0_small_original_unit",mode=mode,sourceSha256=sha,identity="matrix(original_generators)*certificate=[1] over QQ",claimExcluded=True,claimWholeL0Excluded=False,ordinaryISPClaim=False,peakRssKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)

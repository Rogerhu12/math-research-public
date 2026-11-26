#!/usr/bin/env python3
"""R150 S0, original P1 t coefficient zero: exact parameter projection.
Return the original theta-leading-coefficient zero branch after the paid J=0 branch.
No original leading fiber is divided out; retain every exact lambda/z candidate.
"""
import hashlib,json,resource,signal,time
from pathlib import Path
from flint import fmpq,fmpq_poly,fmpq_mpoly_ctx
started=time.perf_counter()
def say(o):
 o['elapsedSeconds']=round(time.perf_counter()-started,6)
 print(json.dumps(o,sort_keys=True),flush=True)
def alarm_handler(signum,frame):
 say({'status':'timeout_unknown','claimExcluded':False})
 raise SystemExit(124)
signal.signal(signal.SIGALRM,alarm_handler);signal.alarm(600)
ctx=fmpq_mpoly_ctx.get(('lam','z','theta'),'lex')
la,z,th=ctx.gens();zero=ctx.constant(0)
s=2*la-3;A=2*la*la-2*la+1;C=-4*la*la+5*la-2;R=3-4*la
D=s*C-A*z;Delta=s*s-4*z;B=2*C*z-D*s
U=D+th*B;V=U-z*z;Q=1-th*th*Delta
# u=U/z^2, l=D/z^2, T=C/z, w=W/z.
W=(la-1)*z-C;E=D+C*z
# G=z^4*Lt/(bc). No division by its theta leading coefficient.
G=z*z*(z*z-D)*Q-2*V*(V-z*z)
Traw=z*z*(2*U-D*Q)-2*U*U
Tn=-4*V-z*z*Q
assert Traw-z*z*Tn==G
Praw=(2*z*z-3*U)*(2*U-D*Q)*z*z-Q*U*z**4+2*U**3
assert Praw-2*D*Q*V*z*z==-U*G
assert z*z*(D-z*z)*Q+2*U*(z*z-U)==-G-4*V*V
# Cross=b*p*(k-1)+c*q*(h-1)=Y/(2z^2).
Y=2*(D*s-C*z)+th*(B*s-D*Delta)
# On G=0 this is z^7 times Q/v times the compatibility of
# the original P1 line with the original N(V) line. v=u-1 is already paid.
K=z**3*(R-z)*(-Tn*Tn+2*D*E*Q*Q-2*la*D*Q*Tn)+8*D*E*Q*V*V-2*V*Tn*W*Y
def degree(p,j):return max((int(m[j]) for m in p.to_dict()),default=-1)
def profile(p):return {'degrees':[degree(p,j) for j in range(3)],'terms':len(p.to_dict())}
def co(p,j):
 return ctx.from_dict({(int(m[0]),int(m[1]),0):v for m,v in p.to_dict().items() if int(m[2])==j})
def serialized(p):
 t=str(p)
 return {'profile':profile(p),'polynomial':t if len(t)<=8000 else None,'sha256':hashlib.sha256(str(sorted(p.to_dict().items())).encode()).hexdigest()}
def factor_report(p):
 content,ff=p.factor()
 return {'content':str(content),'factors':[{'exponent':int(e),**serialized(f)} for f,e in ff]}

g0=co(G,0);g1=co(G,1);g2=co(G,2)
assert g0==-(D-z*z)*(2*D-3*z*z)
assert g1==-2*B*(2*D-3*z*z)
assert g2==z*z*(D-z*z)*Delta-2*B*B
J=4*z**3+(12*la*la-4*la-1)*z*z+(96*la**3-236*la*la+196*la-62)*z+192*la**4-624*la**3+776*la*la-442*la+100
assert B*B-Delta*(D-z*z)**2==z*z*J
assert g2==-2*z*z*J-Delta*(D-z*z)*(2*D-3*z*z)
# If g2=g1=0, either 2D-3z^2=0 gives J=0 directly, or B=0
# gives D=z^2 because z*Delta!=0, and again J=0. Hence g1!=0
# on the already-paid J!=0 scope. No unknown coefficient is inverted.
# theta=-(D-z^2)/(2B) then parametrizes every finite original g2=0 point.
theta_num=-(D-z*z);theta_den=2*B
assert theta_den*g0+theta_num*g1==0
nk=degree(K,2)
Kspecial=zero
for j0 in range(nk+1):Kspecial=Kspecial+co(K,j0)*theta_num**j0*theta_den**(nk-j0)
assert all(int(m[2])==0 for m in Kspecial.to_dict())
bcnum=2*D*D-D*z*z+z**4
Lnum=2*B+s*(D-z*z)
Afnum=R*z*(3*z*z-D)-(z**4+3*D*z*z-2*D*D)
# On this original g2=0 branch:
# u=(l+1)/2, Q=(3-l)/2, T0=(1-3l)/2,
# bc=(2l^2-l+1)/8; P0!=0 pays l(l-1)(l-3).
# L!=0 is explicitly retained; Af!=0 is paid by 51d84b503698....
units=[
 ('lambda',la),('z',z),('Delta',Delta),('paid_small_J',J),
 ('B_for_original_theta_chart',B),('P0_l',D),('P0_u_minus_one',D-z*z),
 ('pq',3*z*z-D),('original_P1_f_coefficient',z*z-3*D),
 ('bc',bcnum),('L_nonzero',Lnum),('paid_Af_nonzero',Afnum)]
def strip(p0):
 if not p0:return p0
 for label,atom in units:
  while True:
   gg=p0.gcd(atom)
   if gg.total_degree()==0:break
   p0=p0/gg
 return p0
F=strip(g2);H=strip(Kspecial)
sha=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
say({'stage':'complete_original_Lt_theta_leading_zero_parameter_chart','sourceSha256':sha,'scope':'S0,Lt0,L!=0,Af!=0,J!=0,g2=0','originalG2':profile(g2),'parameterEquations':[serialized(F),serialized(H)],'allCoefficientZeroBranchesAccountedForByPaidJ':True,'claimExcluded':False})
common=F.gcd(H)
if common.total_degree()>0:
 signal.alarm(0)
 say({'status':'original_theta_leading_zero_parameter_curve_remains','sourceSha256':sha,'commonParameterCurve':serialized(common),'claimExcluded':False})
 raise SystemExit(2)
rr=F.resultant(H,'z')
assert rr and all(int(m[1])==0 and int(m[2])==0 for m in rr.to_dict())
cs={int(m[0]):v for m,v in rr.to_dict().items()}
rp=fmpq_poly([cs.get(i,fmpq(0)) for i in range(max(cs)+1)])
sf=rp/rp.gcd(rp.derivative());sf=sf/sf.leading_coefficient()
content,factors=sf.factor(monic=True)
product=fmpq_poly([content])
for phi,m in factors:product*=phi**m
assert product==sf
say({'stage':'complete_QQ_theta_leading_zero_parameter_projection','sourceSha256':sha,'resultantLambdaDegree':int(rp.degree()),'squarefreeLambdaDegree':int(sf.degree()),'squarefreeSha256':hashlib.sha256(str(sf).encode()).hexdigest(),'factors':[{'degree':int(phi.degree()),'multiplicity':int(m),'coefficientsLowFirst':[str(phi[j0]) for j0 in range(phi.degree()+1)]} for phi,m in factors],'claimExcluded':False})
# Return the whole original parameter fiber, not just roots of a norm.
class FE:
 def __init__(self,field,v=0):
  self.field=field
  if isinstance(v,FE):assert v.field is field;self.p=v.p;return
  pp=v if isinstance(v,fmpq_poly) else fmpq_poly([v])
  self.p=divmod(pp,field.mod)[1]
 def __bool__(self):return bool(self.p)
 def __add__(self,o):o=FE(self.field,o);return FE(self.field,self.p+o.p)
 __radd__=__add__
 def __neg__(self):return FE(self.field,-self.p)
 def __sub__(self,o):return self+-FE(self.field,o)
 def __mul__(self,o):o=FE(self.field,o);return FE(self.field,self.p*o.p)
 __rmul__=__mul__
 def __eq__(self,o):o=FE(self.field,o);return self.p==o.p
 def inv(self):
  assert self
  gg,ss,tt=self.p.xgcd(self.field.mod)
  assert self.p*ss+self.field.mod*tt==gg and gg.degree()==0
  vv=FE(self.field,ss/gg[0]);assert self*vv==1
  self.field.inverses+=1;return vv
class Field:
 def __init__(self,phi):
  self.mod=phi/phi.leading_coefficient();self.inverses=0
  self.zero=FE(self);self.one=FE(self,1)
 def __call__(self,v=0):return FE(self,v)
def tr(pp):
 pp=list(pp)
 while pp and not pp[-1]:pp.pop()
 return pp
def rem(pp,qq):
 pp=tr(pp);qq=tr(qq);assert qq
 inv=qq[-1].inv()
 while pp and len(pp)>=len(qq):
  sh=len(pp)-len(qq);aa=pp[-1]*inv
  for j0,v in enumerate(qq):pp[j0+sh]=pp[j0+sh]-aa*v
  pp=tr(pp)
 return pp
def gcdp(pp,qq):
 pp=tr(pp);qq=tr(qq)
 while qq:pp,qq=qq,rem(pp,qq)
 if pp:
  inv=pp[-1].inv();pp=[inv*v for v in pp]
 return pp
def quo(pp,qq):
 pp=tr(pp);qq=tr(qq);assert qq
 out=[qq[0].field.zero]*max(0,len(pp)-len(qq)+1);inv=qq[-1].inv()
 while pp and len(pp)>=len(qq):
  sh=len(pp)-len(qq);aa=pp[-1]*inv;out[sh]=out[sh]+aa
  for j0,v in enumerate(qq):pp[j0+sh]=pp[j0+sh]-aa*v
  pp=tr(pp)
 assert not pp;return tr(out)
def spec(poly,field):
 terms=poly.to_dict()
 if not terms:return []
 out=[]
 for j0 in range(max(int(m[1]) for m in terms)+1):
  dd={int(m[0]):v for m,v in terms.items() if int(m[1])==j0}
  cs=[fmpq(0)]*(max(dd,default=-1)+1)
  for i,v in dd.items():cs[i]=v
  out.append(field(fmpq_poly(cs)))
 return tr(out)
reports=[]
for phi,m in factors:
 field=Field(phi);ff=spec(F,field);hh=spec(H,field)
 pp=gcdp(ff,hh);history=[];wholezero=None
 for label,atom in units:
  vv=spec(atom,field)
  if not vv:pp=[field.one];wholezero=label;break
  while len(pp)>1:
   gg=gcdp(pp,vv)
   if len(gg)<=1:break
   history.append({'removedOriginalUnit':label,'degree':len(gg)-1});pp=quo(pp,gg)
 report={'lambdaFactor':str(phi),'lambdaDegree':int(phi.degree()),'remainingZDegree':len(pp)-1,'excluded':len(pp)==1,'history':history,'wholeFiberPaidUnitZero':wholezero,'inverseIdentities':field.inverses}
 if len(pp)!=1:report['remainingZCoefficientsInLambdaField']=[str(v.p) for v in pp]
 reports.append(report)
 say({'stage':'original_theta_leading_zero_parameter_fiber_return','report':report,'claimFullCriticalSystemExcluded':False})
closed=all(r['excluded'] for r in reports)
signal.alarm(0)
say({'status':'original_Lt_theta_leading_zero_branch_excluded' if closed else 'finite_original_Lt_theta_leading_zero_candidates_remain','sourceSha256':sha,'scope':'only S0,Lt0,L!=0,Af!=0,J!=0,g2=0','reports':reports,'claimExcluded':closed,'claimWholeS0LayerEmpty':False,'ordinaryISPClaim':False,'peakRssKiB':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss})
raise SystemExit(0 if closed else 2)

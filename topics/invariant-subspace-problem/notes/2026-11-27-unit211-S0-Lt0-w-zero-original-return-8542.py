#!/usr/bin/env python3
"""R150 S0, original P1 t coefficient zero: exact parameter projection.
Return the whole w=0 stratum of the remaining original Lt0 graph.
The remaining distinct-value S0/Lt0 chart is used.
The paid theta-remainder double-zero exclusion permits theta=-F/H.
Every same-parameter original fiber is returned.
All same-parameter roots, physical denominators and original nine equations remain.
The paid J=0 and g2=0 branches are excluded; every remaining original fiber is retained.
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
signal.signal(signal.SIGALRM,alarm_handler);signal.alarm(180)
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
 return {'profile':profile(p),'sha256':hashlib.sha256(str(sorted(p.to_dict().items())).encode()).hexdigest()}
def factor_report(p):
 content,ff=p.factor()
 return {'content':str(content),'factors':[{'exponent':int(e),**serialized(f)} for f,e in ff]}

g0=co(G,0);g1=co(G,1);g2=co(G,2)
assert g0==-(D-z*z)*(2*D-3*z*z)
assert g1==-2*B*(2*D-3*z*z)
assert g2==z*z*(D-z*z)*Delta-2*B*B
J=4*z**3+(12*la*la-4*la-1)*z*z+(96*la**3-236*la*la+196*la-62)*z+192*la**4-624*la**3+776*la*la-442*la+100
assert B*B-Delta*(D-z*z)**2==z*z*J
rem0=K;pseudo_steps=0
while degree(rem0,2)>=2:
 n=degree(rem0,2);rr=co(rem0,n)
 rem0=g2*rem0-rr*th**(n-2)*G;pseudo_steps+=1
assert pseudo_steps==3
r0=co(rem0,0);r1=co(rem0,1);common=r0.gcd(r1)
assert common/(z**5*J)==ctx.constant(fmpq(1,192))
F=r0/common;H=r1/common
assert F.gcd(H).total_degree()==0
# All these units are independent of theta and of the sign of d.
# In particular no norm of a theta-dependent physical unit is discarded.
bcnum=D*D*Delta-B*B
units=[('lambda',la),('z',z),('distinct_h_k_Delta',Delta),
 ('paid_small_J',J),('paid_g2_nonzero',g2),('P0_l_nonzero',D),
 ('original_bc',bcnum)]
def strip(p0):
 if not p0:return p0
 for label,atom in units:
  while True:
   gg=p0.gcd(atom)
   if gg.total_degree()==0:break
   p0=p0/gg
 return p0
sha=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
res=G.resultant(K,'theta');content,factors=res.factor()
M=next(pp for pp,nn in factors if degree(pp,1)==12)
assert degree(M,0)==26
# Exact complete factor cover: no additional parameter factor is omitted.
assert res==256*z**14*J**2*M
lcM=ctx.from_dict({(i,0,0):v for (i,j,k),v in M.to_dict().items() if int(j)==12})
assert lcM==(4*la-1)**2*A**4
Hz=(la-1)*z-C
resu=M.resultant(Hz,'z');cs={int(m[0]):v for m,v in resu.to_dict().items()}
assert all(int(m[1])==0 and int(m[2])==0 for m in resu.to_dict())
rp=fmpq_poly([cs.get(i,0) for i in range(max(cs)+1)])
sf=rp/rp.gcd(rp.derivative());sf/=sf.leading_coefficient()
content,factors=sf.factor(monic=True);product=fmpq_poly([content])
for ph,nn in factors:product*=ph**nn
assert product==sf
say({'stage':'complete_original_w_zero_parameter_cover','sourceSha256':sha,'resultantDegree':int(rp.degree()),'squarefreeDegree':int(sf.degree()),'squarefreeSha256':hashlib.sha256(str(sf).encode()).hexdigest(),'factors':[{'degree':int(ph.degree()),'coefficientsLowFirst':[str(ph[j]) for j in range(ph.degree()+1)]} for ph,nn in factors],'completeResultantFactorization':'Res_theta(G,K)=256 z^14 J^2 M','claimExcluded':False})
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
  self.mod=phi/phi.leading_coefficient();self.inverses=0;self.bezout=0;self.divisions=0
  self.zero=FE(self);self.one=FE(self,1)
 def __call__(self,v=0):return FE(self,v)
def trim(pp):
 pp=list(pp)
 while pp and not pp[-1]:pp.pop()
 return pp
def addpoly(pp,qq,zero):
 out=[zero]*max(len(pp),len(qq))
 for j,v in enumerate(pp):out[j]=out[j]+v
 for j,v in enumerate(qq):out[j]=out[j]+v
 return trim(out)
def mulpoly(pp,qq,zero):
 if not pp or not qq:return []
 out=[zero]*(len(pp)+len(qq)-1)
 for i,v in enumerate(pp):
  for j,w in enumerate(qq):out[i+j]=out[i+j]+v*w
 return trim(out)
def dividep(pp,qq):
 pp=trim(pp);qq=trim(qq);assert qq
 field=qq[0].field;original=list(pp);inv=qq[-1].inv()
 out=[field.zero]*max(0,len(pp)-len(qq)+1)
 while pp and len(pp)>=len(qq):
  shift=len(pp)-len(qq);a=pp[-1]*inv;out[shift]=out[shift]+a
  for j,v in enumerate(qq):pp[shift+j]=pp[shift+j]-a*v
  pp=trim(pp)
 out=trim(out)
 assert original==addpoly(mulpoly(out,qq,field.zero),pp,field.zero)
 field.divisions+=1
 return out,pp
def gcdp(pp,qq):
 pp=trim(pp);qq=trim(qq)
 if not pp and not qq:return []
 field=(pp or qq)[0].field;zero=field.zero;one=field.one
 originalp=list(pp);originalq=list(qq)
 s0=[one];s1=[];t0=[];t1=[one]
 while qq:
  quotient,remainder=dividep(pp,qq);pp,qq=qq,remainder
  s0,s1=s1,addpoly(s0,[-v for v in mulpoly(quotient,s1,zero)],zero)
  t0,t1=t1,addpoly(t0,[-v for v in mulpoly(quotient,t1,zero)],zero)
 if pp:
  inv=pp[-1].inv();pp=[inv*v for v in pp];s0=[inv*v for v in s0];t0=[inv*v for v in t0]
 assert pp==addpoly(mulpoly(s0,originalp,zero),mulpoly(t0,originalq,zero),zero)
 field.bezout+=1
 return pp

tr=trim
def quo(pp,qq):
 out,remainder=dividep(pp,qq);assert not remainder;return out
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
def fpower(self,n):
 assert n>=0
 out=self.field.one;v=self
 while n:
  if n&1:out=out*v
  v=v*v;n//=2
 return out
FE.__pow__=fpower
FE.__rsub__=lambda self,o:FE(self.field,o)+-self
FE.__truediv__=lambda self,o:self*FE(self.field,o).inv()
FE.__rtruediv__=lambda self,o:FE(self.field,o)*self.inv()
reports=[]
for phi,mult in factors:
 field=Field(phi);Lam=field(fmpq_poly([0,1]));pp=gcdp(spec(M,field),spec(Hz,field));history=[]
 for label,atom in units:
  unit=spec(atom,field)
  if not unit:pp=[field.one];history.append({'unit':label,'wholeFiber':True});break
  while len(pp)>1:
   gg=gcdp(pp,unit)
   if len(gg)<=1:break
   pp=quo(pp,gg);history.append({'unit':label,'zDegree':len(gg)-1})
 fiber_label=str(phi)
 if len(pp)==1:
  report={'lambdaFactor':fiber_label,'baseDegree':int(phi.degree()),'remainingZDegree':0,'paidHistory':history,'inverseIdentities':field.inverses,'bezoutIdentities':field.bezout,'claimExcluded':True}
  reports.append(report);say({'stage':'paid_unit_fiber_exclusion','report':report});continue
 assert len(pp)==2
 Z=-pp[0]/pp[1]
 def ep(poly):
  out=field.zero
  for (i,j,k),vv in poly.to_dict().items():
   assert k==0
   out+=vv*(Lam**int(i))*(Z**int(j))
  return out
 assert not ep(M) and not ep(Hz)
 for label,unit in units:ep(unit).inv()
 hval=ep(H);fval=ep(F)
 if not hval:
  if fval:
   fval.inv();reason='original_theta_remainder_constant_unit'
  else:reason='paid_theta_remainder_both_zero'
  report={'lambdaFactor':fiber_label,'baseDegree':int(phi.degree()),'exclusion':reason,'claimExcluded':True};reports.append(report);say({'stage':'theta_remainder_fiber_exclusion','report':report});continue
 Theta=-fval/hval
 g0v=ep(g0);g1v=ep(g1);g2v=ep(g2)
 assert g2v*Theta*Theta+g1v*Theta+g0v==0
 def ept(poly):
  out=field.zero
  for (i,j,k),vv in poly.to_dict().items():out+=vv*(Lam**int(i))*(Z**int(j))*(Theta**int(k))
  return out
 assert not ept(G)
 kval=ept(K)
 if kval:
  kinv=kval.inv();assert kval*kinv==1
  report={'lambdaFactor':fiber_label,'baseDegree':int(phi.degree()),'originalKUnit':True,'inverseIdentities':field.inverses,'inverseSha256':hashlib.sha256(str(kinv.p).encode()).hexdigest(),'claimExcluded':True}
  reports.append(report);say({'stage':'original_K_unit_fiber_exclusion','report':report});continue
 baseDelta=ep(Delta)
 def TH(v=0):return field(v)
 def encode_th(v):return str(v.p)
 lam=TH(Lam);z=TH(Z);theta=TH(Theta);half=fmpq(1,2)
 sv=2*lam-3;Av=2*lam*lam-2*lam+1;Cv=-4*lam*lam+5*lam-2;Rv=3-4*lam
 DeltaValue=TH(baseDelta);iz=z.inv();idel=DeltaValue.inv()
 lv=(sv*Cv-Av*z)*iz*iz;Tv=Cv*iz;wv=lam-1-Tv
 Bv=2*Tv-lv*sv
 u=lv+theta*Bv;Q=1-theta*theta*DeltaValue;bc=(lv*lv-Bv*Bv*idel)*fmpq(1,4)
 V2=2*u-lv*Q;T0=V2-2*u*u;P02=(2-3*u)*V2-Q*u+2*u**3
 assert TH(g2v)*theta*theta+TH(g1v)*theta+TH(g0v)==0
 assert not wv
 assert P02==2*lv*Q*(u-1)
 assert T0+4*(u-1)+Q==0
 Hval=lv+Tv
 bad_unit=None
 for label,v in [('theta',theta),('bc',bc),('pq',Q),('u',u),('P02',P02),('T0',T0),('u-1',u-1),('L/d',1-theta*sv),('Af',Rv-z*(lv+2*u*(1-u)/Q))]:
  if not v:bad_unit=label;break
  v.inv()
 if bad_unit is not None:
  report={'lambdaFactor':fiber_label,'baseDegree':int(phi.degree()),'zeroPhysicalPaidUnit':bad_unit,'inverseIdentities':field.inverses,'claimExcluded':True}
  reports.append(report);say({'stage':'physical_unit_fiber_exclusion','report':report});continue
 fbar=(-T0*T0+2*lv*Q*Q*Hval-2*lam*lv*Q*T0)/(4*(u-1)*T0)
 say({'stage':'original_theta_rational_and_physical_units_verified','baseInverseIdentities':field.inverses,'claimExcluded':False})
 class E:
  def __init__(self,a=0,b=0):
   if isinstance(a,E):self.a=a.a;self.b=a.b;return
   self.a=TH(a);self.b=TH(b)
  def __bool__(self):return bool(self.a) or bool(self.b)
  def __add__(self,o):o=E(o);return E(self.a+o.a,self.b+o.b)
  __radd__=__add__
  def __neg__(self):return E(-self.a,-self.b)
  def __sub__(self,o):return self+-E(o)
  def __rsub__(self,o):return E(o)+-self
  def __mul__(self,o):
   o=E(o);return E(self.a*o.a+DeltaValue*self.b*o.b,self.a*o.b+self.b*o.a)
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

 b=E(lv*half,Bv*idel*half);c=b.conj();a=E(1-lv)
 p=E(1,theta);q=p.conj()
 h=E(1+sv*half,half);k=h.conj();w=E(wv)
 assert b*c==E(bc) and p*q==E(Q) and b*p+c*q==E(u)
 assert a+w+b*h+c*k==E(lam)
 assert a+2*w+b*h*h+c*k*k==E(2*lam*lam)
 assert a+3*w+b*h**3+c*k**3==E(4*lam**3)
 ivdiff=E(0,-(2*theta*DeltaValue).inv())
 ivbp=c*q*ivdiff*E((bc*Q).inv());ivcq=b*p*ivdiff*E((bc*Q).inv())
 assert ivbp*b*p*(q-p)==1 and ivcq*c*q*(q-p)==1
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

 fp=cp(fbar);tp=P({(0,1):E(1)});zero=P()
 one=[cp(1),zero,cp(1),cp(1)]
 def va(v,z0):return [x+y for x,y in zip(v,z0)]
 def vs(v0,v):return [v0*x for x in v]
 def vm(v,z0):return [v[0]*z0[0],v[0]*z0[1]+v[1]*z0[0],v[2]*z0[2],v[3]*z0[3]]
 def tau(v):return scale(a,v[0])+v[1]+scale(b,v[2])+scale(c,v[3])
 W1=cp(T0*half)+scale(E(2*u),fp)
 W2=cp(u*T0+lam*P02)+scale(E(V2+2*u*u),fp)-scale(E(bc*Q),tp)
 XX=scale(ivbp,scale(q,W1)-W2);YY=scale(ivcq,W2-scale(p,W1))
 r=XX-cp(a*p)-scale(c,tp);ss=YY-cp(a*q)-scale(b,tp)
 Arow=scale(E(2),fp)-scale(2*b,XX)-scale(2*c,YY)+scale(E(2*bc),tp)
 rows=[[zero,zero,cp(p),cp(q)],[zero,Arow,r,ss],[cp(p),r,zero,tp],[cp(q),ss,tp,zero]]
 def DK(v):return [tau(vm(row,v)) for row in rows]
 d=DK(one);F2=tau(d);DKd=DK(d);ddv=vm(d,d)
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
  return ev-scale(E(2),DKd[jj])-scale(E(2),ddv[jj])+scale(E(2),F2*d[jj])
 assert not mean(0) and not (P2(rows[0])-cp(P02)) and not (N4(rows[0])-cp(2*lam*P02))
 VV=[cp(1),cp(w),cp(h),cp(k)]
 assert not P2(VV) and not N4(VV)
 raw=[mean(1),mean(2),mean(3),Pjet2(rows[0],rows[1])-cp(3*wv*P02),P2(rows[2])-cp(h**3*E(P02)),P2(rows[3])-cp(k**3*E(P02)),Njet4(rows[0],rows[1])-cp(4*lam*wv*P02),N4(rows[2])-cp(h*h*E(2*lam*P02)),N4(rows[3])-cp(k*k*E(2*lam*P02))]
 assert not raw[3]
 names=['E1','EB','EC','P1','PB','PC','N1','NB','NC']
 dig=hashlib.sha256()
 for name,po in zip(names,raw):
  assert all(ij[0]==0 for ij in po.co)
  for ij,v in sorted(po.co.items()):dig.update((name+str(ij)+encode_th(v.a)+'/'+encode_th(v.b)+'\n').encode())
 inputsha=dig.hexdigest()
 say({'stage':'all_original_nine_on_full_original_fiber_verified','sourceSha256':sha,'fiber':fiber_label,'inputSha256':inputsha,'tDegrees':[max((ij[1] for ij in po.co),default=-1) for po in raw],'P1IdenticallyZero':True,'NvalueIdenticallyZero':True,'fieldInverseIdentitiesChecked':field.inverses,'quadraticIrreducibilityAssumed':False,'claimExcluded':False})
 def trim(pp):
  pp=list(pp)
  while pp and not pp[-1]:pp.pop()
  return pp
 ups=[trim([po.co.get((0,j0),E()) for j0 in range(max((ij[1] for ij in po.co),default=-1)+1)]) for po in raw]
 def determinant(mm):
  n=len(mm)
  if n==0:return E(1)
  if n==1:return mm[0][0]
  out=E()
  for j0 in range(n):
   if mm[0][j0]:out=out+((-1)**j0)*mm[0][j0]*determinant([row[:j0]+row[j0+1:] for row in mm[1:]])
  return out
 def resultant(pp,qq):
  pp=trim(pp);qq=trim(qq)
  if not pp or not qq:return E()
  n=len(pp)-1;m=len(qq)-1
  if n==0:return pp[0]**m if m else pp[0]
  if m==0:return qq[0]**n
  mat=[]
  for i in range(m):mat.append([E()]*i+pp[::-1]+[E()]*(m-1-i))
  for i in range(n):mat.append([E()]*i+qq[::-1]+[E()]*(n-1-i))
  return determinant(mat)
 history=[];acc=E();closed=False;certificate=None
 pairs=[(0,1),(0,2),(1,2),(0,6),(1,6),(2,6),(0,4),(0,5),(1,5),(2,4),(0,7),(0,8)]
 for ii,jj in pairs:
  rr=resultant(ups[ii],ups[jj]);used=None;rinv=None
  for weight in [0,1,2,3]:
   candidate=rr if weight==0 else acc+weight*rr
   norm=candidate.a*candidate.a-DeltaValue*candidate.b*candidate.b
   if norm:
    invnorm=norm.inv();rinv=E(candidate.a*invnorm,-candidate.b*invnorm)
    assert candidate*rinv==1
    used={'currentWeight':weight,'withPreviousAccumulator':weight!=0};closed=True
    certificate={'pair':[names[ii],names[jj]],'combination':used,'normDegreeInLambda':int(norm.p.degree()),'inverseSha256':hashlib.sha256((encode_th(rinv.a)+'/'+encode_th(rinv.b)).encode()).hexdigest(),'fieldInverseIdentitiesChecked':field.inverses,'identity':'original_resultant_combination * its_inverse = 1'}
    break
   if not acc and rr:acc=rr
  history.append({'pair':[names[ii],names[jj]],'zeroResultant':not bool(rr),'unitCertificateFound':closed})
  say({'stage':'actual_original_t_resultant_unit_test','entry':history[-1],'claimExcluded':closed})
  if closed:break
 assert closed
 reports.append({'fiber':fiber_label,'baseDimension':int(phi.degree()),'fullDimension':2*int(phi.degree()),'inputSha256':inputsha,'history':history,'certificate':certificate,'baseInverseIdentities':field.inverses,'quadraticIrreducibilityAssumed':False})
signal.alarm(0)
say({'status':'entire_original_Lt0_w_zero_stratum_excluded','sourceSha256':sha,'reports':reports,'claimExcluded':True,'claimWholeS0LayerEmpty':False,'claimWholeLt0LayerEmpty':False,'ordinaryISPClaim':False,'peakRssKiB':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss})

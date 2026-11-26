#!/usr/bin/env python3
"""R150 S=Af=0, L!=0, (I,H)!=0: exact two-parameter original equations.
Keep both roots d^2=s^2-4z. B/C equations become their even/odd parts.
Return every zero-leading-coefficient lambda fiber to original Chow/F equations.
--stage eliminate also computes exact QQ lambda resultants.
Every discarded coefficient factor is an explicitly paid chart unit.
A universal finite-point identity pays all zero P1 leading coefficients.
"""
import argparse,hashlib,itertools,json,os,resource,signal,time
from pathlib import Path
from flint import fmpq,fmpq_poly,fmpq_mpoly_ctx
started=time.perf_counter()
ap=argparse.ArgumentParser()
ap.add_argument('--stage',choices=['graph','generate','project','eliminate'],default=os.environ.get('ISP_S0_STAGE','project'))
ap.add_argument('--seconds',type=int,default=300)
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
paid_denominators=set()
def paid(r):
 den=R(r).d;key=str(sorted(den.to_dict().items()))
 if key not in paid_denominators:
  assert int(strip_units(den).total_degree())==0
  paid_denominators.add(key)
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
# The full nine rational polynomials are retained and hashed before any
# expensive common-denominator expansion. Only the actual certificate
# polynomials are subsequently cleared.
hh=hashlib.sha256()
for name,pp in zip(names,basepolys):
 for ij,rr in sorted(pp.items()):
  paid(rr)
  hh.update((name+str(ij)+str(sorted(rr.n.to_dict().items()))+'/'+str(sorted(rr.d.to_dict().items()))+'\n').encode())
inputsha=hh.hexdigest()
say({'stage':'all_original_nine_rational_conditions_verified','sourceSha256':sha,'inputSha256':inputsha,'parameterCurve':profile(F),'claimExcluded':False})
if args.stage=='generate':
 finish('all_original_nine_rational_conditions_generated',{'inputSha256':inputsha});raise SystemExit(0)
def matrix_from_coeffs(ff):
 a,b,c,d,e,f0=ff;half=fmpq(1,2)
 return [[a,half*b,half*d],[half*b,c,half*e],[half*d,half*e,f0]]
def adj_line(mm,line):
 a,b,c=mm[0][0],mm[0][1],mm[0][2]
 d,e,f0=mm[1][1],mm[1][2],mm[2][2]
 x,y,z0=line
 return x*x*(d*f0-e*e)+y*y*(a*f0-c*c)+z0*z0*(a*d-b*b)+2*x*y*(c*e-b*f0)+2*x*z0*(b*e-c*d)+2*y*z0*(b*c-a*e)
def chow(mm,nn,line):
 aa=adj_line(mm,line);cc=adj_line(nn,line)
 plus=[[mm[i][j]+nn[i][j] for j in range(3)] for i in range(3)]
 bb=adj_line(plus,line)-aa-cc
 return bb*bb-4*aa*cc
# Universal polynomial verification at an arbitrary common finite point:
# F(f0,t0)=G(f0,t0)=a*f0+b*t0+c=0. No coefficient is inverted.
vctx=fmpq_mpoly_ctx.get(('A','B','C','D','E','J','K','L','M','N','f0','t0','aa','bb'),'lex')
va0,vb0,vc0,vd0,ve0,vj0,vk0,vl0,vm0,vn0,vf0,vt0,vla0,vlb0=vctx.gens()
vconst1=-(va0*vf0**2+vb0*vf0*vt0+vc0*vt0**2+vd0*vf0+ve0*vt0)
vconst2=-(vj0*vf0**2+vk0*vf0*vt0+vl0*vt0**2+vm0*vf0+vn0*vt0)
vline=[vla0,vlb0,-vla0*vf0-vlb0*vt0]
assert not chow(matrix_from_coeffs([va0,vb0,vc0,vd0,ve0,vconst1]),matrix_from_coeffs([vj0,vk0,vl0,vm0,vn0,vconst2]),vline)
say({'stage':'universal_finite_point_Chow_identity_verified','noLineCoefficientInverted':True,'claimExcluded':False})
cleared={}
def get_cleared(index):
 if index in cleared:return cleared[index]
 pp=basepolys[index];den=oo
 for vv in pp.values():den=den*(vv.d/den.gcd(vv.d))
 keys=sorted(pp);nums=strip_common([pp[ij].n*(den/pp[ij].d) for ij in keys])
 out={ij:v for ij,v in zip(keys,nums) if v}
 cleared[index]=out
 say({'stage':'necessary_original_polynomial_cleared','name':names[index],'ftDegree':max((sum(ij) for ij in out),default=-1),'coefficientProfiles':[profile(v) for ij,v in sorted(out.items())],'claimExcluded':False})
 return out
def matrix_of(index):
 po=get_cleared(index)
 assert max((sum(ij) for ij in po),default=-1)<=2
 return matrix_from_coeffs([po.get(ij,zz) for ij in [(2,0),(1,1),(0,2),(1,0),(0,1),(0,0)]])
linepo=get_cleared(3)
assert max((sum(ij) for ij in linepo),default=-1)<=1
line=[linepo.get(ij,zz) for ij in [(1,0),(0,1),(0,0)]]
assert inputsha=='0e9b97510ea6611e122210a58a51b18b266174d6813011a10237174522ccab3c'
pairs=[(0,1),(0,2),(1,2)]
expected=['61fc40f181e395a6181d5bd060a9280a6b0aef955eff334763667faecc8e3405','f2f6f2b4c0212b94fd5d702d63cfaff58f7306700c62026bb06ae26c22fa7f7b','3a9a4b43224163a7133fc21ec8de17887f2a04a3f59a77e832ab21438c35a04c']
chows=[]
for (ii,jj),digest in zip(pairs,expected):
 rr=strip_units(chow(matrix_of(ii),matrix_of(jj),line))
 actual=hashlib.sha256(str(sorted(rr.to_dict().items())).encode()).hexdigest()
 assert actual==digest
 chows.append(rr)
say({'stage':'same_three_original_Chow_polynomials_reconstructed','inputSha256':inputsha,'ChowSha256':expected,'claimExcluded':False})
# The exact actual z-leading coefficient, including every zero fiber.
nz=deg(F)[1]
def lambda_poly_from_dict(dd):
 if not dd:return fmpq_poly([])
 cs=[fmpq(0)]*(max(dd)+1)
 for j,v in dd.items():cs[j]=v
 return fmpq_poly(cs)
lead=lambda_poly_from_dict({int(m[0]):v for m,v in F.to_dict().items() if int(m[1])==nz})
xx=fmpq_poly([0,1]);cubic=10*xx**3-22*xx*xx+19*xx-5
expected_lc=(xx-1)*(xx-2)*cubic*cubic
quo,rem=divmod(lead,expected_lc)
assert not rem and quo and quo.degree()==0
content,factors=lead.factor(monic=True)
assert sorted(int(phi.degree()) for phi,e in factors)==[1,1,3]
class FE:
 def __init__(self,field,v=0):
  self.field=field
  if isinstance(v,FE):
   assert v.field is field;self.p=v.p;return
  pp=v if isinstance(v,fmpq_poly) else fmpq_poly([v])
  self.p=divmod(pp,field.mod)[1]
 def __bool__(self):return bool(self.p)
 def __add__(self,o):o=FE(self.field,o);return FE(self.field,self.p+o.p)
 __radd__=__add__
 def __neg__(self):return FE(self.field,-self.p)
 def __sub__(self,o):return self+-FE(self.field,o)
 def __rsub__(self,o):return FE(self.field,o)+-self
 def __mul__(self,o):o=FE(self.field,o);return FE(self.field,self.p*o.p)
 __rmul__=__mul__
 def __eq__(self,o):o=FE(self.field,o);return self.p==o.p
 def inv(self):
  assert self
  gg,ss,tt=self.p.xgcd(self.field.mod)
  assert self.p*ss+self.field.mod*tt==gg
  assert gg and gg.degree()==0
  vv=FE(self.field,ss/gg[0]);assert self*vv==1
  self.field.inverses+=1
  return vv
class Field:
 def __init__(self,phi):
  self.mod=phi/phi.leading_coefficient();self.inverses=0
  self.zero=FE(self,0);self.one=FE(self,1)
 def __call__(self,v=0):return FE(self,v)
def ftrim(pp):
 pp=list(pp)
 while pp and not pp[-1]:pp.pop()
 return pp
def frem(pp,qq):
 pp=ftrim(pp);qq=ftrim(qq);assert qq
 iv=qq[-1].inv()
 while pp and len(pp)>=len(qq):
  sh=len(pp)-len(qq);co=pp[-1]*iv
  for j,v in enumerate(qq):pp[j+sh]=pp[j+sh]-co*v
  pp=ftrim(pp)
 return pp
def fgcd(pp,qq):
 pp=ftrim(pp);qq=ftrim(qq)
 while qq:pp,qq=qq,frem(pp,qq)
 if pp:
  iv=pp[-1].inv();pp=[iv*v for v in pp]
 return pp
def fquot(pp,qq):
 pp=ftrim(pp);qq=ftrim(qq);assert qq
 field=qq[-1].field
 out=[field.zero]*max(0,len(pp)-len(qq)+1);iv=qq[-1].inv()
 while pp and len(pp)>=len(qq):
  sh=len(pp)-len(qq);co=pp[-1]*iv;out[sh]=out[sh]+co
  for j,v in enumerate(qq):pp[j+sh]=pp[j+sh]-co*v
  pp=ftrim(pp)
 assert not pp
 return ftrim(out)
def specialize(poly,field):
 terms=poly.to_dict()
 if not terms:return []
 dz=max(int(m[1]) for m in terms);out=[]
 for j in range(dz+1):
  dd={int(m[0]):v for m,v in terms.items() if int(m[1])==j}
  out.append(field(lambda_poly_from_dict(dd)))
 return ftrim(out)
unit_names=['lambda','z','Delta','I2 for L!=0','H3 for p!=q','Den for p+q!=0','pq','bc','P0','u','u-1']
reports=[]
for phi,multiplicity in factors:
 field=Field(phi)
 original_f=specialize(F,field);unit_specs=[specialize(v,field) for v in units]
 history=[];gg=original_f;whole_unit_zero=None
 def remove_paid_factors(pp):
  global_dummy=None
  for label,vv in zip(unit_names,unit_specs):
   if not vv:return [field.one],label
   while len(pp)>1:
    common=fgcd(pp,vv)
    if len(common)<=1:break
    history.append({'removedPaidUnit':label,'degree':len(common)-1})
    pp=fquot(pp,common)
  return pp,None
 gg,whole_unit_zero=remove_paid_factors(gg)
 for rr,pair in zip(chows,pairs):
  if len(gg)==1:break
  gg=fgcd(gg,specialize(rr,field))
  history.append({'pair':[names[pair[0]],names[pair[1]]],'commonZDegree':len(gg)-1})
  gg,newzero=remove_paid_factors(gg)
  if newzero:whole_unit_zero=newzero
 closed=len(gg)==1
 serial=';'.join(str(v.p) for v in gg)
 report={'lambdaFactor':str(phi),'factorDegree':int(phi.degree()),'leadingMultiplicity':int(multiplicity),'originalFDegree':len(original_f)-1,'commonZDegree':len(gg)-1,'history':history,'wholeFiberPaidUnitZero':whole_unit_zero,'fieldInverseIdentitiesChecked':field.inverses,'excluded':closed,'remainingPolynomialSha256':hashlib.sha256(serial.encode()).hexdigest()}
 if not closed and len(serial)<=60000:report['remainingZCoefficientsInLambdaField']=[str(v.p) for v in gg]
 reports.append(report)
 say({'stage':'original_zero_leading_coefficient_fiber_return','fiber':report,'claimS0LayerEmpty':False})
closed=all(r['excluded'] for r in reports)
finish('all_original_zero_leading_coefficient_fibers_excluded' if closed else 'original_leading_fiber_candidates_remain',{'inputSha256':inputsha,'sourceCurveLeadingFactorization':{'content':str(content),'factors':[{'factor':str(phi),'multiplicity':int(e)} for phi,e in factors]},'fiberReturns':reports,'claimExcluded':closed,'scope':'only lambda=1,lambda=2,and 10lambda^3-22lambda^2+19lambda-5=0 inside S=Af=0,L!=0,(I,H)!=0'})
raise SystemExit(0 if closed else 2)

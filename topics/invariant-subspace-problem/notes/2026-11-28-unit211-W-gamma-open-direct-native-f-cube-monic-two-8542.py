#!/usr/bin/env python3
"""NEW current W gamma-open full original monic f^2 and I6 two columns.
Use the PAID native C9 six rules only through their definition prefix:
one NEW homogeneous f^3 reduction gives an explicit full-chart head
Bezout1, without a parameter-field Euclid or a new weight exceptional C.
All original products and both-column source tags are returned.
No old 18-multiplication/cofactor/norm/module gate is executed.
First 180 seconds / 4 GiB; one frozen C9 source dependency; hash-only output.
"""
import json,time,hashlib,signal,resource,itertools,contextlib,io,math
from pathlib import Path
from flint import fmpq,fmpq_poly,fmpq_mpoly_ctx
import sys
START=time.perf_counter();DEADLINE=START+180;signal.setitimer(signal.ITIMER_REAL,180)
resource.setrlimit(resource.RLIMIT_AS,(4*1024**3,4*1024**3))
def say(**kw):
 kw['seconds']=time.perf_counter()-START
 print(json.dumps(kw,separators=(',',':')),flush=True)
def digest(x):
 raw=json.dumps(x,separators=(',',':')).encode()
 return dict(bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest())
ctx=fmpq_mpoly_ctx.get(('e','k','s','f'),'lex');ep,kp,sp,fp=ctx.gens()
zz=ctx.constant(0);oo=ctx.constant(1)
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


e,k,ss,f=R(ep),R(kp),R(sp),R(fp);u=e+1;Q=e*k;Vbar=u*k+2
l=u*((k+2)**2-2*Q)/(k*Vbar);Delta=1-Q;m=u-l
V2=2*u-l*Q;T0=V2-2*u*u;M=l*V2-u*u
Uhat=V2-u;gamma=4*Delta-Uhat*ss
beta=4*Delta-2*u*m*ss-M*ss*ss/4
cc=-ss*(M*u+m*T0/2)+M*u*ss*ss/4
V=(beta*f+cc)/gamma;t=(f-u)*ss
W1=(T0+4*u*f)/2
x0=(Uhat*V-m*W1)/M;x1=(l*W1-u*V)/M
assert 4*Delta*(f-u)-Uhat*t==(f-u)*gamma
Rnorm=4*(f-u)*(V-f)+(M/(4*Delta))*t*t+t*(M*u/Delta-l*V+m*(T0+4*u*f-2*V)/(2*Delta))
assert not Rnorm
L=4*k*e*e-(k*k+4*k+8)*e-(k*k+6*k+8)
assert 2*l-1==-L/(k*Vbar)
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
p=E(1,1);q=p.conj();bc=M/(4*Delta)
assert b*c==E(bc) and b+c==E(l) and b*p+c*q==E(u)
X=E(x0,x1);Y=X.conj()
P02=(2-3*u)*V2-Q*u+2*u**3
assert f==(u*x0+(u-l*Q)*x1-T0/2)/(2*u)
W2=V2*x0+(2*u-u*Q-l*Q)*x1
lam=(W2-u*T0-(V2+2*u*u)*f+bc*Q*t)/P02
J=2*u*(1-u)+l*Q;Phi=T0+4*u-4+Q;Pf=T0*(J-Q)
G0=lam*P02-(1-u)*T0
T=(G0*T0-Pf*f-Phi*bc*Q*t)/(Q*P02)-l
assert Phi*(J-2*u*Q)-Pf==0
r=X-a*p-c*E(t);s=Y-a*q-b*E(t)
A=E(2*f)-2*b*X-2*c*Y+E(2*bc*t)
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
EW=b*EB+c*EC
assert not EW.b and E1==EW

def N4(v):
 return 2*tau(vm(d,vm(v,v)))-F2*tau(vm(v,v))-4*tau(v)*tau(vm(d,v))+2*F2*tau(v)**2+tau(vm(v,DK(v)))
vc=va(rows[0],vs(-tau(rows[0]),one))
zc=va(rows[1],vs(-tau(rows[1]),one))
Pj=3*tau(vm(vm(vc,vc),zc))
Nv=N4(va(rows[0],rows[1]))-N4(rows[0])-N4(rows[1])
N1=Nv-E(lam*fmpq(4,3))*Pj
assert not N1.b
assert N4(rows[0])==E(2*lam*P02)
assert Pj==E(3*(lam-1-T)*P02)
def P2(v):
 cc=va(v,vs(-tau(v),one))
 return tau(vm(vm(cc,cc),cc))
assert P2(rows[0])==E(P02)
A2=2*lam*lam-2*lam+1;B3=4*lam**3-6*lam*lam+3*lam-1
NS=b*N4(rows[2])+c*N4(rows[3])-E(2*lam*P02*(l+2*T+A2))
PS=b*P2(rows[2])+c*P2(rows[3])-E(P02*(l+3*T+3*A2+B3))
assert not NS.b and not PS.b
Dphysical=l*A2-T*T

assert b*X+c*Y==E(V) and b*p*X+c*q*Y==E(W1)
original=[EW.a,EB.b,N1.a,NS.a,PS.a]
for value in original:
 assert all(int(mm[3])==0 for mm in value.d.to_dict())
assert all(not original[i] or int(original[i].n.degrees()[3])<=2 for i in range(3))
assert all(not original[i] or int(original[i].n.degrees()[3])<=3 for i in [3,4])
say(stage='new_gamma_open_original_slope_and_f_rows',
 originalE0N0P0P1Returned=True,trueDualGermSquare=True,
 wholeCorrectRDividedOnlyByPaidFMinusU=True,
 originalE1EqualsWeightedMeanReturned=True,
 sameOriginalN1NSPSSinglePoint=True,
 remainingPrincipalOpen='s*(4delta-Uhat*s)!=0',
 physicalFMinusUStillRequired=True,
 fDegrees=[int(v.n.degrees()[3]) if v else -1 for v in original])

exact_products=0
def dex(p,q):
 global exact_products
 a0,b0=divmod(p,q);assert not b0 and a0*q==p
 exact_products+=1;return a0
def profile(p):
 if not p:return dict(zero=True,degrees_e_k_s_f=[-1]*4,terms=0)
 data=[[list(map(int,mm)),str(c0)] for mm,c0 in sorted(p.to_dict().items())]
 return dict(zero=False,degrees_e_k_s_f=list(map(int,p.degrees())),
  totalDegree=int(p.total_degree()),terms=len(data),**digest(data))
Hold=4*ep*kp-kp*kp-4*kp-8
base_atoms=[('e',ep),('k',kp),('u',ep+1),('Q_minus_one',ep*kp-1),
 ('Vbar',(ep+1)*kp+2),('Phi_k_plus_four',kp+4),('P02',P02.n),('M',M.n),
 ('k_plus_one',kp+1),('whole_H_old',Hold),('whole_equal_weights_k_plus_two',kp+2),
 ('whole_ell_zero',l.n),('whole_Lhalf_zero',L.n),
 ('whole_equal_weights_Q_minus_two',(Q-2).n),
 ('s_equals_t_over_f_minus_u',sp),('gamma_current_chart',gamma.n)]

# These entire original weight curves have independently been excluded:
# R150-appendix-unit211-W-J19-entire-original-weight-curve-exclusion.md
# R150-appendix-essential-four-unit-two-plus-one-plus-one-generic-LS-W-C9-complete-original-exclusion.md
J19=(16*ep**4*kp**3-8*ep**3*kp**4-16*ep**3*kp**3-96*ep**3*kp**2
 -ep**2*kp**5-8*ep**2*kp**4+24*ep**2*kp**3+64*ep**2*kp**2+192*ep**2*kp
 -2*ep*kp**5-14*ep*kp**4-12*ep*kp**3-128*ep
 -kp**5-10*kp**4-40*kp**3-104*kp**2-160*kp-128)
C9=4*ep*ep*kp*kp-ep*(kp**4+9*kp**3+20*kp*kp+16*kp)+kp**3+10*kp*kp+24*kp+16
base_atoms+=[('whole_original_J19',J19),('whole_original_C9',C9)]

def strip_atoms(p,atoms):
 before=p;scale=oo;hist=[]
 if not p:return p,scale,hist
 for name,atom in atoms:
  count=0
  while True:
   gg=p.gcd(atom)
   if int(gg.total_degree())==0:break
   p=dex(p,gg);scale*=gg;count+=1
  if count:hist.append([name,count])
 assert p*scale==before
 return p,scale,hist
def paid_den(p,atoms):
 rest,_,_=strip_atoms(p,atoms)
 assert rest and int(rest.total_degree())==0
for value in [l,M,x0,x1,t,lam,T]+original:paid_den(value.d,base_atoms)
def cooperate(fn):
 def call(self,other):
  if getattr(other,'_isp_quotient_level',0)>0:return NotImplemented
  return fn(self,other)
 return call
for name in ['__add__','__radd__','__sub__','__rsub__','__mul__','__rmul__','__truediv__','__rtruediv__','__eq__']:
 setattr(R,name,cooperate(getattr(R,name)))
def trim(a0):
 while a0 and not a0[-1]:a0.pop()
 return a0
class U:
 _isp_quotient_level=1
 def __init__(self,v=0):
  if isinstance(v,U):self.c=v.c[:];return
  self.c=trim([R(x) for x in v]) if isinstance(v,(list,tuple)) else ([R(v)] if R(v) else [])
 def __bool__(self):return bool(self.c)
 def degree(self):return len(self.c)-1
 def __add__(self,v):
  v=U(v);n=max(len(self.c),len(v.c))
  return U([(self.c[j] if j<len(self.c) else R())+(v.c[j] if j<len(v.c) else R()) for j in range(n)])
 __radd__=__add__
 def __neg__(self):return U([-x for x in self.c])
 def __sub__(self,v):return self+-U(v)
 def __rsub__(self,v):return U(v)+-self
 def __mul__(self,v):
  v=U(v)
  if not self or not v:return U()
  out=[R() for _ in range(len(self.c)+len(v.c)-1)]
  for i,x in enumerate(self.c):
   for j,y in enumerate(v.c):out[i+j]=out[i+j]+x*y
  return U(out)
 __rmul__=__mul__
 def __truediv__(self,v):
  assert not isinstance(v,U);v=R(v);assert v
  return U([x/v for x in self.c])
 def __eq__(self,v):
  v=U(v);return len(self.c)==len(v.c) and all(x==y for x,y in zip(self.c,v.c))
 def __pow__(self,n):
  assert n>=0
  out=U(1)
  for _ in range(n):out=out*self
  return out
def udiv(a0,b0):
 global exact_products
 a0=U(a0);b0=U(b0);assert b0
 r0=U(a0);q0=U()
 while r0 and r0.degree()>=b0.degree():
  d0=r0.degree()-b0.degree();co=r0.c[-1]/b0.c[-1]
  term0=U([R()]*d0+[co]);q0=q0+term0
  r0=r0-term0*b0
 assert q0*b0+r0==a0
 exact_products+=1
 return q0,r0
def as_u(value,axis):
 assert all(int(mm[axis])==0 for mm in value.d.to_dict())
 if not value:return U()
 deg=int(value.n.degrees()[axis]);out=[zz for _ in range(deg+1)]
 for mm,co in value.n.to_dict().items():
  ex=list(map(int,mm));power=ex[axis];ex[axis]=0
  out[power]+=co*ep**ex[0]*kp**ex[1]*sp**ex[2]*fp**ex[3]
 return U([R(p0,value.d) for p0 in out])
def at_u(polyU,var):
 out=R()
 for co in reversed(polyU.c):out=out*var+co
 return out
fu=[as_u(v,3) for v in original]
heads=[p0.c[2] if len(p0.c)>2 else R() for p0 in fu[:3]]

# Necessary old definitions only: stop before all 18 multiplication columns.
path=Path(__file__).with_name('2026-11-27-unit211-generic-LS-W-C9-six-generator-original-parameter-cofactors-8542.py')
raw=path.read_bytes()
assert hashlib.sha256(raw).hexdigest()=='10720660772a9a1252b905b1227b697e038d1b974b7e96ec30e485477b21d3f1'
marker=b'\nmatrices=[];errors=[]'
assert raw.count(marker)==1
prefix=raw.split(marker)[0]
assert len(prefix)==14656
assert hashlib.sha256(prefix).hexdigest()=='88b8e2f49f925e51c0b940f929efb502ced9ed358228a605fea3755d9cdefff8'
ns={'__file__':str(path),'__name__':'paid_native_rules_for_new_homogeneous_f_cube_only'}
old_alarm=signal.alarm;old_timer=signal.setitimer
def timer(which,seconds,interval=0.0):
 if which!=signal.ITIMER_REAL:return old_timer(which,seconds,interval)
 assert not interval
 left=max(.001,DEADLINE-time.perf_counter())
 return old_timer(which,min(left,float(seconds) if seconds>0 else left),0.0)
def alarm(seconds):return math.ceil(timer(signal.ITIMER_REAL,seconds)[0])
signal.alarm=alarm;signal.setitimer=timer
try:
 with contextlib.redirect_stdout(io.StringIO()):
  exec(compile(prefix,str(path)+'#necessary_six_rule_definitions','exec'),ns)
finally:
 signal.alarm=old_alarm;signal.setitimer=old_timer
 old_timer(signal.ITIMER_REAL,max(.001,DEADLINE-time.perf_counter()))
assert ns['freemons']==[(0,0,0),(1,0,0),(0,1,0),(0,0,1),(0,2,0),(0,1,1)]
assert len(ns['q'])==6
def embed_weight(p0):
 out=zz
 for mm,cc0 in p0.to_dict().items():
  assert all(not int(mm[j]) for j in range(2,8))
  out+=cc0*ep**int(mm[0])*kp**int(mm[1])
 return out
# Pay actual selected determinant polynomials, not merely old chart names.
for p0 in [ns['delta2'],ns['delta3'].n,ns['delta3'].d]:
 paid_den(embed_weight(p0),base_atoms)
oldftop=(ns['u']*ns['x0']+(ns['u']-ns['l']*ns['Q'])*ns['x1'])/(2*ns['u'])
oldrow,oldtag=ns['reduce_six'](oldftop**3)
assert len(oldrow)==6 and not oldtag[4] and not oldtag[5]
oldR=ns['R'];oldbasis=ns['basis'];oldoriginal=ns['original']
oldrem=sum((oldrow[j]*oldbasis[j] for j in range(6)),oldR())
assert oldftop**3-oldrem==sum((-oldtag[j]*oldoriginal[j] for j in range(6)),oldR())
xf=as_u(x0,3).c[1];yf=as_u(x1,3).c[1]
assert u*xf+Uhat*yf==2*u
directions=[xf,yf,ss]
weights=[]
for i in range(4):
 tag=-oldtag[i];den=embed_weight(tag.d);paid_den(den,base_atoms)
 val=R()
 for mm,cc0 in tag.n.to_dict().items():
  assert all(not int(mm[j]) for j in range(5,8))
  geos=list(map(int,mm[2:5]));degree=sum(geos);assert degree<=1
  if degree!=1:continue
  axis=geos.index(1)
  val+=R(cc0*ep**int(mm[0])*kp**int(mm[1]),den)*directions[axis]
 weights.append(val)
# E1^top=EW^top; EBe^top=(EW^top-m*EBo^top)/ell.
cofs=[weights[0]+weights[1]/l,weights[2]-m*weights[1]/l,weights[3]]
assert sum((cofs[j]*heads[j] for j in range(3)),R())==R(1)
for co in cofs:paid_den(co.d,base_atoms)
cover=oo;chart_atoms=base_atoms
say(stage='new_global_gamma_original_homogeneous_f_cube_head_Bezout',
 originalHomogeneousCubeAndAllSixTraceColumnsReturned=True,
 originalHighestDegreeRemainderAtMostTwo=True,
 explicitContextEmbedding=True,
 sameFInfinityDirectionHasFLeadingOne=True,
 allThreeActualFQuadraticHeadsCombinedToOne=True,
 allFinalDenominatorsOnlyPreviouslyPaidWeightsAndGamma=True,
 noNewWeightCover=True,noParameterFieldEuclidExecuted=True,
 oldEighteenMultiplicationAndCofactorTailNotExecuted=True,
 coefficients=[dict(numerator=profile(co.n),denominator=profile(co.d)) for co in cofs])
qf=sum((fu[j]*cofs[j] for j in range(3)),U())
assert qf.degree()==2 and qf.c[2]==R(1)
qtag=[U(cofs[j]) if j<3 else U() for j in range(5)]
assert sum((qtag[j]*fu[j] for j in range(5)),U())==qf
say(stage='new_actual_monic_f_two_original_combination',
 pureWeightCover=profile(cover),noAdditionalWeightExceptionalCover=True,
 allDenominatorsPaidOnWholeGammaChart=True,
 qfCoefficients=[dict(numerator=profile(x.n),denominator=profile(x.d)) for x in qf.c],
 allThreeOriginalFColumnsReturned=True,
 environmentFreeRankTwo=True,originalQuotientNotAssumedFree=True)
rows=[];row_tags=[]
for i,p0 in enumerate(fu):
 quot,rem=udiv(p0,qf)
 tg=[-quot*qtag[j]+(U(1) if i==j else U()) for j in range(5)]
 assert sum((tg[j]*fu[j] for j in range(5)),U())==rem
 rows.append(rem);row_tags.append(tg)
Uf=U([0,1])
for i in range(5):
 quot,rem=udiv(Uf*rows[i],qf)
 tg=[Uf*row_tags[i][j]-quot*qtag[j] for j in range(5)]
 assert sum((tg[j]*fu[j] for j in range(5)),U())==rem
 rows.append(rem);row_tags.append(tg)
assert all(p0.degree()<=1 for p0 in rows)
say(stage='new_complete_original_I6_ten_by_two_presentation',
 originalRows=['EW','EBo','N1','NS','PS'],
 allTenOriginalFullPolynomialTagsReturned=True,
 allMonicDivisionProductsReturned=True,
 sameActualBasis=['1','f'],basisValueColumnNeverZero=True,
 noFreeOriginalModuleAssumption=True,fullIdealEquivalenceOnWholeGammaChart=True,
 rowProfiles=[[dict(numerator=profile(x.n),denominator=profile(x.d)) for x in p0.c] for p0 in rows])
def clear_row(p0,tg):
 den=oo
 for co in p0.c:
  paid_den(co.d,chart_atoms);den=dex(den,den.gcd(co.d))*co.d
 vals=[co.n*dex(den,co.d) for co in p0.c]+[zz]*(2-len(p0.c))
 rr=U([R(x) for x in vals]);tt=[R(den)*h0 for h0 in tg]
 assert sum((tt[j]*fu[j] for j in range(5)),U())==rr
 return vals,tt
cleared=[clear_row(rows[i],row_tags[i]) for i in range(10)]
scalar_records=[]
for i,j in itertools.combinations(range(10),2):
 aa,ta=cleared[i];bb,tb=cleared[j]
 if not aa[1] and not bb[1]:
  if not aa[0]:continue
  ca,cb=oo,zz
 else:
  gcd=aa[1].gcd(bb[1]);assert gcd
  ca=dex(bb[1],gcd);cb=-dex(aa[1],gcd)
 raw=ca*aa[0]+cb*bb[0]
 assert ca*aa[1]+cb*bb[1]==zz
 if not raw:continue
 newtag=[R(ca)*ta[k0]+R(cb)*tb[k0] for k0 in range(5)]
 assert sum((newtag[k0]*fu[k0] for k0 in range(5)),U())==U(R(raw))
 core,removed,hist=strip_atoms(raw,chart_atoms)
 if core:
  lc=core.coefficient(0);core/=lc;removed*=lc
 assert core*removed==raw
 rec=dict(selectedOriginalRows=[i,j],actualConstant=profile(raw),
  necessaryPrimitive=profile(core),onlyDeclaredChartUnitRemoval=hist,
  bothFullFColumnsAndFiveOriginalTagsReturned=True,
  onlyCommonActualMultipliersCancelled=True)
 say(stage='new_same_f_two_column_original_scalar',**rec)
 scalar_records.append(rec)
 if len(scalar_records)==2:break
say(stage='new_global_gamma_open_monic_f_two_original_input_finished',
 sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 pureWeightCover=profile(cover),
 wholeCoverZeroFiberRetained=True,
 exactDivisionProducts=exact_products,fullOriginalScalarCount=len(scalar_records),
 noOldGateExecuted=True,noPayloadSaved=True,
 peakRSSKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
 originalChartExcluded=False,ordinaryISPClaim=False)

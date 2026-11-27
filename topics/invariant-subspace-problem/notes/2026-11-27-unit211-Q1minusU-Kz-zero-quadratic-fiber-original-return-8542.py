#!/usr/bin/env python3
"""R150 Q=1-u, complete Kz=0 rational weight input:
multiplication, the two remaining cubic rows, NS/PS, and two original
parameter cofactors. The whole m=1/2 and T0=0 branches are already excluded.
180 seconds / 4 GiB. No previously frozen QQ or W cofactor gate is rerun.
"""
import json,time,os,sys,hashlib,subprocess,shutil,tempfile,resource
from pathlib import Path
from flint import fmpq,fmpq_mpoly_ctx
import signal
signal.alarm(120)
resource.setrlimit(resource.RLIMIT_AS,(1024**3,1024**3))
start=time.perf_counter()
def say(x=None,**kw):
 if x is None:x=kw
 x['seconds']=time.perf_counter()-start;print(json.dumps(x),flush=True)
ctx=fmpq_mpoly_ctx.get(('h','weight_dummy','x','y','t','dummy_t','zeta','dummy'),'lex');ep,kp,Lp,Tp,fp,tp,zp,dp=ctx.gens();zz=ctx.constant(0);oo=ctx.constant(1)
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
h,unusedWeight,x0,x1,t,unused,zeta=map(R,ctx.gens()[:7]);denh=h*h-h+2;u=(h-1)**2/denh;l=u*h;Q=1-u;Delta=u
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
X=E(x0,x1);Y=X.conj()
f=(u*x0+(u-l*Q)*x1-T0/2)/(2*u)
W2=V2*x0+(2*u-u*Q-l*Q)*x1
lam=(W2-u*T0-(V2+2*u*u)*f+bc*Q*t)/P02
J=2*u*(1-u)+l*Q;Phi=T0+4*u-4+Q;Pf=T0*(J-Q)
g=lam*P02-(1-u)*T0
T=(g*T0-Pf*f-Phi*bc*Q*t)/(Q*P02)-l
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




assert N4(rows[0])==E(2*lam*P02)
assert Pj==E(3*(lam-1-T)*P02)
A2=2*lam*lam-2*lam+1;B3=4*lam**3-6*lam*lam+3*lam-1

def P2(vv):
 cc=va(vv,vs(-tau(vv),one));return tau(vm(vm(cc,cc),cc))
NS=b*N4(rows[2])+c*N4(rows[3])-E(2*lam*P02*(l+2*T+A2))
PS=b*P2(rows[2])+c*P2(rows[3])-E(P02*(l+3*T+3*A2+B3))
assert not NS.b and not PS.b

# Explicit original value traces for the two weighted singleton rows.
assert P2(rows[0])==E(P02)
v1=(T-l*zeta)/u;v0=v1+zeta;hh=E(1+v0,v1);kk=hh.conj()
M=l*(2*u-l*Q)-u*u;Dphysical=l*A2-T*T
HA=l*M*zeta*zeta-2*T*M*zeta+V2*T*T-u*u*A2
zvalue=(hh-1)*(kk-1);assert not zvalue.b
HB=u*u*(B3-2*v0*A2+zvalue.a*T)
assert b*(hh-1)+c*(kk-1)==E(T)
assert b*hh*hh+c*kk*kk==E(l+2*T+A2+HA/(u*u))
assert b*hh**3+c*kk**3==E(l+3*T+3*A2+B3+((3+2*v0)*HA-HB)/(u*u))
weightedNB=b*(N4(rows[2])-E(2*lam*P02)*hh*hh)+c*(N4(rows[3])-E(2*lam*P02)*kk*kk)
weightedPB=b*(P2(rows[2])-E(P02)*hh**3)+c*(P2(rows[3])-E(P02)*kk**3)
assert weightedNB==NS-E(2*lam*P02*HA/(u*u))
assert weightedPB==PS-E(P02*((3+2*v0)*HA-HB)/(u*u))
assert E(Dphysical+l*HA/(u*u))==E(bc)*(hh-kk)**2
assert 4*bc*(1-Q)==M

assert P02==(1-u)*((3*u-2)*l-2*u*u+3*u)
assert T0==(1-u)*(2*u-l)
Rt0=u*EB.b+(u-l*Q)/u*EB.a
Ry0=-4*bc*EB.a+l*Rt0
symbolic={'lam':lam,'T':T,'f':f,'ell':l,'Dphysical':Dphysical,'E1':E1.a,'Rt0':Rt0,'Ry0':Ry0,'N1':NH.a,'NS':NS.a,'PS':PS.a}
say(stage='new_Qboundary_KzZero_chart_same_original_Gram',originalE0N0P1Verified=True,weightedOriginalNPThroughHAHBVerified=True,originalDistinctValueRetained=True,wholeWeightChartExcluded=False)
Mp=M.n
Hp=((2*u-1)*l+u).n
P0p=P02.n
G2p=((6*u-4)*l**3+2*l**2+(-2*u+8*u*u-8*u**3)*l-2*u*u).n
assert M==u**3*(h-2)
assert ((2*u-1)*l+u)==u*(h-2)*(h-1)*(h+1)/denh
assert P02==u*Q*(h-2)**2*(h+1)/denh
assert 2*u-1==h*(h-3)/denh
units=[('h',ep),('h_minus_one',ep-1),('h_plus_one',ep+1),('h_minus_two',ep-2),('h_minus_three',ep-3),('h_square_minus_h_plus_two',ep*ep-ep+2)]

out=[];cleared_polys=[];cleared_scales=[]
for name,rr,deg in [('E1',E1.a,2),('Rt0',Rt0,2),('Ry0',Ry0,2),('N1',NH.a,2),('weighted_N',NS.a,3),('weighted_P',PS.a,3)]:
 assert all(int(m[2])+int(m[3])+int(m[4])<=deg for m in rr.n.to_dict())
 po=rr.n;paid=oo;hist=[]
 for name0,atom in units:
  ct=0
  while po:
   gg=po.gcd(atom)
   if gg.total_degree()==0:break
   po=po/gg;paid*=gg;ct+=1
  if ct:hist.append([name0,ct])
 assert po*paid==rr.n
 den=rr.d
 for name0,atom in units:
  while den:
   gg=den.gcd(atom)
   if gg.total_degree()==0:break
   den=den/gg
 assert den.total_degree()==0
 rec={'name':name,'poly':[[list(map(int,m)),str(a)] for m,a in po.to_dict().items()],'den':[[list(map(int,m)),str(a)] for m,a in rr.d.to_dict().items()]};out.append(rec);cleared_polys.append(po);cleared_scales.append(R(rr.d,paid))
 say({'stage':'new_Qboundary_KzZero_chart_original_X_Gram_coordinates','name':name,'degrees':list(map(int,po.degrees())),'terms':len(po.to_dict()),'paidRemoved':hist,'totalDegreeXYt':deg,'originalE0N0P1AndMeanReconstructionVerified':True,'claimExcluded':False})

# New whole Kz=0 degree-four original Macaulay input. No G2 chart inverse.
from fractions import Fraction
from flint import fmpq_poly
def mons_upto(d):
 return [(i,j,k) for n in range(d+1) for i in range(n,-1,-1) for j in range(n-i,-1,-1) for k in [n-i-j]]
allmons=mons_upto(4);assert len(allmons)==35
allmons=allmons[1:]+allmons[:1]
posmon={mm:i for i,mm in enumerate(allmons)}
def mxyz(mm):return Lp**mm[0]*Tp**mm[1]*fp**mm[2]
def coefdict(po):
 out={}
 for mm,cc in po.to_dict().items():
  assert mm[1]==mm[5]==mm[6]==mm[7]==0
  key=tuple(map(int,mm[2:5]))
  out[key]=out.get(key,zz)+cc*ep**int(mm[0])
 return out
matrix=[];labels=[]
for gi,po in enumerate(cleared_polys):
 cmap=coefdict(po)
 for multiplier in mons_upto(2 if gi<4 else 1):
  row=[zz for _ in range(35)]
  for mm,cf in cmap.items():
   target=tuple(mm[j]+multiplier[j] for j in range(3));row[posmon[target]]+=cf
  ret=sum((row[j]*mxyz(allmons[j]) for j in range(35)),zz)
  assert ret==mxyz(multiplier)*po
  assert R(ret)==R(mxyz(multiplier))*cleared_scales[gi]*symbolic[['E1','Rt0','Ry0','N1','NS','PS'][gi]]
  matrix.append(row);labels.append([gi,list(multiplier)])
assert len(matrix)==48
inputhash=hashlib.sha256('|'.join(str(po) for row in matrix for po in row).encode()).hexdigest()
say(stage='new_whole_KzZero_original_Macaulay4',rows=48,columns=35,
    originalSixRows=6,all48OriginalMonomialProductsMultipliedBack=True,constantColumn=34,inputSHA256=inputhash,
    G2Inverted=False,cubicMinorInverted=False,claimExcluded=False)

# New exact whole quadratic quotient of the already completed QQ cover.
# 2*h^2-h+1=0; write h=(1+v)/4 and v^2=-7. No chosen embedding.
kinverse_count=0
class K2:
 def __init__(self,a=0,b=0):
  if isinstance(a,K2):self.a=a.a;self.b=a.b;return
  self.a=fmpq(a);self.b=fmpq(b)
 def __bool__(self):return bool(self.a) or bool(self.b)
 def __add__(self,o):o=K2(o);return K2(self.a+o.a,self.b+o.b)
 __radd__=__add__
 def __neg__(self):return K2(-self.a,-self.b)
 def __sub__(self,o):return self+-K2(o)
 def __rsub__(self,o):return K2(o)+-self
 def __mul__(self,o):o=K2(o);return K2(self.a*o.a-7*self.b*o.b,self.a*o.b+self.b*o.a)
 __rmul__=__mul__
 def inv(self):
  global kinverse_count
  norm=self.a*self.a+7*self.b*self.b
  assert norm
  v=K2(self.a/norm,-self.b/norm);assert self*v==K2(1);kinverse_count+=1;return v
 def __truediv__(self,o):return self*K2(o).inv()
 def __eq__(self,o):o=K2(o);return self.a==o.a and self.b==o.b
 def __pow__(self,n):
  out=K2(1);base=self
  while n:
   if n&1:out=out*base
   base=base*base;n//=2
  return out
 def data(self):return [str(self.a),str(self.b)]
hk=K2(fmpq(1,4),fmpq(1,4))
assert 2*hk*hk-hk+1==0
def evalK(po):
 out=K2()
 for mm,cc in po.to_dict().items():
  assert all(mm[j]==0 for j in range(1,8));out+=K2(cc)*hk**int(mm[0])
 return out
def evalR(rr):return evalK(rr.n)/evalK(rr.d)
assert evalR(u)==K2(fmpq(1,2))-hk and evalR(l)==K2(fmpq(1,2))
for name,atom in units:
 value=evalK(atom);assert value;assert value*value.inv()==K2(1)
actual=[[evalK(po) for po in row] for row in matrix]
aug=[row[:]+[K2(int(i==j)) for j in range(48)] for i,row in enumerate(actual)]
pivots=[];rank=0
for col in range(35):
 opts=[i for i in range(rank,48) if aug[i][col]]
 if not opts:continue
 sw=opts[0];aug[rank],aug[sw]=aug[sw],aug[rank]
 inv=aug[rank][col].inv();aug[rank]=[v*inv for v in aug[rank]]
 for i in range(48):
  if i==rank or not aug[i][col]:continue
  cf=aug[i][col];aug[i]=[v-cf*w for v,w in zip(aug[i],aug[rank])]
 pivots.append(col);rank+=1
 if rank==48:break
assert len(pivots)==rank
say(stage='new_whole_KzZero_quadratic_field_original_RREF',fieldPolynomial='2*h^2-h+1',representation='h=(1+v)/4, v^2=-7',
    originalRows=48,originalColumns=35,rank=rank,pivotColumns=pivots,allFieldInversesMultipliedBack=kinverse_count,
    originalWeights='u=1/2-h, ell=1/2',allOriginalUnitImagesNonzero=True,claimExcluded=False)
def original_target_return(target):
 remainder=target[:];tag=[K2() for _ in range(48)]
 for i,col in enumerate(pivots):
  cf=remainder[col]
  if not cf:continue
  remainder=[v-cf*w for v,w in zip(remainder,aug[i][:35])]
  tag=[v+cf*w for v,w in zip(tag,aug[i][35:])]
 reproduced=[sum((tag[i]*actual[i][j] for i in range(48)),K2()) for j in range(35)]
 assert all(reproduced[j]+remainder[j]==target[j] for j in range(35))
 return remainder,tag
one_target=[K2(int(i==34)) for i in range(35)]
one_rem,one_tag=original_target_return(one_target)
dphys=symbolic['Dphysical'];dc=coefdict(dphys.n);dtarget=[evalK(dc.get(mm,zz)) for mm in allmons]
assert evalK(dphys.d)
drem,dtag=original_target_return(dtarget)
direct=not any(one_rem);physical=not any(drem)
record=dict(stage='new_whole_KzZero_quadratic_field_actual_original_return',
    fieldPolynomial='2*h^2-h+1',rank=rank,originalConstantInRowSpan=direct,
    originalDphysicalNumeratorInRowSpan=physical,originalDphysicalDenominatorImageNonzero=True,
    all35OriginalColumnProductsMultipliedBack=True,fullTwoComplexEmbeddingsCovered=True,
    directNonzeroTraceCount=sum(bool(z) for z in one_tag),physicalNonzeroTraceCount=sum(bool(z) for z in dtag),
    directTraceSHA256=hashlib.sha256(json.dumps([z.data() for z in one_tag]).encode()).hexdigest(),
    physicalTraceSHA256=hashlib.sha256(json.dumps([z.data() for z in dtag]).encode()).hexdigest(),
    fullQuadraticFiberExcluded=direct or physical,
    sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    inputSHA256=inputhash,peakRssKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,ordinaryISPClaim=False)
say(record)
signal.alarm(0)


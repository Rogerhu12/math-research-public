#!/usr/bin/env python3
"""New whole G36 weight curve: original six-generator Gram algebra over
QQ(k)[Q]/(G36(Q/k,k)/32). This is a NEW 36-column input, not a replay of the
old two-parameter C9 cofactor expansion. A rational-k unit certificate leaves
every scalar denominator-zero fibre OPEN. No lambda is inverted.
180 seconds / 4 GiB; immutable source, bounded output, no large cache.

C9 is paid by its OWN complete theorem:
results/R150-appendix-essential-four-unit-two-plus-one-plus-one-generic-LS-W-C9-complete-original-exclusion.md
(main blob d0f6ace7996b31717726676c19b681f03e57f1de), not by D27 or J19.
The original six rules are constructed afresh after imposing G36, following
the frozen C9 construction source a1a9d02a1602a47398ba9bbb9295b3da7d7ddd37.
Every inverse is actually multiplied back; all rational-k denominators are
retained in the exceptional cover, including norms of paid branch units.
"""
import json,time,hashlib,signal,resource,sys
from pathlib import Path
# Independent J19 complete leaf:
# results/R150-appendix-unit211-W-J19-entire-original-weight-curve-exclusion.md
from flint import fmpq_poly,fmpq
start=time.perf_counter()
signal.alarm(180)
resource.setrlimit(resource.RLIMIT_AS,(4*1024**3,4*1024**3))
def say(**r):
 r['seconds']=time.perf_counter()-start
 print(json.dumps(r,separators=(',',':')),flush=True)
def P0(v=()):
 if isinstance(v,fmpq_poly):return v
 if isinstance(v,(int,fmpq)):v=[v]
 return fmpq_poly([fmpq(c) for c in v])
z0=P0();o0=P0(1);kk0=P0([0,1])
def exact(a,b):
 q,r=divmod(a,b)
 assert not r and q*b==a
 return q
def monic(p):
 assert p
 return p/p[p.degree()]
def pc(p):return [str(c) for c in p.coeffs()]
def digest(obj):
 raw=json.dumps(obj,separators=(',',':')).encode()
 return dict(bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest())
def pprofile(p,exact_limit=8192):
 d=pc(p);r=dict(degree=int(p.degree()),**digest(d))
 raw=json.dumps(d,separators=(',',':')).encode()
 if len(raw)<=exact_limit:r['coefficients']=d
 try:
  arr=[]
  for c in p.coeffs():
   ss=str(c).split('/');nn=int(ss[0]);dd=int(ss[1]) if len(ss)==2 else 1
   arr.append(nn%1009*pow(dd%1009,-1,1009)%1009)
  bb=json.dumps(arr,separators=(',',':')).encode()
  r['mod1009DegreePreserved']=bool(p) and bool(arr[-1])
  r['mod1009Bytes']=len(bb);r['mod1009SHA256']=hashlib.sha256(bb).hexdigest()
  if len(bb)<=16384:r['mod1009']=arr
 except (ValueError,ZeroDivisionError):
  r['mod1009Integral']=False
 return r
class Rat:
 """Exact QQ(k), used only for six by six constant-ring inverse solves."""
 def __init__(self,n=0,d=None):
  if isinstance(n,Rat):self.n=n.n;self.d=n.d;return
  n=P0(n);d=o0 if d is None else P0(d);assert d
  if not n:self.n=z0;self.d=o0;return
  g=n.gcd(d);n=exact(n,g);d=exact(d,g);lc=d[d.degree()]
  self.n=n/lc;self.d=d/lc
 def __bool__(self):return bool(self.n)
 def __neg__(self):return Rat(-self.n,self.d)
 def __add__(self,v):
  v=Rat(v);g=self.d.gcd(v.d);a=exact(self.d,g);b=exact(v.d,g)
  return Rat(self.n*b+v.n*a,a*v.d)
 __radd__=__add__
 def __sub__(self,v):return self+-Rat(v)
 def __rsub__(self,v):return Rat(v)+-self
 def __mul__(self,v):
  v=Rat(v)
  g=self.n.gcd(v.d);h=v.n.gcd(self.d)
  return Rat(exact(self.n,g)*exact(v.n,h),exact(self.d,h)*exact(v.d,g))
 __rmul__=__mul__
 def __truediv__(self,v):
  v=Rat(v);assert v
  return self*Rat(v.d,v.n)
 def __eq__(self,v):
  v=Rat(v);return self.n*v.d==v.n*self.d

GDATA=[[0,0,"4096"],[0,1,"9216"],[0,2,"7680"],[0,3,"3072"],[0,4,"592"],[0,5,"24"],[0,6,"-10"],[0,7,"-1"],[1,1,"-6144"],[1,2,"-16128"],[1,3,"-14336"],[1,4,"-6048"],[1,5,"-1416"],[1,6,"-186"],[1,7,"-9"],[2,2,"512"],[2,3,"6016"],[2,4,"6560"],[2,5,"2528"],[2,6,"468"],[2,7,"50"],[2,8,"2"],[3,3,"1792"],[3,4,"832"],[3,5,"-832"],[3,6,"-392"],[3,7,"-50"],[3,8,"-2"],[4,4,"-256"],[4,5,"-544"],[4,6,"-24"],[4,7,"24"],[4,8,"4"],[5,5,"-192"],[5,7,"-8"],[6,6,"32"]]
assert len(GDATA)==36 and all(j>=i for i,j,c in GDATA)
gg=[P0() for _ in range(7)]
for i,j,c in GDATA:gg[i]+=fmpq(c)*kk0**(j-i)
assert gg[6]==32
gmonic=[c/32 for c in gg]
assert gmonic[6]==1
def reduce_numerator(cc):
 cc=list(cc)
 while len(cc)<6:cc.append(z0)
 for j in range(len(cc)-1,5,-1):
  lead=cc[j]
  if lead:
   for i in range(6):cc[j-6+i]=cc[j-6+i]-lead*gmonic[i]
  cc[j]=z0
 assert not any(cc[6:])
 return tuple(cc[:6])
def multiply_numerators(aa,bb):
 cc=[P0() for _ in range(11)]
 for i,a in enumerate(aa):
  if not a:continue
  for j,b in enumerate(bb):
   if b:cc[i+j]=cc[i+j]+a*b
 return reduce_numerator(cc)
def common_gcd(den,ns):
 g=den
 for n in ns:
  if n:g=g.gcd(n)
  if g.degree()==0:break
 return g
inverse_count=0;inverse_cache={};cover=o0;inverse_records=[]
def record_denominator(den):
 global cover
 if den.degree()<=0:return
 den=monic(den);cover=monic(cover*exact(den,cover.gcd(den)))
class Nonunit(Exception):
 def __init__(self,label):self.label=label
class A:
 """Whole rank-six algebra. Never assumed a field or reduced."""
 def __init__(self,v=0,den=None):
  if isinstance(v,A) and den is None:self.n=v.n;self.d=v.d;return
  if isinstance(v,Rat) and den is None:v,den=v.n,v.d
  if not isinstance(v,(tuple,list)):v=[P0(v)]
  else:v=[P0(c) for c in v]
  ns=reduce_numerator(v);dd=o0 if den is None else P0(den);assert dd
  if not any(ns):self.n=(z0,)*6;self.d=o0;return
  gc=common_gcd(dd,ns)
  if gc.degree()>0:
   ns=tuple(exact(n,gc) for n in ns);dd=exact(dd,gc)
  lc=dd[dd.degree()]
  self.n=tuple(n/lc for n in ns);self.d=dd/lc
 def __bool__(self):return any(self.n)
 @staticmethod
 def accepts(v):return isinstance(v,(A,Rat,fmpq_poly,fmpq,int,tuple,list))
 def __neg__(self):return A(tuple(-n for n in self.n),self.d)
 def __add__(self,v):
  if not self.accepts(v):return NotImplemented
  v=A(v)
  if not self:return v
  if not v:return self
  g=self.d.gcd(v.d);a=exact(self.d,g);b=exact(v.d,g)
  return A(tuple(x*b+y*a for x,y in zip(self.n,v.n)),a*v.d)
 __radd__=__add__
 def __sub__(self,v):
  if not self.accepts(v):return NotImplemented
  return self+-A(v)
 def __rsub__(self,v):
  if not self.accepts(v):return NotImplemented
  return A(v)+-self
 def __mul__(self,v):
  if not self.accepts(v):return NotImplemented
  v=A(v)
  if not self or not v:return A()
  g=common_gcd(v.d,self.n);h=common_gcd(self.d,v.n)
  an=tuple(exact(n,g) for n in self.n);bn=tuple(exact(n,h) for n in v.n)
  return A(multiply_numerators(an,bn),exact(self.d,h)*exact(v.d,g))
 __rmul__=__mul__
 def __eq__(self,v):
  if not self.accepts(v):return False
  v=A(v)
  return all(x*v.d==y*self.d for x,y in zip(self.n,v.n))
 def key(self):return tuple(str(n) for n in self.n)+(str(self.d),)
 def inverse(self,label='whole six-dimensional algebra inverse'):
  global inverse_count
  if not self:raise Nonunit(label+': zero')
  if self==1:return A(1)
  key=self.key()
  if key in inverse_cache:return inverse_cache[key]
  if not any(self.n[1:]):
   out=A(self.d,self.n[0])
  else:
   columns=[]
   for j in range(6):
    nn=[z0]*6;nn[j]=o0
    columns.append(multiply_numerators(self.n,nn))
   mm=[[columns[j][i] for j in range(6)]+[self.d if i==0 else z0] for i in range(6)]
   previous=o0
   for j in range(5):
    if not mm[j][j]:
     choices=[i for i in range(j+1,6) if mm[i][j]]
     if not choices:raise Nonunit(label+': multiplication norm identically zero')
     sw=choices[0];mm[j],mm[sw]=mm[sw],mm[j]
    pivot=mm[j][j]
    for i in range(j+1,6):
     for h in range(j+1,7):
      mm[i][h]=exact(mm[i][h]*pivot-mm[i][j]*mm[j][h],previous)
     mm[i][j]=z0
    previous=pivot
   if not mm[5][5]:raise Nonunit(label+': multiplication norm identically zero')
   sol=[Rat() for _ in range(6)]
   for i in range(5,-1,-1):
    sol[i]=(Rat(mm[i][6])-sum((Rat(mm[i][j])*sol[j] for j in range(i+1,6)),Rat()))/Rat(mm[i][i])
   den=o0
   for c0 in sol:den=monic(den*exact(c0.d,den.gcd(c0.d)))
   out=A([c0.n*exact(den,c0.d) for c0 in sol],den)
  assert self*out==1
  record_denominator(self.d);record_denominator(out.d)
  inverse_count+=1;inverse_cache[key]=out
  inverse_records.append(dict(label=label,inverseDenominatorDegree=int(out.d.degree()),
                              inverseDenominatorSHA256=digest(pc(out.d))['sha256'],
                              actualWholeSixComponentProductOne=True))
  return out
 def __truediv__(self,v):
  if not self.accepts(v):return NotImplemented
  return self*A(v).inverse()
 def __rtruediv__(self,v):
  if not self.accepts(v):return NotImplemented
  return A(v)*self.inverse()
 def __pow__(self,j):
  if j<0:return self.inverse()**(-j)
  out=A(1);v=self
  while j:
   if j&1:out=out*v
   j//=2
   if j:v=v*v
  return out
 def data(self):return dict(numerators=[pc(n) for n in self.n],denominator=pc(self.d))
 def complexity(self):
  return (max([int(n.degree()) for n in self.n]+[int(self.d.degree())]),
          sum(len(n.coeffs()) for n in self.n)+len(self.d.coeffs()))

k=A(kk0);Q=A([0,1]);e=Q/k
assert e*k==Q
assert sum((A(c)*Q**i for i,c in enumerate(gmonic)),A())==0
assert sum((A(fmpq(c))*e**i*k**j for i,j,c in GDATA),A())==0
say(stage='G36_original_Q_coordinate_whole_monic_six_algebra',
    gDegreesInK=[int(c.degree()) for c in gg],QDegree=6,
    originalELeading='32*k^6',originalQLeading=32,
    all36TermCoordinateProductsVerified=True,wholeSixAlgebraNotAssumedField=True,
    noUnpaidWeightOrLambdaRemoved=True)


class P:
 """Sparse polynomial in the actual finite variables x,y,t over A."""
 def __init__(self,v=0):
  if isinstance(v,P):self.c=v.c.copy();return
  if isinstance(v,dict):self.c={tuple(m):A(c) for m,c in v.items() if A(c)};return
  v=A(v);self.c={(0,0,0):v} if v else {}
 @staticmethod
 def accepts(v):return isinstance(v,P) or A.accepts(v)
 def __bool__(self):return bool(self.c)
 def __neg__(self):return P({m:-c for m,c in self.c.items()})
 def __add__(self,v):
  if not self.accepts(v):return NotImplemented
  v=P(v);out=self.c.copy()
  for m,c in v.c.items():out[m]=out.get(m,A())+c
  return P(out)
 __radd__=__add__
 def __sub__(self,v):
  if not self.accepts(v):return NotImplemented
  return self+-P(v)
 def __rsub__(self,v):
  if not self.accepts(v):return NotImplemented
  return P(v)+-self
 def __mul__(self,v):
  if not self.accepts(v):return NotImplemented
  v=P(v);out={}
  for m,a in self.c.items():
   for n,b in v.c.items():
    z=tuple(m[j]+n[j] for j in range(3))
    out[z]=out.get(z,A())+a*b
  return P(out)
 __rmul__=__mul__
 def __truediv__(self,v):return self*P(A(v).inverse('original weight polynomial denominator'))
 def __pow__(self,j):
  assert j>=0;out=P(1);v=self
  while j:
   if j&1:out=out*v
   j//=2
   if j:v=v*v
  return out
 def __eq__(self,v):
  if not self.accepts(v):return False
  return not (self-P(v))
 def coeff(self,m):return self.c.get(tuple(m),A())
 def degree(self):return max((sum(m) for m in self.c),default=-1)
 def data(self):return [[list(m),c.data()] for m,c in sorted(self.c.items())]
 def profile(self):
  return dict(monomials=len(self.c),degree=self.degree(),
              largestKDegree=max((c.complexity()[0] for c in self.c.values()),default=-1))
 def shift(self,mm):return P({tuple(m[j]+mm[j] for j in range(3)):c for m,c in self.c.items()})

u=e+1;V=u*k+2
ell=u*((k+2)**2-2*e*k)/(k*V)
dweight=1-Q;mweight=u-ell
bc=(ell*ell-mweight*mweight/dweight)/4
V2=2*u-ell*Q;T0=V2-2*u*u
P02=(2-3*u)*V2-Q*u+2*u**3
J=2*u*(1-u)+ell*Q;Phi=T0+4*u-4+Q;Pf=T0*(J-Q)
M=ell*V2-u*u
C9=4*e*e*k*k-e*(k**4+9*k**3+20*k*k+16*k)+k**3+10*k*k+24*k+16
J19=16*e**4*k**3-8*e**3*k**4-16*e**3*k**3-96*e**3*k*k-e*e*k**5-8*e*e*k**4+24*e*e*k**3+64*e*e*k*k+192*e*e*k-2*e*k**5-14*e*k**4-12*e*k**3-128*e-k**5-10*k**4-40*k**3-104*k*k-160*k-128
assert Phi*(J-2*u*Q)==Pf
assert 4*bc*dweight==M
assert (ell-u)*k*V==u*(k+2)*(2-Q)
assert Phi*V==-2*e*e*(k+4)
say(stage='G36_actual_original_weight_identities',wholeSixQAlgebra=True,
    scalarInverseCount=inverse_count,currentExceptionalKDegree=int(cover.degree()),
    C9IndependentTheorem='R150-appendix-essential-four-unit-two-plus-one-plus-one-generic-LS-W-C9-complete-original-exclusion.md',
    J19IndependentTheorem='R150-appendix-unit211-W-J19-entire-original-weight-curve-exclusion.md',
    noNormZeroFiberDiscarded=True)
xx=P({(1,0,0):1});yy=P({(0,1,0):1});tt=P({(0,0,1):1})
# Reuse ONLY the frozen original-construction prefix. No old head matrix,
# overlap, parameter pivot, cofactor, or failed 180-second gate is executed.
import io,contextlib,math
dep=Path(__file__).with_name('2026-11-27-unit211-generic-LS-W-C9-six-generator-original-parameter-cofactors-8542.py')
depraw=dep.read_bytes()
assert hashlib.sha256(depraw).hexdigest()=='10720660772a9a1252b905b1227b697e038d1b974b7e96ec30e485477b21d3f1'
oldtext=depraw.decode()
marker='\n# New mathematical input: all four original quadratics'
assert oldtext.count(marker)==1
prefix=oldtext[:oldtext.index(marker)]
old={'__file__':str(dep),'__name__':'__frozen_original_Gram_construction_only__'}
with contextlib.redirect_stdout(io.StringIO()):
 exec(compile(prefix,str(dep),'exec'),old)
signal.alarm(max(1,math.ceil(start+180-time.perf_counter())))
say(stage='G36_frozen_original_construction_prefix_only',
    sourceSHA256=hashlib.sha256(depraw).hexdigest(),
    prefixBytes=len(prefix.encode()),oldHeadOrParameterCofactorNotExecuted=True)

epowers={0:A(1)};kpowers={0:A(1)}
def epower(i):
 if i not in epowers:epowers[i]=e**i
 return epowers[i]
def kpower(j):
 if j not in kpowers:kpowers[j]=k**j
 return kpowers[j]
scalar_cache={}
def eval_scalar(po):
 key=str(po)
 if key in scalar_cache:return scalar_cache[key]
 out=A()
 for mm,cf in po.to_dict().items():
  assert all(mm[j]==0 for j in range(2,len(mm)))
  out+=A(cf)*epower(int(mm[0]))*kpower(int(mm[1]))
 scalar_cache[key]=out
 return out
def eval_polynomial(po):
 out={}
 for mm,cf in po.to_dict().items():
  assert all(mm[j]==0 for j in range(5,len(mm)))
  gg0=tuple(map(int,mm[2:5]))
  out[gg0]=out.get(gg0,A())+A(cf)*epower(int(mm[0]))*kpower(int(mm[1]))
 return P(out)
def eval_rational_polynomial(rr):
 iv=eval_scalar(rr.d).inverse('frozen original weight denominator')
 return eval_polynomial(rr.n)*iv
names=['E1','EBe','EBo','N1','NS','PS']
original=[eval_rational_polynomial(old['symbolic'][name]) for name in names]
cleared=[eval_polynomial(po) for po in old['cleared_polys']]
input_scales=[]
for rr in old['cleared_scales']:
 scale=eval_scalar(rr.n)*eval_scalar(rr.d).inverse('previously paid original row content')
 input_scales.append(scale)
for i in range(6):assert cleared[i]==input_scales[i]*original[i]
assert all(p.degree()<=2 for p in original[:4])
assert all(p.degree()<=3 for p in original[4:])
assert eval_rational_polynomial(old['symbolic']['ell'])==P(ell)
lam=eval_rational_polynomial(old['symbolic']['lam'])
T=eval_rational_polynomial(old['symbolic']['T'])
f=eval_rational_polynomial(old['symbolic']['f'])
assert all(p.degree()<=1 for p in [lam,T,f])
say(stage='G36_whole_Q_six_original_Gram_and_weighted_rows',
    originalE0N0P1AndWeightedMomentTracesReturnedByFrozenPrefix=True,
    allSixOriginalRows=[p.profile() for p in original],
    allSixPaidRowScalesActuallyMultipliedBack=True,
    dualProductSecondComponent='v0*w1+v1*w0',
    currentExceptionalKDegree=int(cover.degree()),noGeometryOrLambdaInverseUsed=True)


freemons=[(0,0,0),(1,0,0),(0,1,0),(0,0,1),(0,2,0),(0,1,1)]
qheads=[(2,0,0),(1,1,0),(1,0,1),(0,0,2)]
cubemons=[(0,3,0),(0,2,1)]
basis=[P({mm:1}) for mm in freemons]
variables=[xx,yy,tt]
def determinant(mm):
 n=len(mm)
 if n==0:return A(1)
 if n==1:return mm[0][0]
 ans=A()
 for j in range(n):
  if mm[0][j]:
   ans+=(-1)**j*mm[0][j]*determinant([row[:j]+row[j+1:] for row in mm[1:]])
 return ans
def verify_trace(pp,tag):
 assert sum((tag[i]*original[i] for i in range(6)),P())==pp
head=[[cleared[i].coeff(mm) for mm in qheads] for i in range(4)]
delta2=determinant(head)
ivdelta2=delta2.inverse('actual original four-quadratic head on whole G36')
inv=[]
for j in range(4):
 rr=[]
 for i in range(4):
  mm=[[head[r][c0] for c0 in range(4) if c0!=j] for r in range(4) if r!=i]
  rr.append((-1)**(i+j)*determinant(mm)*ivdelta2)
 inv.append(rr)
for i in range(4):
 for j in range(4):
  assert sum((inv[i][h]*head[h][j] for h in range(4)),A())==int(i==j)
rules=[];rule_tags=[]
for j in range(4):
 qj=sum((cleared[i]*inv[j][i] for i in range(4)),P())
 tag=[P(inv[j][i]*input_scales[i]) if i<4 else P() for i in range(6)]
 verify_trace(qj,tag)
 for i,mm in enumerate(qheads):assert qj.coeff(mm)==int(i==j)
 rules.append(qj);rule_tags.append(tag)
say(stage='G36_four_original_quadratic_rules',
    all16InverseEntriesAndFourOriginalTracesActuallyReturned=True,
    originalHeads=qheads,currentExceptionalKDegree=int(cover.degree()),
    allHeadNormZeroFibersRetained=True)
def order(mm):return (sum(mm),mm[0],mm[2],mm[1])
def reduce_original(pp):
 inp=P(pp);rem=P();tag=[P() for _ in range(6)]
 while pp:
  mm=max(pp.c,key=order);cf=pp.c[mm]
  inds=[j for j,h in enumerate(qheads) if all(h[i]<=mm[i] for i in range(3))]
  if not inds:
   term=P({mm:cf});rem+=term;pp-=term;continue
  j=inds[0];shift=tuple(mm[i]-qheads[j][i] for i in range(3))
  pp-=rules[j].shift(shift)*cf
  for h in range(6):
   if rule_tags[j][h]:tag[h]+=rule_tags[j][h].shift(shift)*cf
 verify_trace(inp-rem,tag)
 return rem,tag
specs=[(0,1,(0,1,0),(1,0,0)),(0,2,(0,0,1),(1,0,0)),
       (1,2,(0,0,1),(0,1,0)),(2,3,(0,0,1),(1,0,0))]
overlaps=[];overlap_tags=[]
for i,j,si,sj in specs:
 pp=rules[i].shift(si)-rules[j].shift(sj)
 tag=[rule_tags[i][h].shift(si)-rule_tags[j][h].shift(sj) for h in range(6)]
 verify_trace(pp,tag)
 rem,witness=reduce_original(pp)
 tag=[tag[h]-witness[h] for h in range(6)]
 verify_trace(rem,tag)
 assert all(mm in freemons+cubemons for mm in rem.c)
 overlaps.append(rem);overlap_tags.append(tag)
aa=overlaps[0].coeff(cubemons[0]);bb=overlaps[0].coeff(cubemons[1])
cc=overlaps[2].coeff(cubemons[0]);dd=overlaps[2].coeff(cubemons[1])
delta3=aa*dd-bb*cc
ivdelta3=delta3.inverse('actual original cubic pair 0,2; C9 independent complete theorem')
for alpha,beta in [(dd*ivdelta3,-bb*ivdelta3),(-cc*ivdelta3,aa*ivdelta3)]:
 pp=overlaps[0]*alpha+overlaps[2]*beta
 tag=[overlap_tags[0][h]*alpha+overlap_tags[2][h]*beta for h in range(6)]
 verify_trace(pp,tag);rules.append(pp);rule_tags.append(tag)
for j in range(2):
 for h,mm in enumerate(cubemons):assert rules[4+j].coeff(mm)==int(j==h)
 assert all(mm in freemons+cubemons for mm in rules[4+j].c)
qheads+=cubemons
say(stage='G36_six_original_monic_rules_whole_weight_algebra',
    basis=freemons,weightBasis='1,Q,Q^2,Q^3,Q^4,Q^5',
    scalarColumns=36,allSixOriginalTracesActuallyReturned=True,
    all16QuadraticAndFourCubicInverseProductsOne=True,
    scalarInverseCount=inverse_count,currentExceptionalKDegree=int(cover.degree()),
    C9NotInferredFromJ19OrD27=True,quotientNotAssumedFree=True)
def asrow(pp):
 assert all(mm in freemons for mm in pp.c)
 return [pp.coeff(mm) for mm in freemons]
def torowpoly(row):return sum((basis[j]*row[j] for j in range(6)),P())
matrices=[];errors=[]
for axis,var in enumerate(variables):
 mm=[];er=[]
 for bp in basis:
  inp=var*bp;rem,tag=reduce_original(inp)
  mm.append(asrow(rem));er.append(tag)
 matrices.append(mm);errors.append(er)
 say(stage='G36_actual_original_multiplication_axis',
     axis=axis,actualWholeWeightMonomialProducts=6,
     allOriginalTraceProductsReturned=True,noFreeAlgebraClaim=True)
rawrows=[];rawtags=[];rawlabels=[]
def append_row(row,tag,label):
 if not any(row):return
 verify_trace(torowpoly(row),tag)
 rawrows.append(row);rawtags.append(tag);rawlabels.append(label)
def append_original_polynomial(pp,tag,label):
 rem,witness=reduce_original(pp)
 newtag=[tag[h]-witness[h] for h in range(6)]
 append_row(asrow(rem),newtag,label)
# The two remaining original cubic overlaps.
for j in [1,3]:
 append_original_polynomial(overlaps[j],overlap_tags[j],'original_cubic_overlap_'+str(j))
# All five additional noncoprime critical pairs involving the two new cubic
# rules. These are actual same-point original rows; no matrix-freeness claim.
newpairs=[(1,4),(1,5),(2,5),(3,5),(4,5)]
for i,j in newpairs:
 lcm=tuple(max(qheads[i][h],qheads[j][h]) for h in range(3))
 si=tuple(lcm[h]-qheads[i][h] for h in range(3))
 sj=tuple(lcm[h]-qheads[j][h] for h in range(3))
 pp=rules[i].shift(si)-rules[j].shift(sj)
 tag=[rule_tags[i][h].shift(si)-rule_tags[j][h].shift(sj) for h in range(6)]
 append_original_polynomial(pp,tag,'original_new_quartic_pair_%d_%d'%(i,j))
for j in [4,5]:
 tag=[P(int(h==j)) for h in range(6)]
 append_original_polynomial(original[j],tag,names[j])
say(stage='G36_complete_new_original_six_column_rows',
    labels=rawlabels,rowCount=len(rawrows),scalarRows=6*len(rawrows),
    scalarColumns=36,allOriginalPolynomialTraceProductsActuallyReturned=True,
    all18OriginalMultiplicationsReturned=True,
    rowLargestKDegrees=[max(c.complexity()[0] for c in row) for row in rawrows],
    currentExceptionalKDegree=int(cover.degree()),genericConstantNotYetReturned=True)


echelon=[];echelon_tags=[];pivots=[];generic_nonunit_attempts=[]
column_order=[1,2,3,4,5,0]
def clean_tag(tag):return {i:c0 for i,c0 in tag.items() if c0}
def add_to_span(ri):
 row=rawrows[ri][:];tag={ri:A(1)}
 for brow,pv,bt in zip(echelon,pivots,echelon_tags):
  cc0=row[pv]
  if not cc0:continue
  row=[v-cc0*w for v,w in zip(row,brow)]
  for j,cf in bt.items():tag[j]=tag.get(j,A())-cc0*cf
 if not any(row):return False
 options=[j for j in column_order if row[j]]
 # Prefer a small actual unit, without declaring nonzero elements to be units.
 options.sort(key=lambda j:(row[j].complexity(),column_order.index(j)))
 found=None
 for pv in options:
  try:
   iv=row[pv].inverse('new G36 actual six-column pivot rank '+str(len(pivots)))
   found=(pv,iv);break
  except Nonunit as ex:
   generic_nonunit_attempts.append(dict(row=ri,column=pv,reason=ex.label))
 if found is None:
  say(stage='G36_actual_nonunit_row_retained',row=ri,label=rawlabels[ri],
      noComponentDiscarded=True,noRankClaimFromNonzeroPivot=True)
  return False
 pv,iv=found
 row=[cf*iv for cf in row];tag=clean_tag({j:cf*iv for j,cf in tag.items()})
 assert row[pv]==1 and all(not row[j] for j in pivots)
 # This checked row identity is over the ENTIRE degree-six weight algebra.
 for j in range(6):
  assert sum((cf*rawrows[i][j] for i,cf in tag.items()),A())==row[j]
 echelon.append(row);echelon_tags.append(tag);pivots.append(pv)
 say(stage='G36_actual_whole_algebra_original_pivot',rank=len(pivots),
     sourceRow=ri,label=rawlabels[ri],pivotColumn=pv,
     allSixOriginalRowProductsActuallyReturned=True,
     equivalentScalarColumns=36,currentExceptionalKDegree=int(cover.degree()))
 return True
def constant_target():
 target=[A(1)]+[A() for _ in range(5)]
 rem=target[:];combo={}
 for brow,pv,bt in zip(echelon,pivots,echelon_tags):
  cc0=rem[pv]
  if not cc0:continue
  rem=[v-cc0*w for v,w in zip(rem,brow)]
  for j,cf in bt.items():combo[j]=combo.get(j,A())+cc0*cf
 return not any(rem),clean_tag(combo),rem
initial_count=len(rawrows)
for ri in range(initial_count):
 add_to_span(ri)
 if len(pivots)==6:break
returned,combo,remaining=constant_target()
# Only if needed, genuinely new same-point multiples of the weighted rows
# and the smallest remaining overlap are added. No failed matrix is rerun.
if not returned:
 sources=[i for i,label in enumerate(rawlabels[:initial_count]) if label in ['NS','PS']]
 others=[i for i in range(initial_count) if i not in sources]
 if others:
  sources.append(min(others,key=lambda i:max(cf.complexity()[0] for cf in rawrows[i])))
 for src in sources:
  for axis,var in enumerate(variables):
   row=[sum((rawrows[src][i]*matrices[axis][i][j] for i in range(6)),A()) for j in range(6)]
   tag=[var*rawtags[src][h]-sum((errors[axis][i][h]*rawrows[src][i] for i in range(6)),P()) for h in range(6)]
   oldcount=len(rawrows)
   append_row(row,tag,rawlabels[src]+'*'+'xyt'[axis])
   if len(rawrows)>oldcount:add_to_span(oldcount)
   returned,combo,remaining=constant_target()
   if returned:break
  if returned:break
if returned:
 for j in range(6):
  prod=sum((cf*rawrows[i][j] for i,cf in combo.items()),A())
  assert prod==int(j==0)
  for h in range(6):
   assert prod.n[h]==(prod.d if j==0 and h==0 else z0)
 # Each original trace was already multiplied back when its row was created.
 # Compose those ACTUAL identities with this ACTUAL all-column certificate;
 # expansion of their potentially enormous polynomial coefficients is neither
 # assumed nor required. This is a complete original ideal certificate.
 for cf in combo.values():record_denominator(cf.d)
 say(stage='G36_actual_generic_original_constant_one',
     allSixAlgebraColumnsAndAll36ScalarComponentsReturned=True,
     allUsedOriginalPolynomialTraceIdentitiesPreviouslyActuallyReturned=True,
     actualComposedOriginalIdealCertificate=True,
     usedRows=[dict(index=i,label=rawlabels[i]) for i in sorted(combo)],
     weightAlgebraNotAssumedField=True,geometryQuotientNotAssumedFree=True,
     noPhysicalDOrLambdaInverseUsed=True,
     genericExclusionOnly=True,wholeG36Excluded=False,
     currentExceptionalKDegree=int(cover.degree()))
else:
 say(stage='G36_original_span_not_yet_constant_one',rank=len(pivots),
     remainingTargetColumns=[j for j,c0 in enumerate(remaining) if c0],
     allNonunitComponentsAndScalarDenominatorFibersRetained=True,
     genericExclusionNotClaimed=True,wholeG36Excluded=False)

# All arithmetic and original-trace coefficients live in QQ[k,1/cover].
# Keep EVERY zero of this polynomial, except the original physical k=0.
# In particular a norm of a paid branch factor is never automatically paid.
assert cover
gg0=cover.gcd(cover.derivative())
sf=monic(exact(cover,gg0))
assert sf*gg0/gg0[gg0.degree()]==cover/cover[cover.degree()]
removed_k=0
while sf.degree()>0 and not sf[0]:
 before=sf;sf=exact(sf,kk0);assert sf*kk0==before;removed_k+=1
sf=monic(sf)
say(stage='G36_complete_univariate_exception_cover',
    genericOriginalConstantOneReturned=returned,
    finiteCoverNeededOnlyIfGenericReturned=True,
    wholeSixQFibersAboveEveryRemainingKRootStillOpen=True,
    onlyPhysicalKZeroRemoved=removed_k,
    noNormZeroOrOtherKLeadingZeroRemoved=True,
    noLambdaDenominatorPresent=True,
    cover=pprofile(sf),factorizationNotAttempted=True,
    wholeG36Excluded=False)

# Preserve the exact, newly computed finite parameter cover for subsequent
# finite-fibre returns. This output is NOT a claim that sf (rather than a
# suitable power) itself lies in the original ideal.
import base64,zlib
cover_raw=json.dumps(pc(sf),separators=(',',':')).encode()
cover_compressed=zlib.compress(cover_raw,9)
cover_b64=base64.b64encode(cover_compressed).decode('ascii')
assert zlib.decompress(base64.b64decode(cover_b64))==cover_raw
cover_chunks=[cover_b64[i:i+80000] for i in range(0,len(cover_b64),80000)]
say(stage='G36_exact_exception_cover_encoding',
    format='canonical ascending QQ coefficient strings, JSON, zlib, base64',
    exactRawBytes=len(cover_raw),exactRawSHA256=hashlib.sha256(cover_raw).hexdigest(),
    compressedBytes=len(cover_compressed),base64Characters=len(cover_b64),
    chunks=len(cover_chunks),maximumChunkCharacters=80000,
    completeCompressionRoundTripVerified=True,
    genericLocalizationCertificateOnly=True,noFirstPowerIdealClaim=True)
for i,chunk in enumerate(cover_chunks):
 say(stage='G36_exact_exception_cover_chunk',index=i,total=len(cover_chunks),data=chunk)

cert_hash=hashlib.sha256();cert_bytes=0
def hash_piece(obj):
 global cert_bytes
 bb=json.dumps(obj,separators=(',',':')).encode()
 cert_hash.update(bb);cert_hash.update(b'\n');cert_bytes+=len(bb)+1
hash_piece(dict(G36=GDATA,basis=freemons,originalSourceSHA256=hashlib.sha256(depraw).hexdigest()))
for i in (sorted(combo) if returned else []):
 hash_piece(dict(row=i,label=rawlabels[i],coefficient=combo[i].data()))
 for h in range(6):hash_piece(dict(original=h,trace=rawtags[i][h].data()))
hash_piece(dict(cover=pc(sf),rank=len(pivots),pivots=pivots,returned=returned))
say(stage='G36_new_original_six_by_six_degree_weight_return_complete',
    sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    originalConstructionPrefixSHA256=hashlib.sha256(prefix.encode()).hexdigest(),
    originalNecessaryRows=len(rawrows),initialNecessaryRows=initial_count,
    scalarColumns=36,rankOverWholeWeightAlgebra=len(pivots),
    actualGenericOriginalConstantOneReturned=returned,
    actualComposedCertificateSHA256=cert_hash.hexdigest(),
    actualComposedCertificateBytes=cert_bytes,
    actualInverseProducts=inverse_count,
    inverseReceiptDigest=digest(inverse_records),
    retainedNonunitAttempts=generic_nonunit_attempts,
    exceptionalKCoverDegree=int(sf.degree()),
    exceptionalKCoverSHA256=digest(pc(sf))['sha256'],
    noLargeCoefficientCacheWritten=True,
    noOldParameterCofactorGateRerun=True,
    noMultivariateModularOrGcdEmptinessInference=True,
    wholeG36Excluded=False,wholeWExcluded=False,ordinaryISPClaim=False,
    peakRssKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
signal.alarm(0)

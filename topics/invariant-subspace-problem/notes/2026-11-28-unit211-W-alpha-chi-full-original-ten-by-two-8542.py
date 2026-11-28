#!/usr/bin/env python3
"""NEW whole W: polynomial alpha,chi original I6/ten-by-two.
Use the proved pure-WEIGHT-unit coordinate map, not the prior gamma graph.
No geometry denominator is inverted. Rebuild only native mean six-rule
definitions (14656 bytes), not old multiplication/cofactor tails.
New highest-alpha cube gives the actual monic alpha^2; native NS/PS
remainders then give FIVE alpha quadratics and their exact 10x2 ideal.
Only three fixed new original two-row scalar targets. 180s/4GiB.
"""
import json,time,hashlib,signal,resource,contextlib,io,math
from pathlib import Path
from flint import fmpq,fmpq_mpoly_ctx
START=time.perf_counter();DEADLINE=START+180
signal.setitimer(signal.ITIMER_REAL,180)
resource.setrlimit(resource.RLIMIT_AS,(4*1024**3,4*1024**3))
def say(**kw):
 kw['seconds']=time.perf_counter()-START
 print(json.dumps(kw,separators=(',',':')),flush=True)
def digest(obj):
 raw=json.dumps(obj,separators=(',',':')).encode()
 return dict(bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest())
ctx=fmpq_mpoly_ctx.get(('e','k','chi','alpha'),'lex');ep,kp,cp,ap=ctx.gens()
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


e,k,chi,alpha=R(ep),R(kp),R(cp),R(ap)
u=e+1;Q=e*k;Vbar=u*k+2
l=u*((k+2)**2-2*e*k)/(k*Vbar);delta=1-Q;m=u-l
Uhat=u-l*Q;V2=2*u-l*Q;T0=V2-2*u*u
M=l*V2-u*u;bc=M/(4*delta)
Z=u*(u-1)+l*(1-l)*Q;C=u-1+(1-l)*Q
Rw=2*u*(1-u)-u*Q+(2*u-1)*l*Q
Hold=4*ep*kp-kp*kp-4*kp-8
assert Rw==-u*e*e*R(Hold)/Vbar
assert Uhat*Z-M*C==-m*Rw and 2*u*Z+m*T0==-l*Rw
tt=-alpha*chi/(m*Rw)-2*delta*l/m
f=u+(alpha+Uhat*tt)/(4*delta)
V=f+(M-Z-chi)*tt/(4*delta)
A1=(chi+Z)*tt/(2*delta)
W1=(T0+4*u*f)/2
xx=(Uhat*V-m*W1)/M;yy=(l*W1-u*V)/M
assert A1==2*f-2*V+2*bc*tt
assert 4*delta*(f-u)-Uhat*tt==alpha
assert 2*delta*A1==(chi+Z)*tt
assert l*xx+m*yy==V and u*xx+Uhat*yy==W1
Rtrue=4*(f-u)*(V-f)+bc*tt*tt+tt*(4*bc*u-l*V+m*(T0+4*u*f-2*V)/(2*delta))
assert not Rtrue
P02=(2-3*u)*V2-Q*u+2*u**3
W2=V2*xx+(2*u-u*Q-l*Q)*yy
lam=(W2-u*T0-(V2+2*u*u)*f+bc*Q*tt)/P02
J=2*u*(1-u)+l*Q;Phi=T0+4*u-4+Q;Pf=T0*(J-Q)
G=lam*P02-(1-u)*T0
Tr=(G*T0-Pf*f-Phi*bc*Q*tt)/(Q*P02)-l
J19=(16*ep**4*kp**3-8*ep**3*kp**4-16*ep**3*kp**3-96*ep**3*kp**2
 -ep**2*kp**5-8*ep**2*kp**4+24*ep**2*kp**3+64*ep**2*kp**2+192*ep**2*kp
 -2*ep*kp**5-14*ep*kp**4-12*ep*kp**3-128*ep
 -kp**5-10*kp**4-40*kp**3-104*kp**2-160*kp-128)
C9=4*ep*ep*kp*kp-ep*(kp**4+9*kp**3+20*kp*kp+16*kp)+kp**3+10*kp*kp+24*kp+16
atoms=[('e',ep),('k',kp),('u',ep+1),('delta',ep*kp-1),
 ('Vbar',(ep+1)*kp+2),('Phi_k_plus_four',kp+4),('P02',P02.n),
 ('M',M.n),('whole_k_plus_one',kp+1),('whole_H_old',Hold),
 ('whole_equal_weights_k_plus_two',kp+2),('whole_ell_zero',l.n),
 ('whole_equal_weights_m',m.n),('Rw_paid_by_H_identity',Rw.n),
 ('whole_original_J19',J19),('whole_original_C9',C9)]
divisions=0;identity_products=10
def dex(a,b):
 global divisions
 q,r=divmod(a,b);assert not r and q*b==a
 divisions+=1;return q
def weight(p):return all(int(mm[2])==int(mm[3])==0 for mm in p.to_dict())
def strip(p):
 before=p;removed=oo;hist=[]
 if not p:return p,removed,hist
 for name,atom in atoms:
  n=0
  while True:
   g=p.gcd(atom)
   if int(g.total_degree())==0:break
   p=dex(p,g);removed*=g;n+=1
  if n:hist.append([name,n])
 assert p*removed==before
 return p,removed,hist
def paid(p):
 assert weight(p)
 rest,_,_=strip(p);assert rest and int(rest.total_degree())==0
def profile(p):
 if not p:return dict(zero=True,degrees_e_k_chi_alpha=[-1]*4,terms=0)
 dat=[[list(map(int,mm)),str(v)] for mm,v in sorted(p.to_dict().items())]
 return dict(zero=False,degrees_e_k_chi_alpha=list(map(int,p.degrees())),
  totalDegree=int(p.total_degree()),terms=len(dat),**digest(dat))
def ac(v,i):
 v=R(v);paid(v.d)
 po=zz
 for mm,c in v.n.to_dict().items():
  ee,kk,cc,aa=map(int,mm)
  if aa==i:po+=c*ep**ee*kp**kk*cp**cc
 return R(po,v.d)
def adeg(v):return int(v.n.degrees()[3]) if v else -1
for value in [tt,f,V,A1,xx,yy,lam,Tr]:
 paid(value.d);assert adeg(value)<=1
say(stage='new_entire_W_polynomial_alpha_chi_original_coordinates',
 allCorrectRAndA1AndWeightedReconstructionIdentitiesReturned=True,
 onlyPreviouslyPaidWeightDenominators=True,
 noGammaAlphaOrChiHeadInverted=True,
 inverseUsesOnlyPreviouslyPaidT=True,
 alphaZeroStillIncludedByIdentities=True,
 coordinateDegrees={name:list(map(int,v.n.degrees()[2:])) for name,v in [('t',tt),('f',f),('V',V),('A1',A1),('x',xx),('y',yy)]})
path=Path(__file__).with_name('2026-11-27-unit211-generic-LS-W-C9-six-generator-original-parameter-cofactors-8542.py')
raw=path.read_bytes()
assert hashlib.sha256(raw).hexdigest()=='10720660772a9a1252b905b1227b697e038d1b974b7e96ec30e485477b21d3f1'
marker=b'\nmatrices=[];errors=[]';assert raw.count(marker)==1
prefix=raw.split(marker)[0]
assert len(prefix)==14656 and hashlib.sha256(prefix).hexdigest()=='88b8e2f49f925e51c0b940f929efb502ced9ed358228a605fea3755d9cdefff8'
ns={'__file__':str(path),'__name__':'new_alpha_chi_native_mean_definitions'}
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
  exec(compile(prefix,str(path)+'#definitions_only','exec'),ns)
finally:
 signal.alarm=old_alarm;signal.setitimer=old_timer
 old_timer(signal.ITIMER_REAL,max(.001,DEADLINE-time.perf_counter()))
NR=ns['R'];oldoriginal=ns['original']
assert ns['freemons']==[(0,0,0),(1,0,0),(0,1,0),(0,0,1),(0,2,0),(0,1,1)]
assert all(not tag[j] for tag in ns['tags'] for j in [4,5])
def embed(p):
 ans=zz
 for mm,c in p.to_dict().items():
  assert all(int(mm[j])==0 for j in range(2,8))
  ans+=c*ep**int(mm[0])*kp**int(mm[1])
 return ans
def pull(v,degree_limit=3):
 v=NR(v);den=embed(v.d);paid(den);groups={}
 for mm,c in v.n.to_dict().items():
  assert all(int(mm[j])==0 for j in range(5,8))
  geom=tuple(map(int,mm[2:5]));assert sum(geom)<=degree_limit
  groups[geom]=groups.get(geom,zz)+c*ep**int(mm[0])*kp**int(mm[1])
 out=R()
 for geom,po in groups.items():
  term=R(po,den)
  for var,power in zip([xx,yy,tt],geom):term=term*var**power
  out+=term
 paid(out.d);return out
for po in [ns['delta2'],ns['delta3'].n,ns['delta3'].d]:paid(embed(po))
for rule,tag in zip(ns['q'],ns['tags']):
 for cf in ns['coeffmap'](rule).values():paid(embed(cf.d))
 for cf in tag:paid(embed(cf.d))
for key,value in [('u',u),('Q',Q),('l',l),('Delta',delta),('P02',P02),('f',f),('lam',lam),('T',Tr)]:
 assert pull(ns[key],1)==value;identity_products+=1
four=[pull(v,2) for v in oldoriginal[:4]]
E1,EBe,EBo,N1=four
EW=l*EBe+m*EBo
assert E1==EW
rawthree=[EW,EBo,N1]
for v in rawthree:assert adeg(v)<=2;paid(v.d)
identity_products+=1
say(stage='new_alpha_chi_same_original_three_quadratics',
 originalE1EqualsEWReturned=True,fullTrueDualGermInputs=True,
 profiles=[profile(v.n) for v in rawthree],
 allCoefficientDenominatorsPurePaidWeights=True,
 noOldGammaRowsOrScalarsRebuilt=True)
# New homogeneous alpha-direction identity, not the old f^3 calculation.
oldUhat=ns['u']-ns['l']*ns['Q']
oldL=(2*ns['Delta']/ns['u'])*(ns['u']*ns['x0']+oldUhat*ns['x1'])-oldUhat*ns['t']
oldrow,oldtag=ns['reduce_six'](oldL**3)
assert not oldtag[4] and not oldtag[5]
oldrem=sum((oldrow[j]*ns['basis'][j] for j in range(6)),NR())
assert oldL**3-oldrem==sum((-oldtag[j]*oldoriginal[j] for j in range(4)),NR())
directions=[ac(v,1) for v in [xx,yy,tt]]
assert (2*delta/u)*(u*directions[0]+Uhat*directions[1])-Uhat*directions[2]==R(1)
hco=[]
for j in range(4):
 tag=-oldtag[j];den=embed(tag.d);paid(den);v=R()
 for mm,c in tag.n.to_dict().items():
  assert all(int(mm[z])==0 for z in range(5,8))
  geo=tuple(map(int,mm[2:5]));assert sum(geo)<=1
  if sum(geo)!=1:continue
  v+=R(c*ep**int(mm[0])*kp**int(mm[1]),den)*directions[geo.index(1)]
 paid(v.d);assert all(int(mm[3])==0 for mm in v.n.to_dict());hco.append(v)
cofs=[hco[0]+hco[1]/l,hco[2]-m*hco[1]/l,hco[3]]
heads=[ac(v,2) for v in rawthree]
assert sum((cofs[j]*heads[j] for j in range(3)),R())==R(1)
qalpha=sum((cofs[j]*rawthree[j] for j in range(3)),R())
qc=[ac(qalpha,j) for j in range(3)]
assert qc[2]==R(1) and adeg(qalpha)==2
assert sum((qc[j]*alpha**j for j in range(3)),R())==qalpha
for c in cofs+qc:paid(c.d)
identity_products+=4
say(stage='new_alpha_chi_actual_global_monic_two',
 sameAlphaHighestDirectionOne=True,
 allThreeActualQuadraticHeadsCombinedToOne=True,
 originalHomogeneousCubeReturned=True,
 originalMonicCombinationReturned=True,
 coefficients=[dict(numerator=profile(c.n),denominator=profile(c.d)) for c in qc],
 allDenominatorsPurePaidWeightUnits=True,
 noNewChiHeadOrGammaOpen=True)
newfive=rawthree[:]
basis=[R(1),xx,yy,tt,yy*yy,yy*tt]
for gen in [4,5]:
 row,tag=ns['reduce_six'](oldoriginal[gen],[NR(int(i==gen)) for i in range(6)])
 assert tag[4]==NR(int(gen==4)) and tag[5]==NR(int(gen==5))
 rem=sum((pull(row[j],0)*basis[j] for j in range(6)),R())
 assert adeg(rem)<=2
 original_cubic=pull(oldoriginal[gen],3)
 mt=[pull(tag[j],1) for j in range(4)]
 combined=[mt[0]+mt[1]/l,mt[2]-m*mt[1]/l,mt[3]]
 assert rem==original_cubic+sum((combined[j]*rawthree[j] for j in range(3)),R())
 for c in combined:paid(c.d)
 newfive.append(rem);identity_products+=1
 say(stage='new_alpha_chi_native_original_cubic_quadratic_return',
  name=['NS','PS'][gen-4],originalCubicCoefficientOne=True,
  completeOriginalThreeMeanTagIdentityReturned=True,
  numerator=profile(rem.n),denominator=profile(rem.d),
  noGeometryDenominator=True)
assert len(newfive)==5
polyrows=[];origin_rows=[];scales=[]
def clear_row(pair):
 den=oo
 for cf in pair:
  paid(cf.d);den=dex(den,den.gcd(cf.d))*cf.d
 paid(den);cols=[cf.n*dex(den,cf.d) for cf in pair]
 removed=oo;hist=[]
 for name,atom in atoms:
  n=0
  while any(cols):
   g=atom
   for col in cols:g=g.gcd(col)
   if int(g.total_degree())==0:break
   cols=[dex(col,g) for col in cols];removed*=g;n+=1
  if n:hist.append([name,n])
 if any(cols):
  c=next(v for v in cols if v).coefficient(0)
  cols=[v/c for v in cols];removed*=c
 scale=R(removed,den);paid(scale.n);paid(scale.d)
 for col,cf in zip(cols,pair):assert R(col)*scale==cf
 return cols,scale,hist
for j,value in enumerate(newfive):
 head=ac(value,2);line=value-head*qalpha
 assert adeg(line)<=1
 pair=[ac(line,0),ac(line,1)]
 assert pair[0]+pair[1]*alpha==value-head*qalpha
 multiple=[-pair[1]*qc[0],pair[0]-pair[1]*qc[1]]
 assert multiple[0]+multiple[1]*alpha==alpha*line-pair[1]*qalpha
 identity_products+=2
 for axis,rr in enumerate([pair,multiple]):
  for cf in rr:
   assert all(int(mm[3])==0 for mm in cf.n.to_dict());paid(cf.d)
  cols,scale,hist=clear_row(rr)
  polyrows.append(cols);origin_rows.append(rr);scales.append(scale)
  say(stage='new_alpha_chi_original_two_column_row',
   original=['EW','EBo','N1','nativeNS','nativePS'][j],
   alphaMultiple=axis,columns=[profile(c) for c in cols],
   onlyPaidWeightContentRemoved=hist,
   completeOriginalShortDivisionAndScalingReturned=True)
assert len(polyrows)==10
say(stage='new_entire_W_alpha_chi_exact_I6_ten_by_two',
 rows=10,columns=['1','alpha'],
 fullI6EqualityViaMonicQAndFiveOriginalLinears=True,
 allOriginalNativeNSPSAndMeanRelationsRetained=True,
 allNewCoefficientDenominatorsPureWeightUnits=True,
 noNewChiOrAlphaHeadInverted=True,
 furtherPhysicalTAndDLocalizationsNotClaimedFiniteFree=True)
targets=[]
for i,j in [(6,8),(6,7),(0,6)]:
 left,right=polyrows[i],polyrows[j]
 mu=[right[1],-left[1]]
 g=mu[0].gcd(mu[1])
 if not g:
  say(stage='new_alpha_chi_fixed_scalar_zero',rows=[i,j],reason='both actual multipliers zero')
  continue
 mu=[dex(p,g) for p in mu]
 vals=[mu[0]*left[c]+mu[1]*right[c] for c in range(2)]
 assert not vals[1]
 assert mu[0]*(left[0]+left[1]*ap)+mu[1]*(right[0]+right[1]*ap)==vals[0]
 target=vals[0];core,removed,hist=strip(target)
 if core:
  c=core.coefficient(0);core/=c;removed*=c
 assert core*removed==target
 rec=dict(rows=[i,j],actualCommonMultiplier=profile(g),
  originalScalar=profile(target),retainedNecessaryPolynomial=profile(core),
  onlyPaidWeightRemoval=hist,completeTwoColumnAndPolynomialIdentityReturned=True,
  unpaidCommonFactorZeroFibersPreserved=True)
 targets.append(rec);identity_products+=2
 say(stage='new_alpha_chi_fixed_original_scalar',**rec)
say(stage='new_alpha_chi_full_original_two_column_inputs_complete',
 sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 exactOriginalI6TenByTwo=True,
 newActualPolynomialDivisionProducts=divisions,
 newActualOriginalIdentityProducts=identity_products,
 nonzeroNecessaryScalars=sum(not r['retainedNecessaryPolynomial']['zero'] for r in targets),
 wholeCurrentWExcluded=any(not r['retainedNecessaryPolynomial']['zero'] and r['retainedNecessaryPolynomial']['totalDegree']==0 for r in targets),
 noNewUnitAssumed=True,noOldFrozenOrCompletedTargetReplayed=True,
 noCoefficientPayloadOrMatrixCacheSaved=True,
 peakRSSKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
 ordinaryISPClaim=False)

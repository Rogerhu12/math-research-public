#!/usr/bin/env python3
"""NEW whole-W original-value quartics in the global physical-lambda
three-generator model. Use the actual monic value T^4 and the T^3
remainder, with NO division by 3-2lambda, D, or any value coefficient.
Return the three rows N1,qT4,rT3 to the SAME original eight equations.
Their fixed 3x3 constant cofactor is a lambda polynomial of degree <=8.
Divide it only by the already proved monic lambda six, obtaining a new
necessary lambda polynomial of degree <=5, with an exact division return.
No old 12-resultant or 18-row generic module is executed. 180s / 4GiB.
All unproved content/head zero fibres remain. Source/definitions/hash only.
"""
import json,time,hashlib,signal,resource,contextlib,io,math
from pathlib import Path
from flint import fmpq
started=time.perf_counter();deadline=started+180
signal.alarm(180);resource.setrlimit(resource.RLIMIT_AS,(4*1024**3,4*1024**3))
def say(**d):
 d['seconds']=time.perf_counter()-started
 print(json.dumps(d,separators=(',',':')),flush=True)
def digest(o):
 b=json.dumps(o,separators=(',',':')).encode()
 return dict(bytes=len(b),sha256=hashlib.sha256(b).hexdigest())
def frozen_prefix(name,sha,marker,size,phash,label):
 path=Path(__file__).with_name(name);raw=path.read_bytes()
 assert hashlib.sha256(raw).hexdigest()==sha and raw.count(marker)==1
 prefix=raw.split(marker)[0]
 assert len(prefix)==size and hashlib.sha256(prefix).hexdigest()==phash
 ns={'__file__':str(path),'__name__':label}
 with contextlib.redirect_stdout(io.StringIO()):
  exec(compile(prefix,str(path)+'#new_value_input_definitions','exec'),ns)
 signal.alarm(max(1,math.ceil(deadline-time.perf_counter())))
 return ns
tri=frozen_prefix(
 '2026-11-28-unit211-W-K7-open-physical-lambda-original-three-column-projection-binding-corrected-8542.py',
 '7cf3ff802cdf8166e3fb96f3ea806b81b83570f9200d10fad11caa13862f2c3f',
 b'\nrows=[];rowtags=[];labels=[]',5833,
 '8ea50cb422b81b5976bbb132e01809135ebbaedc06d545bcdb0c741fec4e3ff4',
 'only_original_three_mean_rules_and_six_products')
R=tri['R'];ctx=tri['ctx'];zero=tri['zero'];one=tri['one']
ep,kp,xp,yp,Lp,Tformal=ctx.gens()[:6]
xx,yy,L=tri['xx'],tri['yy'],tri['L'];TT=R(Tformal)
phys=tri['ns'];old=phys['ns'];pay=tri['pay'];strip=tri['strip']
u,Q,ell,J,Phi=[phys[z] for z in ['u','Q','ell','J','Phi']]
M=old['M'];d=1-Q;m=u-ell
T=phys['subst'](old['symbolic']['T'],[xx,yy,phys['tnew']])
assert phys['subst'](T,[xx,yy,phys['old_lambda']])==old['symbolic']['T']
for atom in [m,u,Q,ell,d,M,Phi]:
 pay(atom.n);pay(atom.d)
Al=2*L*L-2*L+1;Bl=4*L**3-6*L*L+3*L-1
D=ell*Al-TT*TT;Kval=ell**2*Bl-3*ell*TT*Al+2*TT**3
c=3-2*L;Ast=4*u*Q-J;Cst=Ast*m*m+J*d*ell*ell
ad=M*ell*ell*Q*(3-4*L)+M*Ast*TT*TT+2*M*u*Q*c*ell*TT+Cst*D
bd=2*M*m*(Ast*TT+u*Q*c*ell)
R4=M*ad*ad-D*bd*bd;C4=2*m*D*ad+Kval*bd
def Tcoeff(rr):
 rr=R(rr);pay(rr.d);out={}
 for mm,cc in rr.n.to_dict().items():
  assert mm[2]==mm[3]==mm[6]==mm[7]==0
  j=int(mm[5])
  out[j]=out.get(j,zero)+cc*ep**int(mm[0])*kp**int(mm[1])*Lp**int(mm[4])
 return {j:R(v,rr.d) for j,v in out.items() if v}
c4c=Tcoeff(C4);r4c=Tcoeff(R4)
head=8*m*u*Q*ell*ell*d;pay(head.n);pay(head.d)
assert max(c4c)==4 and c4c[4]==head
qT=C4/head
rT=R4-r4c.get(4,R())*qT
rtc=Tcoeff(rT)
assert max(rtc,default=-1)<=3
assert rtc.get(3,R())==8*M*M*u*Q*ell**3*d*(3-2*L)*(2*u*Q-J)
assert qT*head==C4 and rT+r4c.get(4,R())*qT==R4
def evaluate_T(pp):
 cc=Tcoeff(pp);pw=[R(1)]
 for j in range(max(cc,default=0)):pw.append(pw[-1]*T)
 return sum((v*pw[j] for j,v in cc.items()),R())
qvalue=evaluate_T(qT);rvalue=evaluate_T(rT)
original8=tri['original']+[qvalue,rvalue]
basis=tri['basis']
def verify8(p,tag):
 assert sum((tag[g]*original8[g] for g in range(8)),R())==p
def enc(p):
 return [[[int(i) for i in mm],str(c)] for mm,c in sorted(p.to_dict().items())]
def profile(p):
 if not p:return dict(zero=True,terms=0)
 return dict(degrees=list(map(int,p.degrees()[:6])),
 totalDegree=int(p.total_degree()),terms=len(p.to_dict()),**digest(enc(p)))
def clear_row(row,tag):
 den=one
 for cf in row:
  pay(cf.d);gg=den.gcd(cf.d);qq=cf.d/gg
  assert gg*qq==cf.d;den*=qq
 pay(den)
 out=[]
 for cf in row:
  qq=den/cf.d;assert qq*cf.d==den
  out.append(cf.n*qq)
 removed=one
 for label,atom in phys['paid_atoms']:
  while any(out):
   gg=atom
   for po in out:gg=gg.gcd(po)
   if gg.total_degree()==0:break
   newer=[p/gg for p in out]
   assert all(newer[j]*gg==out[j] for j in range(3))
   out=newer;removed*=gg
 pay(removed)
 first=next((p for p in out if p),None)
 if first is None:return out,tag
 qq=first.coefficient(0);out=[p/qq for p in out]
 scale=R(den,removed)/qq;trace=[scale*z for z in tag]
 assert all(R(out[j])==scale*row[j] for j in range(3))
 verify8(sum((R(out[j])*basis[j] for j in range(3)),R()),trace)
 return out,trace
rows=[];traces=[]
# The original N1 is kept. Do not treat the dual-point germ as a simple value.
row,tag=tri['reduce_row'](tri['original'][3],[R(int(i==3)) for i in range(6)])
rows.append(row);traces.append(tag+[R(),R()])
for index,value in enumerate([qvalue,rvalue]):
 po,removed,hist=strip(value.n)
 scale=R(value.d,removed);pay(scale.n);pay(scale.d)
 assert R(po)==scale*value
 row,tag6=tri['reduce_row'](R(po))
 # reduce_row with no initial tag returns rem-input = tag6*original6.
 tag=tag6+[scale if index==0 else R(),scale if index==1 else R()]
 verify8(sum((row[j]*basis[j] for j in range(3)),R()),tag)
 rows.append(row);traces.append(tag)
polyrows=[];polytraces=[]
for label,row,tag in zip(['N1','original_value_monic_T4','original_value_T3_remainder'],rows,traces):
 verify8(sum((row[j]*basis[j] for j in range(3)),R()),tag)
 po,tr=clear_row(row,tag);polyrows.append(po);polytraces.append(tr)
 for p in po:
  assert all(mm[2]==mm[3]==mm[5]==mm[6]==mm[7]==0 for mm in p.to_dict())
 say(stage='new_whole_W_original_value_three_column_row',label=label,
     columnProfiles=[profile(p) for p in po],
     allEightOriginalTraceProductsReturned=True,
     noDOrSingleValueCoefficientOrLambdaLeadingInverse=True,
     onlyPreviouslyPaidWeightDenominators=True,claimExcluded=False)
say(stage='new_whole_W_two_value_quartics_in_same_three_generator_model',
 actualOriginalValueSources='published R4/C4 identities in original E2,E3,E_Delta',
 exactWeightOnlyChange='qT4=C4/(8m u Q ell^2 d); rT3=R4-[T4]R4*qT4',
 allTwoValuePolynomialProductsAndDegreeIdentitiesReturned=True,
 originalRows=['N1','qT4','rT3'],
 lambdaThreeHalvesAndAllValueLeadingZeroFibresPreserved=True,
 noOldTwelveResultantOrGenericModuleExecuted=True,claimExcluded=False)
def det2(a,b):return a[0]*b[1]-a[1]*b[0]
A=polyrows
cof=[(-1)**i*det2(*[[A[r][j] for j in [1,2]] for r in range(3) if r!=i]) for i in range(3)]
C=sum((cof[i]*A[i][0] for i in range(3)),zero)
for j in range(3):
 assert sum((cof[i]*A[i][j] for i in range(3)),zero)==C*int(j==0)
say(stage='new_original_N1_two_value_quartic_fixed_constant_cofactor',
 rows=['N1','qT4','rT3'],polynomial=profile(C),
 allThreeColumnCofactorProductsReturned=True,
 originalEightTermSource='sum_i cofactor_i*the_actual_returned_row_trace_i',
 exactOriginalIdealConsequenceByAlreadyReturnedRows=True,
 noExpandedLargeEightTermTraceClaimed=True,
 allTemporaryAndLeadingZeroFibresIncluded=True,claimExcluded=False)
if not C:
 say(stage='new_original_value_fixed_cofactor_is_identically_zero',
     noNecessaryScalarCurveClaimed=True,wholeWExcluded=False,
     sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
 signal.alarm(0);raise SystemExit(2)
assert int(C.degrees()[4])<=8
# Construct only the coefficients required for this NEW monic division.
# The old generic module and its failed computation are never used.
ch=frozen_prefix(
 '2026-11-28-unit211-W-global-physical-lambda-six-characteristic-original-input-8542.py',
 '563ef7c9682a4b52f30bea024a391588c747fd97b0a2e8a6c1a4f14a49ec2d65',
 b'# Strip only these TWO',8601,
 'ce868f00596f420d1a46a1503e2432be7bd13f0001e8ebc3e0cd68a53092fc7a',
 'only_monic_lambda_coefficients_for_new_value_division')
chi=[R(c.n,c.d) for c in ch['chi']]
assert len(chi)==7 and chi[-1]==1
def trim(a):
 while a and not a[-1]:a.pop()
 return a
def Lcoeff(p):
 ans={}
 for mm,c in p.to_dict().items():
  assert mm[2]==mm[3]==mm[5]==mm[6]==mm[7]==0
  j=int(mm[4]);ans[j]=ans.get(j,zero)+c*ep**int(mm[0])*kp**int(mm[1])
 return trim([R(ans.get(j,zero)) for j in range(max(ans,default=-1)+1)])
def padd(a,b):
 return trim([(a[i] if i<len(a) else R())+(b[i] if i<len(b) else R()) for i in range(max(len(a),len(b)))])
def pmul(a,b):
 if not a or not b:return []
 out=[R() for _ in range(len(a)+len(b)-1)]
 for i,x in enumerate(a):
  for j,y in enumerate(b):out[i+j]+=x*y
 return trim(out)
cs=Lcoeff(C);rem=cs[:];quot=[R() for _ in range(max(0,len(cs)-6))]
while len(rem)>=7:
 h=len(rem)-7;v=rem[-1];quot[h]+=v
 for j in range(7):rem[h+j]-=v*chi[j]
 trim(rem)
assert padd(pmul(quot,chi),rem)==cs
assert len(rem)<=6
for c0 in quot+rem:
 assert all(not any(mm[j] for j in range(2,8)) for p in [c0.n,c0.d] for mm in p.to_dict())
 pay(c0.d)
def scalar_profile(c0):
 return dict(numerator=profile(c0.n),denominator=profile(c0.d))
say(stage='new_whole_W_original_value_lambda_degree_five_remainder',
 sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 originalFixedCofactorDegree=len(cs)-1,monicDivisorDegree=6,
 quotientDegree=len(trim(quot[:]))-1,remainderDegree=len(rem)-1,
 completePolynomialDivisionProductActuallyReturned=True,
 originalIdeal='I6+(R4,C4), localized only at previously paid weight factors',
 exactIdentity='remainder = fixed_value_cofactor - quotient*chi(lambda)',
 quotientCoefficientProfiles=[scalar_profile(c0) for c0 in quot],
 remainderCoefficientProfiles=[scalar_profile(c0) for c0 in rem],
 noOtherContentOrLeadingFactorDivided=True,
 allNewHeadZeroFibresPreserved=True,
 noExpandedDataOrEncodingOrMatrixCache=True,
 wholeWExcluded=False,ordinaryISPClaim=False,
 peakRssKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
signal.alarm(0)

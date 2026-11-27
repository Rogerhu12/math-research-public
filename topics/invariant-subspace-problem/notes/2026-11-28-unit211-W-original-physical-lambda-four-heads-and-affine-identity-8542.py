#!/usr/bin/env python3
"""NEW whole-W physical-lambda coordinate, four binary quadratic heads,
and a complete original affine relation, with no new head inverse.
The t coefficient of original lambda is exactly bc*Q/P02, already paid.
Only the original Gram construction prefix is used; no old six-column,
determinant, Gaussian or canonical large-value return is replayed.
180 seconds / 4 GiB; source/definitions/profiles only, no coefficient cache.
"""
import json,time,hashlib,signal,resource,contextlib,io,math,itertools
from pathlib import Path
start=time.perf_counter();deadline=start+180
signal.alarm(180);resource.setrlimit(resource.RLIMIT_AS,(4*1024**3,4*1024**3))
def say(**r):
 r['seconds']=time.perf_counter()-start
 print(json.dumps(r,separators=(',',':')),flush=True)
def digest(obj):
 raw=json.dumps(obj,separators=(',',':')).encode()
 return dict(bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest())
dep=Path(__file__).with_name('2026-11-27-unit211-generic-LS-W-C9-six-generator-original-parameter-cofactors-8542.py')
raw=dep.read_bytes()
assert hashlib.sha256(raw).hexdigest()=='10720660772a9a1252b905b1227b697e038d1b974b7e96ec30e485477b21d3f1'
marker=b'\n# New mathematical input: all four original quadratics'
assert raw.count(marker)==1
prefix=raw.split(marker)[0]
assert len(prefix)==7224
assert hashlib.sha256(prefix).hexdigest()=='be7af2ffd4e73d716847c7fa6286170ec18702ea8c84a7cb964e8fcd5622ae4f'
ns={'__file__':str(dep),'__name__':'frozen_Gram_only_for_new_physical_lambda_input'}
with contextlib.redirect_stdout(io.StringIO()):
 exec(compile(prefix,str(dep),'exec'),ns)
signal.alarm(max(1,math.ceil(deadline-time.perf_counter())))
R=ns['R'];ctx=ns['ctx'];ep,kp,xp,yp,Lp=ctx.gens()[:5]
zero=ns['zz'];one=ns['oo'];xx,yy,L=map(R,[xp,yp,Lp])
e,k,u,Q,ell,bc,P02,T0,J,Phi=[ns[z] for z in ['e','k','u','Q','l','bc','P02','T0','J','Phi']]
original=[ns['symbolic'][z] for z in ['E1','EBe','EBo','N1','NS','PS']]
# All entries in this list are existing WHOLE current-W weight units.
C9=4*ep**2*kp**2-ep*(kp**4+9*kp**3+20*kp**2+16*kp)+kp**3+10*kp**2+24*kp+16
J19=(16*ep**4*kp**3-8*ep**3*kp**4-16*ep**3*kp**3-96*ep**3*kp**2
 -ep**2*kp**5-8*ep**2*kp**4+24*ep**2*kp**3+64*ep**2*kp**2+192*ep**2*kp
 -2*ep*kp**5-14*ep*kp**4-12*ep*kp**3-128*ep-kp**5-10*kp**4-40*kp**3-104*kp**2-160*kp-128)
D27=(16*ep**5*kp**4-4*ep**4*kp**5+32*ep**4*kp**4+2*ep**3*kp**6
 -12*ep**3*kp**5-96*ep**3*kp**4-384*ep**3*kp**3-384*ep**3*kp**2
 +3*ep**2*kp**6+8*ep**2*kp**5+60*ep**2*kp**4+384*ep**2*kp**3
 +1088*ep**2*kp**2+1024*ep**2*kp-10*ep*kp**5-28*ep*kp**4
 +48*ep*kp**3+64*ep*kp**2-512*ep*kp-768*ep-kp**6-18*kp**5
 -120*kp**4-440*kp**3-1008*kp**2-1344*kp-768)
gcoeff=[[4096,9216,7680,3072,592,24,-10,-1],
 [-6144,-16128,-14336,-6048,-1416,-186,-9],
 [512,6016,6560,2528,468,50,2],
 [1792,832,-832,-392,-50,-2],
 [-256,-544,-24,24,4],[-192,0,-8],[32]]
G36=sum((sum((ctx.constant(v)*kp**j for j,v in enumerate(row)),zero)*(ep*kp)**i for i,row in enumerate(gcoeff)),zero)
paid_atoms=ns['units']+[
 ('k_plus_one',kp+1),('whole_equal_weights_k_plus_two',kp+2),
 ('old_H',4*ep*kp-kp**2-4*kp-8),('whole_u_half',2*ep+1),
 ('ell',ell.n),('ell_minus_u',(ell-u).n),('Q_minus_two',(Q-2).n),
 ('u_minus_Q',(u-Q).n),('T0',T0.n),('J_minus_Q',(J-Q).n),
 ('whole_C9',C9),('whole_J19',J19),('whole_D27',D27),('whole_G36',G36)]
def strip(p):
 p0=p;removed=one;hist=[]
 for name,atom in paid_atoms:
  count=0
  while p:
   g=p.gcd(atom)
   if g.total_degree()==0:break
   q=p/g;assert q*g==p
   p=q;removed*=g;count+=1
  if count:hist.append([name,count])
 assert p*removed==p0
 return p,removed,hist
def pay(p):
 assert p
 rest,removed,hist=strip(p)
 assert rest.total_degree()==0 and rest*removed==p
 return hist
def enc(p):
 return [[[int(i) for i in mm],str(c)] for mm,c in sorted(p.to_dict().items())]
def prof(p):
 return dict(degrees=list(map(int,p.degrees()[:5])),
  totalDegree=int(p.total_degree()),terms=len(p.to_dict()),**digest(enc(p)))
def rprof(r):
 r=R(r);return dict(numerator=prof(r.n),denominator=prof(r.d))
def geo_coeff(rr):
 rr=R(rr)
 assert all(all(mm[j]==0 for j in range(2,8)) for mm in rr.d.to_dict())
 out={}
 for mm,c in rr.n.to_dict().items():
  assert not any(mm[j] for j in range(5,8))
  ijh=tuple(map(int,mm[2:5]))
  out[ijh]=out.get(ijh,zero)+c*ep**int(mm[0])*kp**int(mm[1])
 return {m:R(p,rr.d) for m,p in out.items() if p}
def subst(rr,images):
 cc=geo_coeff(rr);mx=[max((m[j] for m in cc),default=0) for j in range(3)]
 pw=[]
 for image,degree in zip(images,mx):
  arr=[R(1)]
  for z in range(degree):arr.append(arr[-1]*image)
  pw.append(arr)
 return sum((v*pw[0][m[0]]*pw[1][m[1]]*pw[2][m[2]] for m,v in cc.items()),R())
old_lambda=ns['symbolic']['lam']
lamcoeff=geo_coeff(old_lambda)
assert set(lamcoeff).issubset({(0,0,0),(1,0,0),(0,1,0),(0,0,1)})
a0,ax,ay,at=[lamcoeff.get(m,R()) for m in [(0,0,0),(1,0,0),(0,1,0),(0,0,1)]]
assert at==bc*Q/P02
pay(at.n);pay(at.d)
tnew=(L-a0-ax*xx-ay*yy)/at
pay(tnew.d)
assert subst(old_lambda,[xx,yy,tnew])==L
assert subst(tnew,[xx,yy,old_lambda])==R(Lp)
new=[];polys=[];scales=[]
for i,rr in enumerate(original):
 rrnew=subst(rr,[xx,yy,tnew])
 assert subst(rrnew,[xx,yy,old_lambda])==rr
 pay(rrnew.d)
 assert all(sum(m)<= (2 if i<4 else 3) for m in geo_coeff(rrnew))
 po,removed,hist=strip(rrnew.n)
 scale=R(rrnew.d,removed);pay(scale.n);pay(scale.d)
 assert R(po)==scale*rrnew
 new.append(rrnew);polys.append(po);scales.append(scale)
say(stage='new_whole_W_original_physical_lambda_coordinate',
 exactForwardIdentity='lambda=alpha0+alphax*x+alphay*y+(bc*Q/P02)*t',
 exactInverseIdentity='t=(lambda-alpha0-alphax*x-alphay*y)/(bc*Q/P02)',
 bothCoordinateProductsActuallyReturned=True,
 sixFullOriginalEquationForwardAndReverseProductsReturned=True,
 newVariables=['e','k','x','y','lambda'],
 onlyPreviouslyPaidWeightDenominators=True,noLambdaNormDOrNewHeadInverted=True,
 originalOtherValueConditionsStillRequired=True)
headmons=[(2,0,0),(1,1,0),(0,2,0)]
heads=[]
for po in polys[:4]:
 cc=geo_coeff(R(po))
 for (i,j,h),v in cc.items():
  if i+j==2:assert h==0
 row=[cc.get(m,R()) for m in headmons]
 assert all(v.d==one for v in row)
 heads.append([v.n for v in row])
def det3(mat):
 assert len(mat)==3 and all(len(r)==3 for r in mat)
 a,b,c=mat
 return a[0]*(b[1]*c[2]-b[2]*c[1])-a[1]*(b[0]*c[2]-b[2]*c[0])+a[2]*(b[0]*c[1]-b[1]*c[0])
cof=[(-1)**i*det3([heads[j] for j in range(4) if j!=i]) for i in range(4)]
for j in range(3):assert sum((cof[i]*heads[i][j] for i in range(4)),zero)==0
# Divide a COMMON FACTOR OF ALL FOUR ACTUAL MULTIPLIERS, not an original
# equation and not a head assumed nonzero. The resulting polynomial
# coefficients still form an original combination on its entire zero set.
common=next((c for c in cof if c),None)
if common is not None:
 for c in cof:
  if c:common=common.gcd(c)
 cofn=[]
 for c in cof:
  q=c/common;assert q*common==c;cofn.append(q)
 scalar=next(c for c in cofn if c).coefficient(0)
 cofn=[c/scalar for c in cofn];common*=scalar
 assert all(cofn[i]*common==cof[i] for i in range(4))
 for j in range(3):assert sum((cofn[i]*heads[i][j] for i in range(4)),zero)==0
 line=sum((R(cofn[i])*R(polys[i]) for i in range(4)),R())
 tag=[R(cofn[i])*scales[i] if i<4 else R() for i in range(6)]
 assert line==sum((tag[i]*new[i] for i in range(6)),R())
 cc=geo_coeff(line)
 assert all(i+j<=1 and i+j+h<=2 for i,j,h in cc)
 c0=R();cx=R();cy=R()
 for (i,j,h),v in cc.items():
  part=v*(L**h)
  if i==1:cx+=part
  elif j==1:cy+=part
  else:c0+=part
 assert line==c0+cx*xx+cy*yy
 assert max((m[2] for m in geo_coeff(cx)),default=-1)<=1
 assert max((m[2] for m in geo_coeff(cy)),default=-1)<=1
 assert max((m[2] for m in geo_coeff(c0)),default=-1)<=2
 for z in [c0,cx,cy]+tag:pay(z.d)
 # Return it to the actual old Gram as well, with no new root choice.
 old_line=subst(line,[xx,yy,old_lambda])
 old_tags=[subst(z,[xx,yy,old_lambda]) for z in tag]
 assert old_line==sum((old_tags[i]*original[i] for i in range(6)),R())
 say(stage='new_entire_W_four_original_quadratics_affine_physical_lambda_identity',
  exactIdentity='L0(lambda)+Lx(lambda)*x+Ly(lambda)*y=sum_i true_cofactor_i*original_quad_i',
  allThreeQuadraticHeadProductsReturned=True,
  allFourCommonMultiplierDivisionProductsReturned=True,
  originalPolynomialIdentityInBothCoordinateSystemsReturned=True,
  cofactorCommonRemoved=prof(common),
  affineCoefficientProfiles={'constant':rprof(c0),'x':rprof(cx),'y':rprof(cy)},
  allNewHeadZeroFibresIncluded=True,
  noCommonFactorWasDeclaredAUnit=True,
  noOriginalEquationDividedByAnUnpaidFactor=True,
  newAffineRelationNonzero=bool(line),wholeWExcluded=False)
else:
 cofn=[zero]*4
 say(stage='accurate_new_physical_lambda_four_head_minors_all_zero',
  rankAtMostTwoOverWeightFunctionField=True,noNewAffineRelationClaimed=True,
  wholeWExcluded=False)
# Only FOUR new lambda-direction quadratic heads, not the old fifteen
# three-variable heads. Factor each whole QQ polynomial with product return.
factor_cache={}
def factor_profile(p):
 if not p:return dict(zero=True)
 lead=p.coefficient(0);pp=p/lead
 key=str(pp)
 if key in factor_cache:
  scalar,out=factor_cache[key]
  return dict(scalar=str(lead*scalar),factors=out,completeFactorProductReturned=True)
 scalar,factors=pp.factor();back=ctx.constant(scalar);out=[]
 for fac,m in factors:
  m=int(m);back*=fac**m
  rec=dict(multiplicity=m,**prof(fac))
  ss=str(fac)
  if len(ss)<=2048 and len(fac.to_dict())<=30:rec['shortDefiningPolynomial']=ss
  out.append(rec)
 assert back==pp
 answer=dict(scalar=str(lead*scalar),factors=out,completeFactorProductReturned=True)
 factor_cache[key]=(scalar,out)
 return answer
unit_heads=[]
for omitted,c in enumerate(cof):
 if not c:
  say(stage='new_physical_lambda_fixed_quadratic_head_zero',omittedOriginal=omitted)
  continue
 remaining,paidpart,hist=strip(c)
 assert remaining*paidpart==c
 if remaining.total_degree()==0:unit_heads.append(omitted)
 say(stage='new_physical_lambda_fixed_quadratic_head_complete_QQ_factor',
  omittedOriginal=omitted,originalRows=[i for i in range(4) if i!=omitted],
  rawHead=prof(c),paidRemoved=hist,
  remainingUnpaid=prof(remaining),
  completeRemainingQQFactorization=factor_profile(remaining),
  paidOnWholeCurrentW=(remaining.total_degree()==0),
  allUnpaidFactorZeroFibresRetained=True)
if common is not None:
 say(stage='new_physical_lambda_common_four_head_factor',
  exactCommonMultiplier=prof(common),
  completeCommonQQFactorization=factor_profile(common),
  commonZeroNotExcluded=True,
  normalizedCofactorOriginalIdentityStillGlobal=True)
say(stage='new_physical_lambda_original_head_and_affine_input_finished',
 sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 paidThreeHeadChoices=unit_heads,
 exactCoordinateAndAllOriginalEquationReturnsComplete=True,
 originalAffineIdentityReturned=(common is not None),
 allNewHeadZeroFibresRetained=True,
 noWeightCurveEmptinessOrQuotientFreenessClaim=True,
 noFormerSixDeterminantOrGaussianGateReplayed=True,
 noEncodedOrChunkedParameterDataOrRegenerableCacheWritten=True,
 peakRssKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
 wholeWExcluded=False,ordinaryISPClaim=False)
signal.alarm(0)

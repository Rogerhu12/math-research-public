#!/usr/bin/env python3
"""NEW entire QQ original moment-image fibers on the exceptional Phi graph.
The actual identity psiD=3*B3^2-2*A2^3 gives a genuine QQ input,
not a lift guessed from modular support. Test all its irreducible
QQ factors and every embedding against the three saved same-rho
original curves. A complete fixed QQ ideal matrix with integral
modular inverse can exclude whole fibers. Then an independent exact
regular-representation kernel of the ORIGINAL 57 Sylvester gives
true QQ phi-adic determinant lower bounds by the local corank lemma.
Finally take the actual full new modular quotient/gcd/Bezout.
120 seconds /1 GiB. Same three SHA-pinned JSON dependencies; no helpers.
"""
import time,json,hashlib,base64,zlib,signal,resource
from pathlib import Path
from flint import fmpq,fmpq_poly,fmpq_mpoly_ctx,nmod_poly,fmpq_mat
signal.alarm(120);resource.setrlimit(resource.RLIMIT_AS,(1024**3,1024**3))
began=time.perf_counter()
def say(stage,**kw):
 kw.update(stage=stage,seconds=time.perf_counter()-began)
 print(json.dumps(kw),flush=True)
ctx=fmpq_mpoly_ctx.get(("rho","lam"),"lex")
def load_poly(data,payload_sha,poly_sha,degrees,terms):
 raw=zlib.decompress(base64.b64decode(data))
 assert hashlib.sha256(raw).hexdigest()==payload_sha
 obj=json.loads(raw);assert obj["variables"]==["rho","lam"]
 pp=ctx.from_dict({(int(i),int(j)):fmpq(c) for i,j,c in obj["terms"]})
 assert list(map(int,pp.degrees()))==degrees and len(pp.to_dict())==terms
 assert hashlib.sha256(str(sorted(pp.to_dict().items())).encode()).hexdigest()==poly_sha
 return pp
def dependency(name,sha256):
 path=Path(__file__).with_name(name)
 raw=path.read_bytes()
 assert hashlib.sha256(raw).hexdigest()==sha256,("wrong exact dependency",name)
 return json.loads(raw)
inputF=dependency(
 "2026-11-27-unit211-Phi-zero-exceptional-F26-exact-input-8542.json",
 "67c73f8f5fef33d509ffebd8165487e5b6abcc59fe391acc4075da1f22287d61")
inputG=dependency(
 "2026-11-27-unit211-Phi-zero-exceptional-PB-core-and-mod-resultant-exact-input-8542.json",
 "74891d2b2f8bd21f74ff063cef7aeed85532a2378e71dac07ad5cfc4d240c8c9")
inputH=dependency(
 "2026-11-27-unit211-Phi-zero-exceptional-mixed-core-and-mod-return-exact-input-8542.json",
 "a9ab01ff03d894ed1fe6033b68268ecbf7b9d36dc2cd4ff3d7bf69b771387073")
rf,rg,rh=(obj["polynomial"] for obj in (inputF,inputG,inputH))
F=load_poly(rf["data"],rf["payloadSha256"],
 "9057238c5d37c8cd9f62f3f512dcff1f6d2e385cd6c0e39250a571713f0aaac7",[26,26],729)
G=load_poly(rg["data"],rg["payloadSha256"],
 "3d850765f6c9338aa8f79af2b5889582cf8d4f45fd81ad90f4743fb5bebd5f6c",[31,50],1632)
H=load_poly(rh["data"],rh["payloadSha256"],
 "496ce5b01ff327ac7b1fa6a125f04808d368aca7a88b0078f0e0622ced90f8e4",[34,48],1715)

# This is an exact original moment-image polynomial, not a modular
# factor reconstruction.  D=ell*A2-T^2=0 and sn=ell*B3-A2*T=0
# at ell=3/2 imply psiD=3*B3^2-2*A2^3=0.  The converse is NOT
# assumed; every whole lambda fiber is tested with all three originals.
A2poly=fmpq_poly([1,-2,2]);B3poly=fmpq_poly([-1,3,-6,4])
psi=3*B3poly**2-2*A2poly**3
assert psi==fmpq_poly([1,-6,27,-68,108,-96,32])
scalar,fac=psi.factor();product=fmpq_poly([scalar]);phis=[]
for ix,(fp,multiplicity) in enumerate(fac):
 product*=fp**multiplicity
 monic=fp*(1/fp[fp.degree()])
 phis.append(("genuine_moment_image_factor_"+str(ix),monic))
assert product==psi
say("new_exact_original_D_sn_zero_moment_image_QQ_factors",
    psiCoefficientsAscending=[str(psi[i]) for i in range(psi.degree()+1)],
    exactWholeQQFactorProductReturned=True,
    factors=[dict(label=label,coefficientsAscending=[str(p[i]) for i in range(p.degree()+1)])
             for label,p in phis],
    momentImageEquationNotAssumedToForceDZero=True)
rho_units=[("1-Q",fmpq(0)),("Q_rho1",fmpq(1)),("Q_rho_minus1",fmpq(-1)),
           ("T0",fmpq(3)),("u",fmpq(-3)),("u+Q-1",fmpq(3,2))]
stats={"exactQQOriginalLinearUnitDivisions":0,"exactQQLeadingInverseProducts":0,
       "modMonicDivisionProducts":0,"modScalarInverseProducts":0,
       "completeSelectedSquareInverseProducts":0}
def qqcoeffs_in_rho(p):
 n=int(p.degrees()[0]);out=[fmpq_poly([]) for _ in range(n+1)]
 for (i,j),c in p.to_dict().items():
  cc=[fmpq(0)]*(int(j)+1);cc[int(j)]=c
  out[int(i)]=out[int(i)]+fmpq_poly(cc)
 return out
original=[qqcoeffs_in_rho(p) for p in (F,G,H)]
outcomes=[]
for label,phi in phis:
 e=int(phi.degree());kzero=fmpq_poly([]);kone=fmpq_poly([1])
 def kk(x):return x%phi
 def trim(a):
  a=[kk(x) for x in a]
  while a and not a[-1]:a.pop()
  return a
 def ka(a,b):
  cc=[kzero]*max(len(a),len(b))
  for i in range(len(a)):cc[i]=cc[i]+a[i]
  for i in range(len(b)):cc[i]=cc[i]+b[i]
  return trim(cc)
 def km(a,b):
  if not a or not b:return []
  cc=[kzero]*(len(a)+len(b)-1)
  for i,x in enumerate(a):
   for j,y in enumerate(b):cc[i+j]=cc[i+j]+x*y
  return trim(cc)
 def evaluate(a,r):
  v=kzero
  for c in reversed(a):v=kk(v*r+c)
  return v
 values=[trim(a) for a in original];removed=[]
 for j,a in enumerate(values):
  rr=[]
  for uname,r in rho_units:
   while a and len(a)>1 and not evaluate(a,r):
    olda=a;q=[kzero]*(len(a)-1);q[-1]=a[-1]
    for i in range(len(a)-2,0,-1):q[i-1]=kk(a[i]+r*q[i])
    assert not kk(a[0]+r*q[0])
    assert km(q,[fmpq_poly([-r]),kone])==olda
    stats["exactQQOriginalLinearUnitDivisions"]+=1
    a=trim(q);rr.append(uname)
  values[j]=a;removed.append(rr)
 say("new_entire_QQ_parameter_fiber_original_unit_divisions",
     fiber=label,phiCoefficients=[str(phi[j]) for j in range(e+1)],
     originalRhoDegrees=[len(a)-1 for a in original],
     residualRhoDegrees=[len(a)-1 for a in values],
     removedOnlyActualOriginalRhoUnitFactors=removed,
     allExactDivisionsMultipliedBack=True)
 candidates=sorted((len(a)-1,j) for j,a in enumerate(values) if a)
 assert candidates
 selected=None
 for n,j in candidates:
  lc=values[j][-1]
  gg,ss,tt=lc.xgcd(phi)
  assert ss*lc+tt*phi==gg
  if gg.degree()!=0:continue
  inv=kk(ss*(1/gg[0]));assert kk(inv*lc)==kone
  stats["exactQQLeadingInverseProducts"]+=1
  selected=(n,j,inv);break
 assert selected is not None
 n,j0,inv=selected
 monic=trim([kk(c*inv) for c in values[j0]])
 assert monic[-1]==kone and len(monic)==len(values[j0])
 assert [kk(c*values[j0][-1]) for c in monic]==values[j0]
 if n==0:
  result=dict(fiber=label,wholeQQFiberExcluded=True,
              reason="an exact original residual is a nonzero constant unit",
              monicOriginalIndex=j0,QQLeadingInverseProductReturned=True)
  outcomes.append(result);say("complete_new_entire_QQ_parameter_fiber",**result)
  continue
 # Choose an actual integral prime for the specific QQ matrix below.
 # Its entries are defined by monic rho division, so integral inputs
 # imply integral entries; no uncomputed quotient-norm inverse is used.
 chosen=None
 for prime in [1009,1013,1019,1021,1031]:
  assert all(prime%d for d in range(2,int(prime**0.5)+1))
  allqq=[phi]+monic+[c for a in values for c in a]
  if all(int(p[t].denominator)%prime for p in allqq for t in range(p.degree()+1)):
   chosen=prime;break
 assert chosen is not None
 prime=chosen
 def bar(p):
  aa=[]
  for t in range(p.degree()+1):
   c=fmpq(p[t]);den=int(c.denominator)%prime;assert den
   v=pow(den,-1,prime);assert den*v%prime==1
   aa.append(int(c.numerator)%prime*v%prime)
  return nmod_poly(aa,prime)
 phibar=bar(phi);mz=nmod_poly([],prime);mo=nmod_poly([1],prime)
 def mk(p):return p%phibar
 def mt(a):
  a=[mk(x) for x in a]
  while a and not a[-1]:a.pop()
  return a
 def ma(a,b):
  cc=[mz]*max(len(a),len(b))
  for i in range(len(a)):cc[i]=cc[i]+a[i]
  for i in range(len(b)):cc[i]=cc[i]+b[i]
  return mt(cc)
 def mm(a,b):
  if not a or not b:return []
  cc=[mz]*(len(a)+len(b)-1)
  for i,x in enumerate(a):
   for j,y in enumerate(b):cc[i+j]=cc[i+j]+x*y
  return mt(cc)
 mf=mt([bar(c) for c in monic]);assert mf[-1]==mo
 assert len(mf)==n+1 and int(phibar.degree())==e
 def red(a):
  a=mt(a);olda=list(a)
  q=[mz]*max(0,len(a)-n)
  while a and len(a)>n:
   shift=len(a)-1-n;c=a[-1];q[shift]=c
   for t in range(n+1):a[shift+t]=mk(a[shift+t]-c*mf[t])
   a=mt(a)
  q=mt(q)
  assert ma(mm(q,mf),a)==olda
  stats["modMonicDivisionProducts"]+=1
  return a
 rows=[];tags=[]
 for j,a in enumerate(values):
  if j==j0:continue
  cur=red([bar(c) for c in a])
  for rpower in range(n):
   for lpower in range(e):
    lp=nmod_poly([0]*lpower+[1],prime)
    cc=[mk(c*lp) for c in cur]
    row=[]
    for r in range(n):
     c=cc[r] if r<len(cc) else mz
     row.extend(int(c[t]) for t in range(e))
    rows.append(row);tags.append([j,rpower,lpower])
   cur=red([mz]+cur)
 dimension=n*e
 # Select an explicit square submatrix using exact finite-field row
 # operations.  The complete inverse product below certifies its rank.
 basis={};chosen_rows=[]
 for index,row in enumerate(rows):
  a=list(row)
  for pivot,b in sorted(basis.items()):
   z=a[pivot]
   if z:
    for c in range(pivot,dimension):a[c]=(a[c]-z*b[c])%prime
  pivot=next((c for c,z in enumerate(a) if z),None)
  if pivot is None:continue
  invpivot=pow(a[pivot],-1,prime)
  assert a[pivot]*invpivot%prime==1
  stats["modScalarInverseProducts"]+=1
  a=[z*invpivot%prime for z in a]
  basis[pivot]=a;chosen_rows.append(index)
  if len(basis)==dimension:break
 full=len(basis)==dimension
 cert=None
 if full:
  B=[list(rows[i]) for i in chosen_rows]
  aug=[r+[int(i==j) for j in range(dimension)] for i,r in enumerate(B)]
  for c in range(dimension):
   pivot=next(r for r in range(c,dimension) if aug[r][c])
   aug[c],aug[pivot]=aug[pivot],aug[c]
   iv=pow(aug[c][c],-1,prime);assert aug[c][c]*iv%prime==1
   stats["modScalarInverseProducts"]+=1
   aug[c]=[v*iv%prime for v in aug[c]]
   for r in range(dimension):
    if r==c:continue
    z=aug[r][c]
    if z:aug[r]=[(x-z*y)%prime for x,y in zip(aug[r],aug[c])]
  assert all(aug[i][j]==int(i==j) for i in range(dimension) for j in range(dimension))
  inverse=[row[dimension:] for row in aug]
  cols=list(zip(*inverse))
  for i,row in enumerate(B):
   for j,col in enumerate(cols):
    assert sum(x*y for x,y in zip(row,col))%prime==int(i==j)
  stats["completeSelectedSquareInverseProducts"]+=1
  cert=dict(selectedOriginalRows=[tags[i] for i in chosen_rows],
            selectedSquareSha256=hashlib.sha256(str(B).encode()).hexdigest(),
            inverseSha256=hashlib.sha256(str(inverse).encode()).hexdigest(),
            completeSelectedSquareTimesInverseReturned=True)
 result=dict(fiber=label,phiDegree=e,prime=prime,
             monicOriginalIndex=j0,monicRhoDegree=n,
             finiteAlgebraDimension=dimension,originalMacaulayRows=len(rows),
             actualRank=len(basis),squareCertificate=cert,
             exactQQLeadingInverseProductReturned=True,
             allQQMatrixInputsIntegralAtActualPrime=True,
             modMatrixIsReductionOfFixedQQOriginalIdealMatrix=True,
             wholeQQFiberExcluded=full,
             noBareModularEmptinessInference=True,
             noOriginalResultantRecomputed=True)
 outcomes.append(result);say("complete_new_entire_QQ_parameter_fiber",**result)

all_fibers=all(x["wholeQQFiberExcluded"] for x in outcomes)
say("complete_new_genuine_moment_image_whole_QQ_fibers",
    outcomes=outcomes,checks=stats,allWholeQQFibersExcluded=all_fibers,
    ordinaryISPClaim=False)
def original_rho_coefficients(p):
 out=[fmpq_poly([]) for _ in range(int(p.degrees()[0])+1)]
 for (i,j),c in p.to_dict().items():
  row=[fmpq(0)]*(int(j)+1);row[int(j)]=c
  out[int(i)]=out[int(i)]+fmpq_poly(row)
 return out
pf,pg=original_rho_coefficients(F),original_rho_coefficients(G)
assert [len(pf)-1,len(pg)-1]==[26,31]
zero=fmpq_poly([]);matrix=[[zero]*57 for _ in range(57)]
for i in range(31):
 for j in range(27):matrix[i][i+j]=pf[j]
for i in range(26):
 for j in range(32):matrix[31+i][i+j]=pg[j]
oldphi1=fmpq_poly([fmpq(-1,2),1])
oldphi6=fmpq_poly([fmpq(5,64),fmpq(39,80),fmpq(63,80),
                  fmpq(-7,10),fmpq(-9,4),fmpq(3,5),1])
already_paid=oldphi1**10*oldphi6**2
def mod1009(p):
 aa=[]
 for i in range(p.degree()+1):
  c=p[i];dd=int(c.denominator)%1009;assert dd
  aa.append(int(c.numerator)%1009*pow(dd,-1,1009)%1009)
 return nmod_poly(aa,1009)
def old_mod(rec,expected_sha,expected_degree):
 raw=zlib.decompress(base64.b64decode(rec["fullCoefficientsData"]))
 assert hashlib.sha256(raw).hexdigest()==rec["fullCoefficientsPayloadSha256"]
 p=nmod_poly(json.loads(raw),1009)
 assert p.degree()==expected_degree and hashlib.sha256(str(p).encode()).hexdigest()==expected_sha
 return p
oldR=old_mod(inputG["full_fixed_mod1009_resultant"],
 "f4505a726a6c2691ac52b92ec424160f7cc748d6a9b17751ce8b2f9f3f0eaa85",2033)
oldS=old_mod(inputH["fixed_mod_resultant"],
 "060c2f63b871fec6e649ce3bdfbf29612df9402b07c3c4d381245f639edb8e12",2050)
baseR,rem=divmod(oldR,mod1009(already_paid))
assert rem==0 and baseR*mod1009(already_paid)==oldR and baseR.degree()==2011
new_power=fmpq_poly([1]);all_extra_power=fmpq_poly([1]);local=[];local_checks=0
excluded_labels={item["fiber"] for item in outcomes if item["wholeQQFiberExcluded"]}
for label,ph in phis:
 e=int(ph.degree());N=57*e
 cop,aa,bb=ph.xgcd(already_paid)
 assert aa*ph+bb*already_paid==cop and cop.degree()==0
 reduced=[]
 for row in matrix:
  rr=[]
  for p in row:
   q,r=divmod(p,ph);assert q*ph+r==p;rr.append(r);local_checks+=1
  reduced.append(rr)
 table=[[fmpq(0)]*N for _ in range(N)]
 powers=[fmpq_poly([0]*j+[1]) for j in range(e)]
 for i in range(57):
  for j in range(57):
   for h,powu in enumerate(powers):
    entry=(reduced[i][j]*powu)%ph
    for k in range(e):table[i*e+k][j*e+h]=entry[k]
 B=fmpq_mat(table);rr,rank=B.rref();rank=int(rank)
 pivots=[]
 for i in range(rank):
  p=next(j for j in range(N) if rr[i,j])
  assert rr[i,p]==1;pivots.append(p)
 free=[j for j in range(N) if j not in set(pivots)]
 assert len(free)==N-rank and (N-rank)%e==0
 c=(N-rank)//e
 certificate=None
 if free:
  kdim=len(free);entries=[[fmpq(0)]*kdim for _ in range(N)]
  for j,fcol in enumerate(free):
   entries[fcol][j]=fmpq(1)
   for i,pivot in enumerate(pivots):entries[pivot][j]=-rr[i,fcol]
  kernel=fmpq_mat(entries)
  assert B*kernel==fmpq_mat(N,kdim,[0]*(N*kdim))
  assert all(kernel[free[i],j]==int(i==j) for i in range(kdim) for j in range(kdim))
  for j in range(kdim):
   kv=[fmpq_poly([kernel[i*e+t,j] for t in range(e)]) for i in range(57)]
   assert any(kv)
   for row in reduced:
    assert not sum((p*x for p,x in zip(row,kv)),zero)%ph
    local_checks+=1
  certificate=dict(regularQQDimension=N,actualQQRank=rank,
                   independentQQKernelColumns=kdim,guaranteedKCorank=c,
                   completeQQMatrixTimesKernelReturned=True,
                   completeFreeRowIdentityReturned=True,
                   allOriginalKRowProductsReturned=True,
                   kernelSha256=hashlib.sha256(str(entries).encode()).hexdigest())
 # Exact local algebra lemma: over QQ[lambda] localized at the
 # irreducible ph, a matrix with residue-field corank c has determinant
 # divisible by ph^c. Gaussian elimination uses only local units;
 # after the invertible residue block is removed the remaining c-by-c
 # block has every entry divisible by ph. Clearing those local units
 # does not change ph-adic valuation. No such units are asserted to be
 # global original physical units.
 barphi=mod1009(ph);vr=0;cur=baseR
 while cur and cur%barphi==0:
  q=cur//barphi;assert q*barphi==cur;cur=q;vr+=1
 assert c<=vr
 all_extra_power*=ph**c
 usable=label in excluded_labels
 if usable:new_power*=ph**c
 item=dict(factor=label,QQPhiCoefficients=[str(ph[i]) for i in range(e+1)],
           degree=e,provedQQDeterminantDivisibilityPower=c,
           factorUsedForGlobalPointBound=usable,
           completeStoredModRMultiplicity=vr,
           allQQConjugatesCovered=True,
           oldPaidQQFactorCoprimalityMultipliedBack=True,
           exactKernelCertificate=certificate,
           onlyLocalDeterminantValuationUnitsUsed=True)
 local.append(item);say("new_actual_original_Sylvester_QQ_corank_divisibility",**item)
newR,rem=divmod(baseR,mod1009(new_power))
assert rem==0 and newR*mod1009(new_power)==baseR
gg,aa,bb=newR.xgcd(oldS)
assert aa*newR+bb*oldS==gg
say("complete_new_moment_image_exact_local_divisibility_and_actual_quotient",
    completeWholeQQFiberOutcomes=outcomes,
    allWholeQQFibersExcluded=all_fibers,
    exactQQDivisibilityCertificates=local,
    totalAdditionalQQRemovedDegree=int(new_power.degree()),
    totalAdditionalQQDivisibilityDegreeIncludingUnexcludedFibers=int(all_extra_power.degree()),
    newMonicQQRQuotientDegree=2011-int(new_power.degree()),
    actualNewFullModRQuotientDegree=int(newR.degree()),
    actualFullModSDegree=int(oldS.degree()),
    actualNewFullModGcdDegree=int(gg.degree()),
    actualNewFullModGcdCoefficients=[int(gg[i]) for i in range(gg.degree()+1)],
    newBezoutDegrees=[int(aa.degree()),int(bb.degree())],
    completeNewBezoutProductReturned=True,additionalLocalProductChecks=local_checks,
    strictDifferentOrderedBasePointBound=int(gg.degree()),
    oldStrictDifferentOrderedBasePointBound=146,
    newBoundUsesOnlySeparatelyExcludedWholeQQFibers=True,
    noOldCofactorOrCompleteResultantRecomputed=True,
    wholeExceptionalBranchExcluded=False,ordinaryISPClaim=False)

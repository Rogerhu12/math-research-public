#!/usr/bin/env python3
"""NEW entire QQ lambda fibers for two exact original Phi boundary images.
Use the three saved original curves only.  Strip actual rho unit factors
by exact QQ[lambda]/phi linear divisions, multiplied back.  Normalize
one original rho polynomial using a QQ Bezout inverse modulo phi.
A full-rank, fixed finite original-ideal matrix mod an integral prime
then certifies the complete QQ fiber by Gauss; its selected square
inverse is fully multiplied back.  Reducible modular phi is allowed.
No direct modular emptiness inference; no resultant replay.
120 seconds / 1 GiB, three same pinned JSON dependencies as 4f9fe288.
"""
import time,json,hashlib,base64,zlib,signal,resource
from pathlib import Path
from flint import fmpq,fmpq_poly,fmpq_mpoly_ctx,nmod_poly
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

# These two exact QQ polynomials were obtained from full original
# same-rho QQ gcds by source 4f9fe288; not reconstructed from mod factors.
phis=[("lambda_half",fmpq_poly([fmpq(-1,2),1])),
      ("genuine_boundary_H6",fmpq_poly([fmpq(5,64),fmpq(39,80),fmpq(63,80),
                                      fmpq(-7,10),fmpq(-9,4),fmpq(3,5),1]))]
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
  a=mt(a);olda=a
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
say("complete_two_genuine_boundary_image_QQ_fibers",
     outcomes=outcomes,checks=stats,
     bothWholeQQFibersExcluded=all(x["wholeQQFiberExcluded"] for x in outcomes),
     QQHigherResultantMultiplicitiesNotYetPaid=True,
     priorStrictDifferentOrderedBasePointBound=168,
     newFinitePointBoundClaim=False,ordinaryISPClaim=False)

#!/usr/bin/env python3
"""NEW exact QQ local multiplicities of the original 57 Sylvester R.
For the two genuine QQ boundary factors, translate rho by the actual
rational boundary root, verify inverse translation, and certify full
minimum-weight assignments with their dual inequalities.  One further
phi power, if needed, is certified by an exact QQ regular-representation
kernel with complete original K-row products.  No determinant or old
projection is recomputed; only the fixed original entries are used.
Finally compute the NEW full modular quotient/gcd/Bezout product.
120 seconds /1 GiB, same three exact saved-curve JSON dependencies.
"""
import time,json,hashlib,base64,zlib,signal,resource
from pathlib import Path
from flint import fmpq,fmpq_poly,fmpq_mpoly_ctx,nmod_poly,fmpq_mat
from math import comb
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
def old_mod(data,sha,expected_sha,degree):
 raw=zlib.decompress(base64.b64decode(data))
 assert hashlib.sha256(raw).hexdigest()==sha
 p=nmod_poly(json.loads(raw),1009)
 assert p.degree()==degree and hashlib.sha256(str(p).encode()).hexdigest()==expected_sha
 return p
rrec=inputG["full_fixed_mod1009_resultant"]
srec=inputH["fixed_mod_resultant"]
grec=inputH["actual_common_mod_input"]
oldR=old_mod(rrec["fullCoefficientsData"],rrec["fullCoefficientsPayloadSha256"],
 "f4505a726a6c2691ac52b92ec424160f7cc748d6a9b17751ce8b2f9f3f0eaa85",2033)
oldS=old_mod(srec["fullCoefficientsData"],srec["fullCoefficientsPayloadSha256"],
 "060c2f63b871fec6e649ce3bdfbf29612df9402b07c3c4d381245f639edb8e12",2050)
oldg=nmod_poly(grec["coefficientsAscending"],1009)
assert oldg.degree()==168
assert oldR%oldg==0 and oldS%oldg==0

checks={"QQTranslationCoefficientProducts":0,"QQPhiDivisionProducts":0,
        "QQScaleDivisionProducts":0,"QQModPhiRemainderProducts":0,
        "fullQQRegularKernelProducts":0,"fullKKernelProducts":0}
def poly_rho_coeffs(p):
 out=[fmpq_poly([]) for _ in range(int(p.degrees()[0])+1)]
 for (i,j),c in p.to_dict().items():
  row=[fmpq(0)]*(int(j)+1);row[int(j)]=c
  out[int(i)]=out[int(i)]+fmpq_poly(row)
 return out
def translate(a,r):
 out=[fmpq_poly([]) for _ in a]
 for i,p in enumerate(a):
  for j in range(i+1):out[j]=out[j]+p*(comb(i,j)*r**(i-j))
 return out
def hungarian(cost):
 n=len(cost);big=10**18
 u=[0]*(n+1);v=[0]*(n+1);p=[0]*(n+1);way=[0]*(n+1)
 for i in range(1,n+1):
  p[0]=i;j0=0;mv=[big]*(n+1);used=[False]*(n+1)
  while True:
   used[j0]=True;i0=p[j0];delta=big;j1=0
   for j in range(1,n+1):
    if not used[j]:
     cur=cost[i0-1][j-1]-u[i0]-v[j]
     if cur<mv[j]:mv[j]=cur;way[j]=j0
     if mv[j]<delta:delta=mv[j];j1=j
   assert j1
   for j in range(n+1):
    if used[j]:u[p[j]]+=delta;v[j]-=delta
    else:mv[j]-=delta
   j0=j1
   if p[j0]==0:break
  while True:
   j1=way[j0];p[j0]=p[j1];j0=j1
   if j0==0:break
 matching=[0]*n
 for j in range(1,n+1):matching[p[j]-1]=j-1
 a=u[1:];b=v[1:]
 assert all(a[i]+b[j]<=cost[i][j] for i in range(n) for j in range(n))
 value=sum(cost[i][matching[i]] for i in range(n))
 assert value==sum(a)+sum(b)
 return value,a,b,matching
pF,pG=poly_rho_coeffs(F),poly_rho_coeffs(G)
assert [len(pF)-1,len(pG)-1]==[26,31]
cases=[("lambda_half",fmpq_poly([fmpq(-1,2),1]),fmpq(-1),10),
       ("genuine_H6",fmpq_poly([fmpq(5,64),fmpq(39,80),fmpq(63,80),
                              fmpq(-7,10),fmpq(-9,4),fmpq(3,5),1]),fmpq(3),2)]
lower_certificates=[];qqproduct=fmpq_poly([1]);barproduct=nmod_poly([1],1009)
def mod1009(p):
 cc=[]
 for i in range(p.degree()+1):
  c=p[i];den=int(c.denominator)%1009;assert den
  cc.append(int(c.numerator)%1009*pow(den,-1,1009)%1009)
 return nmod_poly(cc,1009)
for label,phi,rho0,target in cases:
 f=translate(pF,rho0);g=translate(pG,rho0)
 assert translate(f,-rho0)==pF and translate(g,-rho0)==pG
 checks["QQTranslationCoefficientProducts"]+=len(f)+len(g)
 m,n=len(f)-1,len(g)-1;size=m+n
 assert [m,n,size]==[26,31,57]
 zero=fmpq_poly([]);matrix=[[zero]*size for _ in range(size)]
 for i in range(n):
  for j in range(m+1):matrix[i][i+j]=f[j]
 for i in range(m):
  for j in range(n+1):matrix[n+i][i+j]=g[j]
 deg=int(phi.degree())
 zero_cost=size*(max(int(p.degree()) for p in f+g)+1)+1
 cache={}
 def valuation(pp):
  if not pp:return zero_cost
  key=str(pp)
  if key in cache:return cache[key]
  count=0;cur=pp
  while cur:
   q,rem=divmod(cur,phi);assert q*phi+rem==cur
   checks["QQPhiDivisionProducts"]+=1
   if rem:break
   cur=q;count+=1
  cache[key]=count;return count
 costs=[[valuation(pp) for pp in row] for row in matrix]
 E,ar,bc0,matching=hungarian(costs)
 assert all(matrix[i][matching[i]] for i in range(size))
 assert E<=target,("contradicts already-paid complete mod upper multiplicity",label,E,target)
 say("new_exact_translated_fixed_Sylvester_phi_assignment",
     factor=label,phiCoefficients=[str(phi[i]) for i in range(deg+1)],
     rhoTranslation=str(rho0),fixedRhoDegrees=[26,31],matrixSize=57,
     trueQQValuationLowerBound=E,knownCompleteMod1009Multiplicity=target,
     rowDual=ar,columnDual=bc0,perfectMatching=matching,
     allDualInequalitiesAndMatchedEqualityReturned=True,
     exactTranslationAndInverseTranslationReturned=True)
 proved=E;kernel_info=None
 if E<target:
  # Over QQ[lambda], the displayed Laurent diagonal equivalence is
  # exact.  Every resulting entry is still a polynomial by the dual
  # inequalities, so det(original)=phi^E det(current).
  reduced=[]
  for i in range(size):
   row=[]
   for j in range(size):
    pp=matrix[i][j];shift=ar[i]+bc0[j]
    if shift>=0:
     pw=phi**shift;q,rem=divmod(pp,pw);assert not rem and q*pw==pp
     scaled=q
    else:
     pw=phi**(-shift);scaled=pp*pw;assert scaled==pp*pw
    checks["QQScaleDivisionProducts"]+=1
    q,rem=divmod(scaled,phi);assert q*phi+rem==scaled
    checks["QQModPhiRemainderProducts"]+=1;row.append(rem)
   reduced.append(row)
  # Exact regular representation of the field QQ[lambda]/phi.
  # Both phi's are already exact irreducible QQ factors.  A nonzero
  # QQ nullvector produces a nonzero K vector; its complete product
  # is separately checked in K. Thus det(current)=0 mod phi.
  N=size*deg
  table=[[fmpq(0)]*N for _ in range(N)]
  powers=[fmpq_poly([0]*j+[1]) for j in range(deg)]
  for i in range(size):
   for j in range(size):
    pp=reduced[i][j]
    for h,pw in enumerate(powers):
     entry=(pp*pw)%phi
     for k in range(deg):table[i*deg+k][j*deg+h]=entry[k]
  B=fmpq_mat(table);rr,rank=B.rref()
  rank=int(rank)
  if rank<N:
   pivots=[]
   for i in range(rank):
    pivot=next(j for j in range(N) if rr[i,j])
    assert rr[i,pivot]==1;pivots.append(pivot)
   free=next(j for j in range(N) if j not in set(pivots))
   vv=[fmpq(0)]*N;vv[free]=fmpq(1)
   for i,pivot in enumerate(pivots):vv[pivot]=-rr[i,free]
   col=fmpq_mat(N,1,vv)
   assert B*col==fmpq_mat(N,1,[0]*N)
   checks["fullQQRegularKernelProducts"]+=1
   kv=[fmpq_poly(vv[i*deg:(i+1)*deg]) for i in range(size)]
   assert any(kv)
   for row in reduced:
    value=sum((p*x for p,x in zip(row,kv)),zero)%phi
    assert not value
    checks["fullKKernelProducts"]+=1
   proved=E+1
   kernel_info=dict(regularRepresentationDimension=N,actualQQRank=rank,
                    freeColumn=free,
                    kernelVectorSha256=hashlib.sha256(str(vv).encode()).hexdigest(),
                    completeQQMatrixTimesKernelReturned=True,
                    all57OriginalKRowTimesKernelReturned=True)
  else:
   kernel_info=dict(regularRepresentationDimension=N,actualQQRank=rank,
                    currentDeterminantNonzeroModuloExactQQPhi=True)
  say("new_exact_QQ_regular_kernel_extra_phi_power",
      factor=label,assignmentLowerBound=E,
      provedQQValuationLowerBound=proved,knownModUpperMultiplicity=target,
      exactCertificate=kernel_info)
 assert proved<=target
 if proved==target:
  status="exact QQ multiplicity equals complete mod upper bound"
 else:
  status="proved QQ lower bound only; no higher power claimed"
 qqproduct*=phi**proved;barproduct*=mod1009(phi)**proved
 lower_certificates.append(dict(factor=label,degree=deg,power=proved,
                                target=target,status=status,
                                kernel=kernel_info))
# This is a NEW exact full modular quotient and Bezout operation.
# It does not assume gcd(R/P,S)=old_g/P.
quot,rem=divmod(oldR,barproduct)
assert rem==0 and quot*barproduct==oldR
gg,aa,bb=quot.xgcd(oldS)
assert aa*quot+bb*oldS==gg
say("complete_new_true_QQ_local_divisibility_and_actual_modular_quotient",
    certificates=lower_certificates,
    totalProvedQQRemovedDegree=int(qqproduct.degree()),
    newMonicQQRQuotientDegree=2033-int(qqproduct.degree()),
    fullNewModRQuotientDegree=int(quot.degree()),
    completeModOldSDegree=int(oldS.degree()),
    newActualFullModGcdDegree=int(gg.degree()),
    newActualFullModGcdCoefficients=[int(gg[j]) for j in range(gg.degree()+1)],
    newBezoutDegrees=[int(aa.degree()),int(bb.degree())],
    completeNewBezoutProductReturned=True,
    allChecks=checks,
    finitePointBoundRequiresSeparateCompleteQQFiberExclusions=True,
    wholePhiFaceExcluded=False,ordinaryISPClaim=False)

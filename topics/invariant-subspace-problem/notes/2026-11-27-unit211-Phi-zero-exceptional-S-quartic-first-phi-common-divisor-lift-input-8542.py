#!/usr/bin/env python3
"""NEW same-source FIRST PHI LIFT on the excluded entire M_J quartic.
Use the already saved common g4 but read the actual original lambda
coefficients of F and G to form their FIRST phi errors. Solve ONE
32-by-16 QQ system for h modulo g4, giving a common monic
H=g4+phi*h only if both equations actually return. Perform full
monic F/H and G/H division modulo phi^2. Four resulting independent
original 57-column vectors have whole images divisible by phi^2,
paying true QQ phi^8. Only then take the NEW full R quotient/Gauss.
No old 88/208 rank, 160-value, cofactor, or former kernel input rerun.
120 seconds /1 GiB. Same four exact JSON inputs as 6e5d91a0.
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



phi=fmpq_poly([fmpq(916,420),fmpq(-3084,420),fmpq(3663,420),
                 fmpq(-1884,420),1])
e=4
# Irreducibility of this exact phi and the whole original quartic fiber
# exclusion were proved by b7116bba; neither input is repeated here.
kzero=fmpq_poly([]);kone=fmpq_poly([1])
checks={"QQPhiDivisionProducts":0,"QQFieldInverseProducts":0,
        "QQRhoDivisionProducts":0,"QQNamedBaseInverseProducts":0,
        "exactFormalOriginalReductionProducts":0}
def kk(p):
 if not isinstance(p,fmpq_poly):p=fmpq_poly([p])
 q,r=divmod(p,phi);assert q*phi+r==p
 checks["QQPhiDivisionProducts"]+=1
 return r
inverse_cache={}
def ki(p):
 p=kk(p);assert p
 key=str(p)
 if key in inverse_cache:return inverse_cache[key]
 g,s,t=p.xgcd(phi);assert s*p+t*phi==g and g.degree()==0
 ans=kk(s*(1/g[0]));assert kk(ans*p)==kone
 checks["QQFieldInverseProducts"]+=1;inverse_cache[key]=ans
 return ans
def kt(a):
 out=[kk(p) for p in a]
 while out and not out[-1]:out.pop()
 return out
def ka(a,b):
 out=[kzero]*max(len(a),len(b))
 for i,v in enumerate(a):out[i]=out[i]+v
 for i,v in enumerate(b):out[i]=out[i]+v
 return kt(out)
def kn(a):return kt([-v for v in a])
def ks(a,b):return ka(a,kn(b))
def km(a,b):
 if not a or not b:return []
 out=[kzero]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):out[i+j]=out[i+j]+x*y
 return kt(out)
def kd(a,b):
 a=kt(a);b=kt(b);assert b;original=list(a)
 q=[kzero]*max(0,len(a)-len(b)+1);iv=ki(b[-1])
 while a and len(a)>=len(b):
  shift=len(a)-len(b);c=kk(a[-1]*iv);q[shift]=kk(q[shift]+c)
  for j,v in enumerate(b):a[shift+j]=kk(a[shift+j]-c*v)
  a=kt(a)
 q=kt(q)
 assert ka(km(q,b),a)==original
 checks["QQRhoDivisionProducts"]+=1
 return q,a
def monic(a):
 a=kt(a)
 return [kk(x*ki(a[-1])) for x in a] if a else []
def kgcd(a,b,label):
 a=kt(a);b=kt(b);steps=0
 while b:
  q,r=kd(a,b);a,b=b,r;steps+=1
  say("new_exact_QQ_rho_gcd_step",pair=label,step=steps,
      divisorDegree=len(a)-1,nextRemainderDegree=len(b)-1)
 return monic(a)
def kxgcd(a,b):
 a=kt(a);b=kt(b);oa=list(a);ob=list(b)
 s0,s1=[kone],[];t0,t1=[],[kone]
 while b:
  q,r=kd(a,b);a,b=b,r
  s0,s1=s1,ks(s0,km(q,s1));t0,t1=t1,ks(t0,km(q,t1))
 assert ka(km(s0,oa),km(t0,ob))==a
 if a:
  iv=ki(a[-1]);a=[kk(x*iv) for x in a]
  s0=[kk(x*iv) for x in s0];t0=[kk(x*iv) for x in t0]
 assert ka(km(s0,oa),km(t0,ob))==a
 return a,s0,t0
def in_rho(p):
 out=[kzero]*(int(p.degrees()[0])+1)
 for (i,j),c in p.to_dict().items():
  row=[fmpq(0)]*(int(j)+1);row[int(j)]=c
  out[int(i)]=out[int(i)]+fmpq_poly(row)
 return kt(out)
saved=dependency(
 "2026-11-27-unit211-Phi-zero-exceptional-whole-S-quartic-gcd-and-original-values-exact-input-8542.json",
 "a4647a123f3ba072003a658217b0704cd2858ee8e4ae1b5060a9cdd44e5fad8d")
assert saved["producer"]["source_sha256"]=="b7116bbaeba341aa5356aae2a4ad2a3516f29e896b62f14d49384210272b7d82"
assert saved["entireFiberExcluded"] is True
assert saved["qqPhiMultiplicityLowerBound"]==4
assert saved["constantFieldPhiAscending"]==[str(phi[i]) for i in range(e+1)]
g4=[kk(fmpq_poly([fmpq(c) for c in cc])) for cc in saved["fullOriginalSameRhoGcd"]["coefficientsAscending"]]
assert len(g4)==5 and g4[-1]==kone
vF,vG=in_rho(F),in_rho(G)
assert [len(vF)-1,len(vG)-1]==[26,31]
qF,rF=kd(vF,g4);qG,rG=kd(vG,g4)
assert not rF and not rG
assert km(qF,g4)==vF and km(qG,g4)==vG
assert [len(qF)-1,len(qG)-1]==[22,27]

# NEW data: first phi-adic coefficient differences of the ACTUAL F,G,
# not just their already examined residues modulo phi.
def plain_trim(v):
 v=list(v)
 while v and not v[-1]:v.pop()
 return v
def plain_add(a,b):
 out=[kzero]*max(len(a),len(b))
 for j,c in enumerate(a):out[j]=out[j]+c
 for j,c in enumerate(b):out[j]=out[j]+c
 return plain_trim(out)
def plain_sub(a,b):return plain_add(a,[-c for c in b])
def plain_mul(a,b):
 if not a or not b:return []
 out=[kzero]*(len(a)+len(b)-1)
 for i,c in enumerate(a):
  for j,d in enumerate(b):out[i+j]=out[i+j]+c*d
 return plain_trim(out)
def raw_rho(p):
 out=[kzero]*(int(p.degrees()[0])+1)
 for (i,j),c in p.to_dict().items():
  cc=[fmpq(0)]*(int(j)+1);cc[int(j)]=c
  out[int(i)]=out[int(i)]+fmpq_poly(cc)
 return plain_trim(out)
rawF,rawG=raw_rho(F),raw_rho(G)
phi_divisions=0
def first_error(original,cofactor):
 global phi_divisions
 difference=plain_sub(original,plain_mul(g4,cofactor));out=[]
 for c in difference:
  q,r=divmod(c,phi);assert not r and q*phi==c
  phi_divisions+=1;out.append(kk(q))
 return kt(out)
EF,EG=first_error(rawF,qF),first_error(rawG,qG)
def cr(p):return kd(p,g4)[1] if len(kt(p))>=5 else kt(p)
fbar,gbar,efbar,egbar=[cr(p) for p in [qF,qG,EF,EG]]
def cvec(p):
 p=kt(p);assert len(p)<=4
 out=[]
 for r in range(4):
  c=p[r] if r<len(p) else kzero
  out.extend(c[j] for j in range(4))
 return out
columns=[]
for r in range(4):
 for j in range(4):
  v=[kzero]*r+[fmpq_poly([0]*j+[1])]
  columns.append(cvec(cr(km(fbar,v)))+cvec(cr(km(gbar,v))))
assert len(columns)==16 and all(len(c)==32 for c in columns)
rhs=cvec(efbar)+cvec(egbar)
augmented=[[columns[j][i] for j in range(16)]+[rhs[i]] for i in range(32)]
say("new_actual_first_phi_error_common_divisor_lift_linear_input",
    rows=32,unknowns=16,augmentedColumns=17,
    sameUnknown="h in K[rho]/g4",
    actualEquations=["(F/g4)*h=E_F mod g4","(G/g4)*h=E_G mod g4"],
    trueQQOriginalPhiDivisionProducts=phi_divisions,
    old88And208MatricesNotRecomputed=True,
    noOriginalConstantValueReturnReplayed=True)
rr,rank=fmpq_mat(augmented).rref();rank=int(rank)
pivots=[]
for i in range(rank):
 p=next(j for j in range(17) if rr[i,j])
 assert rr[i,p]==1;pivots.append(p)
if 16 in pivots:
 say("accurate_new_full_common_divisor_first_phi_lift_inconsistent",
     augmentedQQRank=rank,
     noFullDegreeFourCommonDivisorModuloPhiSquaredProduced=True,
     exactQQPhiEightNotClaimed=True,
     existing112BoundUnchanged=True,
     noInferenceAgainstPartialHigherOrderKernelLifts=True,
     ordinaryISPClaim=False)
 raise SystemExit(0)
solution=[fmpq(0)]*16
for i,p in enumerate(pivots):solution[p]=rr[i,16]
assert all(sum((row[j]*solution[j] for j in range(16)),fmpq(0))==row[16] for row in augmented)
h=[fmpq_poly(solution[4*r:4*r+4]) for r in range(4)]
h=kt(h)
assert len(h)<=4
assert cr(ks(km(fbar,h),efbar))==[]
assert cr(ks(km(gbar,h),egbar))==[]
lifted=[g4[i]+phi*(h[i] if i<len(h) else kzero) for i in range(5)]
assert lifted[-1]==kone
say("complete_new_same_source_QQ_first_phi_common_divisor_lift",
    actualQQRank=rank,
    all32OriginalLinearEquationsMultipliedBack=True,
    hAscending=[[str(c[j]) for j in range(4)] for c in h],
    liftedMonicRhoDegree=4,
    identity="H=g4+phi*h, with the SAME h for full original F and G",
    allFourLambdaEmbeddingsRetained=True)
phi2=phi*phi;phi2_divisions=0
def mod2(c):
 global phi2_divisions
 q,r=divmod(c,phi2);assert q*phi2+r==c
 phi2_divisions+=1
 return r
def normalized2(v):return plain_trim([mod2(c) for c in v])
def full_phi2_zero(v):
 global phi2_divisions
 for c in v:
  q,r=divmod(c,phi2);assert not r and q*phi2==c
  phi2_divisions+=1
def divide_by_lift(original):
 a=normalized2(original);b=normalized2(lifted);assert b[-1]==kone
 q=[kzero]*max(0,len(a)-len(b)+1)
 while a and len(a)>=len(b):
  shift=len(a)-len(b);c=a[-1]
  q[shift]=mod2(q[shift]+c)
  for j,d in enumerate(b):a[shift+j]=mod2(a[shift+j]-c*d)
  a=plain_trim(a)
 q=normalized2(q);a=normalized2(a)
 full_phi2_zero(plain_sub(original,plain_add(plain_mul(q,lifted),a)))
 return q,a
qF2,rF2=divide_by_lift(rawF);qG2,rG2=divide_by_lift(rawG)
assert not rF2 and not rG2
assert kt(qF2)==qF and kt(qG2)==qG
assert [len(qF2)-1,len(qG2)-1]==[22,27] and kk(qF2[-1])
say("complete_new_full_original_FG_monic_divisions_modulo_phi_squared",
    originalRhoDegrees=[26,31],liftedCommonRhoDegree=4,
    quotientRhoDegrees=[22,27],
    bothCompleteOriginalRemaindersZero=True,
    everyQQPhiSquaredDivisionProductReturned=True,
    noParameterOrNormInverseInTheseMonicDivisions=True,
    moduloPhiRecoversTheExactPreviouslyProvedOriginalCofactors=True)
kernel=[]
for j in range(4):
 a=[kzero]*j+qG2;b=[kzero]*j+[-c for c in qF2]
 assert len(a)<=31 and len(b)<=26
 out=plain_add(plain_mul(a,rawF),plain_mul(b,rawG))
 assert len(out)<=57
 full_phi2_zero(out+[kzero]*(57-len(out)))
 kernel.append(a+[kzero]*(31-len(a))+b+[kzero]*(26-len(b)))
say("complete_new_original_57_kernel_columns_have_phi_squared_products",
    originalFixedRhoDegrees=[26,31],originalFixedOrder=57,
    actualLiftedColumns=4,eachEntireColumnImageDivisibleByPhiPower=2,
    moduloPhiIndependence="the F/g4 blocks have distinct top rho degrees and nonzero leading coefficient",
    exactLocalBasisCompletionThereforeGivesQQPhiPower=8,
    entireOriginal57CoefficientProductsReturned=True,
    QQPhiSquaredDivisionProducts=phi2_divisions,
    kernelSha256=hashlib.sha256(str(kernel).encode()).hexdigest())
def fixed_mod1009(p):
 aa=[]
 for i in range(p.degree()+1):
  c=p[i];d=int(c.denominator)%1009;assert d
  iv=pow(d,-1,1009);assert d*iv%1009==1
  aa.append(int(c.numerator)%1009*iv%1009)
 return nmod_poly(aa,1009)
def read_complete_mod(rec,expected_sha,expected_degree):
 raw=zlib.decompress(base64.b64decode(rec["fullCoefficientsData"]))
 assert hashlib.sha256(raw).hexdigest()==rec["fullCoefficientsPayloadSha256"]
 pp=nmod_poly(json.loads(raw),1009)
 assert pp.degree()==expected_degree
 assert hashlib.sha256(str(pp).encode()).hexdigest()==expected_sha
 return pp
oldR=read_complete_mod(inputG["full_fixed_mod1009_resultant"],
 "f4505a726a6c2691ac52b92ec424160f7cc748d6a9b17751ce8b2f9f3f0eaa85",2033)
oldS=read_complete_mod(inputH["fixed_mod_resultant"],
 "060c2f63b871fec6e649ce3bdfbf29612df9402b07c3c4d381245f639edb8e12",2050)
temp=oldR;mod_multiplicity=0;phimod=fixed_mod1009(phi)
while True:
 quotient,remainder=divmod(temp,phimod)
 if remainder:break
 assert quotient*phimod==temp
 mod_multiplicity+=1;temp=quotient
assert mod_multiplicity==8
ph1=fmpq_poly([fmpq(-1,2),1])
ph6=fmpq_poly([fmpq(5,64),fmpq(39,80),fmpq(63,80),
                 fmpq(-7,10),fmpq(-9,4),fmpq(3,5),1])
phD=fmpq_poly([fmpq(1,32),fmpq(-3,16),fmpq(27,32),fmpq(-17,8),
                 fmpq(27,8),-3,1])
total=ph1**10*ph6**2*phD**3*phi**8
newR,remainder=divmod(oldR,fixed_mod1009(total))
assert not remainder and newR*fixed_mod1009(total)==oldR and newR.degree()==1961
gcdR,aa,bb=newR.xgcd(oldS)
assert aa*newR+bb*oldS==gcdR
say("complete_new_actual_QQ_phi_eight_and_full_1961_original_Gauss_return",
    exactQQPhiMultiplicity=8,
    upperBoundUsesActualCompleteOriginalMod1009R=True,
    lowerBoundUsesFourSameSourcePhiSquaredKernelColumns=True,
    wholeQuarticOriginalFiberPreviouslyExcludedByB711=True,
    totalTrueQQFactorDegree=int(total.degree()),
    actualFullRQuotientDegree=int(newR.degree()),
    actualFullSDegree=int(oldS.degree()),
    actualNewFullGcdDegree=int(gcdR.degree()),
    actualNewFullGcdCoefficients=[int(gcdR[i]) for i in range(gcdR.degree()+1)],
    bezoutDegrees=[int(aa.degree()),int(bb.degree())],
    completeNewQuotientAndBezoutProductsReturned=True,
    strictDifferentOrderedBasePointBound=int(gcdR.degree()),
    noVerticalFibersByPreviouslyProvedF26Irreducibility=True,
    BCSwappedChartNotMergedIntoSameBound=True,
    wholeExceptionalBranchExcluded=gcdR.degree()==0,
    ordinaryISPClaim=False)
signal.alarm(0)

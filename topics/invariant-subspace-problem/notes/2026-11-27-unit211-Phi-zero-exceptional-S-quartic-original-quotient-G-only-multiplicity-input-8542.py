#!/usr/bin/env python3
"""NEW quotient-G-only original linear input on the already excluded M_J fiber.
Read the saved exact monic original F/G/H rho-quartic g4 from b711.
Form ONLY F/g4 and G/g4; a NEW 88-by-88 QQ image in K[rho]/(F/g4)
recovers their full common factor. Actual short products and image rank
pay the exact gcd degree; explicit original 57-column kernel vectors
then pay a true QQ phi multiplicity lower bound. The full mod R gives
only the upper bound. New actual R quotient/Gauss is run only if the
QQ lower bound has increased. No old 208-by-104 combined matrix,
160 value-algebra matrix, cofactor, full resultant, or phi kernel gate
is rerun. 120 seconds /1 GiB. Four saved exact JSON dependencies.
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
say("new_original_quotients_by_previously_saved_same_source_quartic",
    actualOriginalRhoDegrees=[26,31],savedCommonDegree=4,
    newQuotientRhoDegrees=[22,27],
    fullOriginalShortDivisionProductsReturned=True,
    old208By104CombinedMatrixNotRecomputed=True,
    noPreviousOriginalValueMatrixRecomputed=True)
mf=monic(qF);assert mf[-1]==kone
assert [kk(c*qF[-1]) for c in mf]==qF
_,cur=kd(qG,mf)
columns=88
lpowers=[fmpq_poly([0]*i+[1]) for i in range(e)]
qqrows=[]
for rpower in range(22):
 for lpower in range(e):
  cc=[kk(c*lpowers[lpower]) for c in cur]
  row=[]
  for rpower0 in range(21,-1,-1):
   c=cc[rpower0] if rpower0<len(cc) else kzero
   row.extend(c[i] for i in range(e))
  assert len(row)==columns;qqrows.append(row)
 if rpower+1<22:_,cur=kd([kzero]+cur,mf)
assert len(qqrows)==88
say("new_original_quotient_G_only_QQ_linear_image_built",
    rows=88,columns=88,
    originalSources="rho^j lambda^i (G/g4) modulo the actual monic original quotient F/g4",
    noOldCombinedRankOrSylvesterKernelReplayed=True,
    completeQQRemainderProductsReturned=True)
linear=fmpq_mat(qqrows)
red,rank=linear.rref();rank=int(rank)
assert rank%e==0
extra_degree=22-rank//e
pivots=[]
for i in range(rank):
 p=next(j for j in range(columns) if red[i,j])
 assert red[i,p]==1;pivots.append(p)
assert pivots==list(range(rank))
if extra_degree==22:
 h=list(mf)
else:
 target_column=(21-extra_degree)*e
 target_row=pivots.index(target_column)
 h=[kzero]*22
 for column in range(columns):
  rp=21-column//e;lpow=column%e;c=red[target_row,column]
  if c:
   term=[fmpq(0)]*(lpow+1);term[lpow]=c
   h[rp]=h[rp]+fmpq_poly(term)
 h=kt(h)
assert len(h)==extra_degree+1 and h[-1]==kone
for v in [qF,qG]:
 quotient,remainder=kd(v,h)
 assert not remainder and km(quotient,h)==v
full_gcd=km(g4,h)
assert len(full_gcd)==5+extra_degree and full_gcd[-1]==kone
whole_degree=4+extra_degree
qFF,remF=kd(vF,full_gcd);qGG,remG=kd(vG,full_gcd)
assert not remF and not remG
assert km(qFF,full_gcd)==vF and km(qGG,full_gcd)==vG
say("complete_new_true_QQ_original_FG_gcd_from_quotient_G_only_linear_input",
    newOriginalQQRank=rank,extraCommonRhoDegree=extra_degree,
    fullOriginalFGCommonRhoDegree=whole_degree,
    extraMonicGcdAscending=[[str(c[i]) for i in range(e)] for c in h],
    completeOriginalFGMonicGcdAscending=[[str(c[i]) for i in range(e)] for c in full_gcd],
    exactFullOriginalQuotientAndOriginalFGProductsReturned=True,
    degreeEqualityPaidByActual88DimensionalQQImageRank=True,
    allFourLambdaEmbeddingsRetained=True,
    notAProperCommonDivisorMistakenForFullRootCoverage=True)
kernel=[]
for j in range(whole_degree):
 a=[kzero]*j+qGG;b=[kzero]*j+kn(qFF)
 assert len(a)<=31 and len(b)<=26
 assert not ka(km(a,vF),km(b,vG))
 kernel.append(a+[kzero]*(31-len(a))+b+[kzero]*(26-len(b)))
assert qFF
say("complete_new_true_QQ_fixed_original_Sylvester_phi_lower_bound",
    originalFixedRhoDegrees=[26,31],originalOrder=57,
    independentOriginalKernelColumns=whole_degree,
    independence="shifted nonzero F/full_gcd blocks have distinct highest rho degrees",
    allOriginal57CoefficientKernelProductsReturned=True,
    trueQQPhiMultiplicityLowerBound=whole_degree,
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
temp=oldR;mod_multiplicity=0;phimod=fixed_mod1009(phi)
while True:
 quotient,remainder=divmod(temp,phimod)
 if remainder:break
 assert quotient*phimod==temp
 mod_multiplicity+=1;temp=quotient
assert whole_degree<=mod_multiplicity
say("complete_new_original_FG_phi_valuation_interval",
    trueQQPhiMultiplicityLowerBound=whole_degree,
    fullOriginalMod1009PhiMultiplicityUpperBound=mod_multiplicity,
    exactQQPhiMultiplicityPaid=(whole_degree==mod_multiplicity),
    wholeOriginalQuarticFiberExclusionUsesAlreadyPublishedB711=True,
    noBareModularSupportLift=True)
if whole_degree>4:
 oldS=read_complete_mod(inputH["fixed_mod_resultant"],
  "060c2f63b871fec6e649ce3bdfbf29612df9402b07c3c4d381245f639edb8e12",2050)
 ph1=fmpq_poly([fmpq(-1,2),1])
 ph6=fmpq_poly([fmpq(5,64),fmpq(39,80),fmpq(63,80),
                  fmpq(-7,10),fmpq(-9,4),fmpq(3,5),1])
 phD=fmpq_poly([fmpq(1,32),fmpq(-3,16),fmpq(27,32),fmpq(-17,8),
                  fmpq(27,8),-3,1])
 total=ph1**10*ph6**2*phD**3*phi**whole_degree
 newR,remainder=divmod(oldR,fixed_mod1009(total))
 assert not remainder and newR*fixed_mod1009(total)==oldR
 assert newR.degree()==1993-e*whole_degree
 gcdR,aa,bb=newR.xgcd(oldS)
 assert aa*newR+bb*oldS==gcdR
 say("complete_new_actual_full_quotient_original_Gauss_return",
     allRemovedQQDivisibilityAndWholeFibersPaid=True,
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
else:
 say("accurate_new_G_only_quotient_input_no_extra_local_multiplicity",
     actualOriginalFGCommonRhoDegree=whole_degree,
     exactQQPhiEightNotYetPaid=True,
     existing112BoundNotChanged=True,
     noOldModularGaussInputReplayed=True,
     nextUnpaidObject="first phi-adic lift of the four genuine original kernel columns",
     ordinaryISPClaim=False)
signal.alarm(0)

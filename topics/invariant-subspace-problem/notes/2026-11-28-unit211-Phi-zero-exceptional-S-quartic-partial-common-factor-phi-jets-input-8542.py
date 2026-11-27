#!/usr/bin/env python3
"""NEW first obstruction and PARTIAL common-factor phi jets. Only the
frozen original F/G input and g4 construction is reused; no old 32x17,
88x88,208x104,160-value or cofactor computation is executed. The new
obstruction delta=(qG*EF-qF*EG) mod g4 determines a possible partial
factor. Retain its entire QQ field and do not assume it is squarefree.
Only if its complement is actually coprime, solve the smaller same-h
jet systems and perform full original monic divisions modulo phi^j.
Combine these d columns with 4-d old first-order columns, all 57
coefficient products returned, before paying any new QQ power. Fixed
120 seconds /1 GiB. Four frozen JSON inputs as the original first lift.
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

# NEW obstruction; its degree is at most three even though the original
# F and G have rho-degrees 26 and 31.
obstruction=kd(ks(km(qG,EF),km(qF,EG)),g4)[1]
assert obstruction
partial=kgcd(g4,obstruction,"NEW partial first-jet obstruction")
d=len(partial)-1
say("new_actual_partial_phi_obstruction",
    originalG4Degree=4,obstructionRhoDegree=len(obstruction)-1,
    partialCommonFactorDegree=d,
    obstructionAscending=[[str(c[j]) for j in range(4)] for c in obstruction],
    partialFactorAscending=[[str(c[j]) for j in range(4)] for c in partial],
    noOldFullCommonLiftSystemRecomputed=True,existing112BoundUnchanged=True)
if d==0:
 say("new_partial_obstruction_has_no_nonzero_kernel",
     entireFirstJetObstructionInvertible=True,
     noHigherQQPhiPowerPaid=True,existing112BoundUnchanged=True,
     ordinaryISPClaim=False)
 signal.alarm(0);raise SystemExit(0)
assert 0<d<4
complement,rem=kd(g4,partial);assert not rem and km(complement,partial)==g4
coprime=kgcd(partial,complement,"NEW partial factor versus exact complement")
if len(coprime)!=1:
 say("new_partial_factor_and_complement_not_coprime_retained",
     commonDegree=len(coprime)-1,noWholePartialJetClaim=True,
     existing112BoundUnchanged=True,ordinaryISPClaim=False)
 signal.alarm(0);raise SystemExit(0)
partialF,rf=kd(vF,partial);partialG,rg=kd(vG,partial)
assert not rf and not rg
assert km(partialF,partial)==vF and km(partialG,partial)==vG
assert [len(partialF)-1,len(partialG)-1]==[26-d,31-d]
def reduce_partial(v):return kd(v,partial)[1] if len(kt(v))>d else kt(v)
def small_vector(v):
 v=kt(v);assert len(v)<=d
 return [(v[r] if r<len(v) else kzero)[j] for r in range(d) for j in range(4)]
linear_columns=[]
for r in range(d):
 for j in range(4):
  v=[kzero]*r+[fmpq_poly([0]*j+[1])]
  linear_columns.append(small_vector(reduce_partial(km(partialF,v)))+
                        small_vector(reduce_partial(km(partialG,v))))
unknowns=4*d
assert len(linear_columns)==unknowns and all(len(c)==2*unknowns for c in linear_columns)
currentH=list(partial);currentF=list(partialF);currentG=list(partialG)
last_order=1;jet_divisions=0
def error_at_order(original,H,cofactor,power):
 global jet_divisions
 difference=plain_sub(original,plain_mul(H,cofactor));out=[]
 for c in difference:
  q,r=divmod(c,power);assert not r and q*power==c
  jet_divisions+=1;out.append(kk(q))
 return kt(out)
def exact_mod(c,modulus):
 global jet_divisions
 q,r=divmod(c,modulus);assert q*modulus+r==c
 jet_divisions+=1;return r
def exact_mod_vector(v,modulus):
 return plain_trim([exact_mod(c,modulus) for c in v])
def exact_multiple_vector(v,modulus):
 global jet_divisions
 for c in v:
  q,r=divmod(c,modulus);assert not r and q*modulus==c
  jet_divisions+=1
def original_monic_division(original,H,modulus):
 b=exact_mod_vector(H,modulus);assert b[-1]==kone
 a=exact_mod_vector(original,modulus)
 q=[kzero]*max(0,len(a)-len(b)+1)
 while a and len(a)>=len(b):
  shift=len(a)-len(b);cf=a[-1];q[shift]=exact_mod(q[shift]+cf,modulus)
  for j,c in enumerate(b):a[shift+j]=exact_mod(a[shift+j]-cf*c,modulus)
  a=plain_trim(a)
 q=exact_mod_vector(q,modulus);a=exact_mod_vector(a,modulus)
 exact_multiple_vector(plain_sub(original,plain_add(plain_mul(q,H),a)),modulus)
 return q,a

# The already established complete modular R gives v_phi(R)<=8.
# Do not assert a longer lift or a larger true QQ power than it permits.
for order in range(2,2+4//d):
 power=phi**(order-1)
 errF=reduce_partial(error_at_order(rawF,currentH,currentF,power))
 errG=reduce_partial(error_at_order(rawG,currentH,currentG,power))
 rhs=small_vector(errF)+small_vector(errG)
 augmented=[[linear_columns[j][i] for j in range(unknowns)]+[rhs[i]]
            for i in range(2*unknowns)]
 rr,rank=fmpq_mat(augmented).rref();rank=int(rank);pivots=[]
 for i in range(rank):
  pv=next(j for j in range(unknowns+1) if rr[i,j])
  assert rr[i,pv]==1;pivots.append(pv)
 if unknowns in pivots:
  say("new_partial_common_divisor_next_jet_inconsistent",
      desiredPhiOrder=order,partialRhoDegree=d,augmentedQQRank=rank,
      rows=2*unknowns,unknowns=unknowns,lastCompletedOrder=last_order,
      noInferenceAgainstYetSmallerSubfactorJets=True)
  break
 solution=[fmpq(0)]*unknowns
 for i,pv in enumerate(pivots):solution[pv]=rr[i,unknowns]
 assert all(sum((row[j]*solution[j] for j in range(unknowns)),fmpq(0))==row[unknowns] for row in augmented)
 h=kt([fmpq_poly(solution[4*r:4*r+4]) for r in range(d)])
 assert len(h)<=d
 assert not reduce_partial(ks(km(partialF,h),errF))
 assert not reduce_partial(ks(km(partialG,h),errG))
 H=[(currentH[i] if i<len(currentH) else kzero)+power*(h[i] if i<len(h) else kzero)
    for i in range(d+1)]
 assert H[-1]==kone
 modulus=phi**order
 f,rf=original_monic_division(rawF,H,modulus)
 gg,rg=original_monic_division(rawG,H,modulus)
 assert not rf and not rg
 assert kt(f)==partialF and kt(gg)==partialG
 assert kt(H)==partial and [len(f)-1,len(gg)-1]==[26-d,31-d]
 currentH,currentF,currentG=H,f,gg;last_order=order
 say("new_full_original_partial_common_factor_phi_jet_returned",
     partialRhoDegree=d,actualPhiOrder=order,
     rows=2*unknowns,unknowns=unknowns,actualQQRank=rank,
     everyOriginalLinearEquationMultipliedBack=True,
     fullFAndGMonicDivisionRemaindersZero=True,
     allFourLambdaEmbeddingsRetained=True,
     exactHAscending=[[str(c[j]) for j in range(4*order)] for c in H],
     noPhysicalOrLambdaLeadingFactorInverted=True)
paid=4+(last_order-1)*d
if paid==4:
 say("new_partial_jets_pay_no_additional_original_determinant_power",
     exactQQPhiMultiplicityLowerBound=4,actualModularUpperBound=8,
     existing112BoundUnchanged=True,ordinaryISPClaim=False)
 signal.alarm(0);raise SystemExit(0)
assert 4<paid<=8
kernel=[]
for j in range(4-d):
 a=[kzero]*j+qG;b=[kzero]*j+[-v for v in qF]
 out=plain_add(plain_mul(a,rawF),plain_mul(b,rawG))
 assert len(a)<=31 and len(b)<=26 and len(out)<=57
 exact_multiple_vector(out+[kzero]*(57-len(out)),phi)
 kernel.append(dict(order=1,vector=a+[kzero]*(31-len(a))+b+[kzero]*(26-len(b))))
for j in range(d):
 a=[kzero]*j+currentG;b=[kzero]*j+[-v for v in currentF]
 out=plain_add(plain_mul(a,rawF),plain_mul(b,rawG))
 assert len(a)<=31 and len(b)<=26 and len(out)<=57
 exact_multiple_vector(out+[kzero]*(57-len(out)),phi**last_order)
 kernel.append(dict(order=last_order,vector=a+[kzero]*(31-len(a))+b+[kzero]*(26-len(b))))
assert len(kernel)==4 and sum(c["order"] for c in kernel)==paid
# Modulo phi their rho multipliers are 1,...,rho^(3-d), followed by
# (g4/partial),...,rho^(d-1)(g4/partial). These have distinct degrees
# 0,...,3 and leading coefficient 1. The old F/g4 block is nonzero,
# hence all four 57-vectors are independent and extend to a local basis.
multipliers=[[kzero]*j+[kone] for j in range(4-d)]+[[kzero]*j+complement for j in range(d)]
assert [len(v)-1 for v in multipliers]==list(range(4))
assert all(v[-1]==kone for v in multipliers) and qF[-1]
for rec,mult in zip(kernel,multipliers):
 expectedA=km(mult,qG);expectedB=kn(km(mult,qF))
 assert kt(rec["vector"][:31])==expectedA and kt(rec["vector"][31:])==expectedB
say("new_mixed_original_57_kernel_columns_pay_true_QQ_power",
    originalFixedOrder=57,partialRhoDegree=d,partialPhiOrder=last_order,
    originalColumnOrders=[c["order"] for c in kernel],
    all57OriginalCoefficientProductsExactlyDivisible=True,
    moduloPhiIndependenceByDistinctMonicRhoDegrees=[0,1,2,3],
    exactQQPhiMultiplicityLowerBound=paid,
    localInvertibleBasisCompletionJustifiesTheDeterminantPower=True,
    exactJetDivisionProducts=jet_divisions,
    kernelSHA256=hashlib.sha256(str(kernel).encode()).hexdigest())
def fixed_mod1009(p):
 aa=[]
 for i in range(p.degree()+1):
  c=p[i];dd=int(c.denominator)%1009;assert dd
  iv=pow(dd,-1,1009);assert dd*iv%1009==1
  aa.append(int(c.numerator)%1009*iv%1009)
 return nmod_poly(aa,1009)
def read_complete_mod(rec,expected_sha,expected_degree):
 raw=zlib.decompress(base64.b64decode(rec["fullCoefficientsData"]))
 assert hashlib.sha256(raw).hexdigest()==rec["fullCoefficientsPayloadSha256"]
 pp=nmod_poly(json.loads(raw),1009);assert pp.degree()==expected_degree
 assert hashlib.sha256(str(pp).encode()).hexdigest()==expected_sha
 return pp
oldR=read_complete_mod(inputG["full_fixed_mod1009_resultant"],
 "f4505a726a6c2691ac52b92ec424160f7cc748d6a9b17751ce8b2f9f3f0eaa85",2033)
oldS=read_complete_mod(inputH["fixed_mod_resultant"],
 "060c2f63b871fec6e649ce3bdfbf29612df9402b07c3c4d381245f639edb8e12",2050)
temp=oldR;modpower=0;phimod=fixed_mod1009(phi)
while True:
 qq,rr=divmod(temp,phimod)
 if rr:break
 assert qq*phimod==temp
 temp=qq;modpower+=1
assert modpower==8
ph1=fmpq_poly([fmpq(-1,2),1])
ph6=fmpq_poly([fmpq(5,64),fmpq(39,80),fmpq(63,80),fmpq(-7,10),fmpq(-9,4),fmpq(3,5),1])
phD=fmpq_poly([fmpq(1,32),fmpq(-3,16),fmpq(27,32),fmpq(-17,8),fmpq(27,8),-3,1])
total=ph1**10*ph6**2*phD**3*phi**paid
newR,rr=divmod(oldR,fixed_mod1009(total))
assert not rr and newR*fixed_mod1009(total)==oldR
assert newR.degree()==2033-int(total.degree())
gcdR,aa,bb=newR.xgcd(oldS);assert aa*newR+bb*oldS==gcdR
say("new_partial_jet_original_determinant_and_complete_Gauss_return",
    exactQQPhiMultiplicityLowerBound=paid,actualModularUpperBound=8,
    exactQQPhiMultiplicity=(8 if paid==8 else None),
    wholePhiQuarticOriginalFiberAlreadyExcluded=True,
    trueQQFactorDegree=int(total.degree()),actualFullRQuotientDegree=int(newR.degree()),
    actualFullSDegree=int(oldS.degree()),actualFullGcdDegree=int(gcdR.degree()),
    actualFullGcdCoefficients=[int(gcdR[i]) for i in range(gcdR.degree()+1)],
    bezoutDegrees=[int(aa.degree()),int(bb.degree())],
    allOriginalQuotientAndBezoutProductsReturned=True,
    differentOrderedRhoLambdaBound=int(gcdR.degree()),
    verticalFibersExcludedByThePreviouslyProvedOriginalF26Irreducibility=True,
    BCSwappedChartNotMerged=True,wholeExceptionalBranchExcluded=gcdR.degree()==0,
    sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    ordinaryISPClaim=False)
signal.alarm(0)

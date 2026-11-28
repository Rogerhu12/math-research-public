#!/usr/bin/env python3
"""NEW common-zero input for the four CORRECTED Phi quadratic heads.
Only the three small, exactly factorized head polynomials are used.
A=0 is a complete polynomial substitution. B=0 is the entire monic
quadratic algebra; all coefficient-leading-zero and repeated fibers stay.
QQ[u] Bezout identities have explicit original F/B sources.
The final finite QQ algebra tests a power of the actual paid product,
not a norm inverse and not a modular vanishing claim.
No old wrong-Rbar source, old determinant or Gaussian is executed.
120 seconds / 1 GiB. Self-contained. Small receipts only.
"""
import hashlib,itertools,json,resource,signal,time
from flint import fmpq,fmpq_poly,fmpq_mpoly_ctx,fmpq_mat
began=time.perf_counter()
signal.alarm(120)
resource.setrlimit(resource.RLIMIT_AS,(1024**3,1024**3))
def say(stage,**kw):
 kw.update(stage=stage,seconds=time.perf_counter()-began)
 print(json.dumps(kw,sort_keys=True),flush=True)
ctx=fmpq_mpoly_ctx.get(("u","Q"),"lex")
u,Q=ctx.gens();zero=ctx.constant(0);one=ctx.constant(1)
U=fmpq_poly([0,1]);z=fmpq_poly([]);o=fmpq_poly([1])
def original_input_hash(p):
 # Exactly the original five-variable fixed factor convention.
 return hashlib.sha256(str(sorted((tuple(e)+(0,0,0),a)
                                  for e,a in p.to_dict().items())).encode()).hexdigest()
F8=(256*u**8 - 2560*u**7 - 416*u**6*Q + 11648*u**6 + 3104*u**5*Q - 31232*u**5 + 224*u**4*Q**2 - 10176*u**4*Q + 53760*u**4 - 1176*u**3*Q**2 + 18528*u**3*Q - 60672*u**3 - 54*u**2*Q**3 + 2344*u**2*Q**2 - 19424*u**2*Q + 43648*u**2 + 116*u*Q**3 - 2064*u*Q**2 + 10944*u*Q - 18176*u + Q**4 - 64*Q**3 + 672*Q**2 - 2560*Q + 3328)
assert original_input_hash(F8)=="e12cf1bbaf864cd9de2a01b033b2dce98ee6dda20b595d499f39f3c431a3682c"

F10=(128*u**10*Q + 512*u**10 - 512*u**9*Q - 7680*u**9 - 32*u**8*Q**2 - 3584*u**8*Q + 51200*u**8 - 1152*u**7*Q**2 + 38016*u**7*Q - 200704*u**7 - 120*u**6*Q**3 + 11648*u**6*Q**2 - 158208*u**6*Q + 514560*u**6 + 1568*u**5*Q**3 - 49088*u**5*Q**2 + 392064*u**5*Q - 904704*u**5 + 82*u**4*Q**4 - 7464*u**4*Q**3 + 117664*u**4*Q**2 - 633216*u**4*Q + 1106944*u**4 - 584*u**3*Q**4 + 17760*u**3*Q**3 - 172224*u**3*Q**2 + 674816*u**3*Q - 930816*u**3 - 21*u**2*Q**5 + 1384*u**2*Q**4 - 22624*u**2*Q**3 + 152064*u**2*Q**2 - 457984*u**2*Q + 514048*u**2 + 44*u*Q**5 - 1360*u*Q**4 + 14720*u*Q**3 - 74240*u*Q**2 + 179200*u*Q - 167936*u - 24*Q**5 + 480*Q**4 - 3840*Q**3 + 15360*Q**2 - 30720*Q + 24576)
assert original_input_hash(F10)=="fed662807af51d32a487e94de918bb79fec0a93775775351f1d2c59ac95d569b"

F9=(192*u**9*Q - 256*u**9 - 1536*u**8*Q + 1792*u**8 - 176*u**7*Q**2 + 5504*u**7*Q - 4608*u**7 + 1088*u**6*Q**2 - 10560*u**6*Q + 2560*u**6 + 68*u**5*Q**3 - 2464*u**5*Q**2 + 8320*u**5*Q + 14080*u**5 - 224*u**4*Q**3 + 1280*u**4*Q**2 + 8768*u**4*Q - 41216*u**4 - 9*u**3*Q**4 - 84*u**3*Q**3 + 4560*u**3*Q**2 - 30144*u**3*Q + 55296*u**3 - 32*u**2*Q**4 + 1040*u**2*Q**3 - 9408*u**2*Q**2 + 33536*u**2*Q - 41984*u**2 - 2*u*Q**5 + 100*u*Q**4 - 1280*u*Q**3 + 7040*u*Q**2 - 17920*u*Q + 17408*u + 3*Q**5 - 60*Q**4 + 480*Q**3 - 1920*Q**2 + 3840*Q - 3072)
assert original_input_hash(F9)=="75f45c262d856751b610ef4bb16502555d9e2f9e800d08c9d37769c67beb9c10"

Fs=[F8,F10,F9]
A=4*(u-1)**2-Q
B=-Q**2+(12*u**2-20*u+8)*Q-16*(u-1)**2
Bmon=-B
K=Q+4*u-4
L=Q-2*(u-1)*(u-2)
Mn=2*u*L-L**2-u**2*Q
physical_unit_product=Q*(1-Q)*(u-1)*K*L*Mn
exact_divisions=0;bezout_checks=0
def exact(a,b):
 global exact_divisions
 q,r=divmod(a,b);assert not r and q*b==a
 exact_divisions+=1;return q
def embed(p):
 return sum((ctx.constant(p[i])*u**i for i in range(p.degree()+1)),zero)
def gcd_with_source(ps):
 global bezout_checks
 g=z;tags=[z for _ in ps]
 for j,p in enumerate(ps):
  if not p:continue
  new,s,t=g.xgcd(p)
  assert s*g+t*p==new
  bezout_checks+=1
  tags=[s*x for x in tags];tags[j]=tags[j]+t;g=new
 if g:
  lc=g[g.degree()]
  g=g/lc;tags=[v/lc for v in tags]
 assert sum((a*b for a,b in zip(tags,ps)),z)==g
 bezout_checks+=1
 return g,tags
def info(p):
 return {"degree":int(p.degree()),"polynomial":str(p),
         "sha256":hashlib.sha256(str(p).encode()).hexdigest()}
def factor_return(p):
 if not p:return {"zero":True}
 c,fs=p.factor();back=fmpq_poly([c]);out=[]
 for f,e in fs:
  back=back*f**int(e);out.append({"power":int(e),**info(f)})
 assert back==p
 return {"constant":str(c),"factors":out,"fullProductReturned":True}
def substitute_Q(p,qp):
 return sum((fmpq_poly([a])*U**int(e[0])*qp**int(e[1])
             for e,a in p.to_dict().items()),z)
# Whole A curve: no division by a parameter leading coefficient.
qA=4*(U-1)**2
aFs=[substitute_Q(p,qA) for p in Fs]
aQuot=[exact(p-embed(v),A) for p,v in zip(Fs,aFs)]
ga,atags=gcd_with_source(aFs)
assert sum((embed(t)*(p-A*q) for t,p,q in zip(atags,Fs,aQuot)),zero)==embed(ga)
uA=substitute_Q(physical_unit_product,qA)
assert uA
aRemaining=ga;removed=[]
if aRemaining:
 while aRemaining.degree()>0:
  gg=aRemaining.gcd(uA)
  if gg.degree()==0:break
  aRemaining=exact(aRemaining,gg);removed.append(gg)
 aRemaining=aRemaining/aRemaining[aRemaining.degree()]
say("whole_A_original_head_branch",
    substitutedDegrees=[int(p.degree()) for p in aFs],
    originalThreeTermBezoutReturned=True,
    completeGCD=factor_return(ga),
    actualPaidProduct=info(uA),
    paidGCDRemovedFactors=[info(p) for p in removed],
    remainingCover=info(aRemaining),
    excludedUsingOnlyDeclaredPhysicalUnits=bool(aRemaining and aRemaining.degree()==0))
# Entire B algebra: Q^2=cQ-d, with c,d in QQ[u].
qc=12*U**2-20*U+8;qd=16*(U-1)**2
qcp=embed(qc);qdp=embed(qd)
assert Bmon==Q**2-qcp*Q+qdp
maxQ=max(int(p.degrees()[1]) for p in Fs)
powers=[(o,z),(z,o)]
for j in range(2,maxQ+1):
 b0,a0=powers[-1]
 powers.append((-qd*a0,b0+qc*a0))
affine=[];bQuot=[]
for p in Fs:
 b0=z;a0=z
 for e,c in p.to_dict().items():
  cj=fmpq_poly([c])*U**int(e[0]);rb,ra=powers[int(e[1])]
  b0=b0+cj*rb;a0=a0+cj*ra
 h=embed(b0)+embed(a0)*Q
 quo=exact(p-h,Bmon)
 affine.append((b0,a0));bQuot.append(quo)
# Each univariate necessary polynomial comes with a FULL original
# F8/F10/F9/B identity, including every leading-zero fiber.
necessary=[];original_sources=[]
for i,(b0,a0) in enumerate(affine):
 norm=b0*b0+qc*a0*b0+qd*a0*a0
 lin=embed(b0)+embed(a0)*Q
 mul=-embed(a0)*Q+embed(a0*qc+b0)
 btag=embed(a0*a0)-bQuot[i]*mul
 assert embed(norm)==Fs[i]*mul+Bmon*btag
 tags=[zero,zero,zero];tags[i]=mul
 necessary.append(norm);original_sources.append((tags,btag))
for i,j in itertools.combinations(range(3),2):
 bi,ai=affine[i];bj,aj=affine[j]
 cross=ai*bj-aj*bi
 tags=[zero,zero,zero];tags[i]=-embed(aj);tags[j]=embed(ai)
 btag=embed(aj)*bQuot[i]-embed(ai)*bQuot[j]
 assert embed(cross)==sum((x*y for x,y in zip(tags,Fs)),zero)+Bmon*btag
 necessary.append(cross);original_sources.append((tags,btag))
gb,btags=gcd_with_source(necessary)
combined=[zero,zero,zero];combinedB=zero
for tag,(src,btag) in zip(btags,original_sources):
 for j in range(3):combined[j]=combined[j]+embed(tag)*src[j]
 combinedB=combinedB+embed(tag)*btag
assert embed(gb)==sum((a*b for a,b in zip(combined,Fs)),zero)+Bmon*combinedB
say("whole_B_univariate_cover_from_original_rows",
    monicQuadraticKept=True,
    affineDegrees=[{"constant":int(b.degree()),"linear":int(a.degree())}
                   for b,a in affine],
    sixNecessaryDegrees=[int(p.degree()) for p in necessary],
    sixFullOriginalIdentitiesReturned=True,
    fullCombinedOriginalBezoutReturned=True,
    originalUCover=factor_return(gb),
    noNormOrCoefficientLeadingTermInverted=True)
closedB=False
if gb and gb.degree()==0:
 closedB=True
 say("whole_B_original_unit",exactOriginalOneReturned=True)
elif not gb:
 say("whole_B_retained",reason="all six univariate necessities vanish identically")
elif gb.degree()>64:
 say("whole_B_retained",reason="new complete finite algebra exceeds fixed 128-dimensional cap",
     coverDegree=int(gb.degree()))
else:
 # This whole finite QQ algebra contains ALL Q roots and u multiplicities.
 n=int(gb.degree());D=2*n
 def red(p):return p%gb
 def fm(x,y):
  b0,a0=x;b1,a1=y
  return (red(b0*b1-qd*a0*a1),red(b0*a1+a0*b1+qc*a0*a1))
 def power(x,k):
  out=(o,z)
  while k:
   if k&1:out=fm(out,x)
   k//=2
   if k:x=fm(x,x)
  return out
 def flat(x):return [x[j][i] for j in range(2) for i in range(n)]
 def feval(p):
  out=(z,z);ub=(U,z);qb=(z,o)
  for e,c in p.to_dict().items():
   term=fm(power(ub,int(e[0])),power(qb,int(e[1])))
   out=(red(out[0]+c*term[0]),red(out[1]+c*term[1]))
  return out
 basis=[(red(U**i),z) for i in range(n)]+[(z,red(U**i)) for i in range(n)]
 originalRows=[(red(b),red(a)) for b,a in affine]
 cols=[flat(fm(h,v)) for h in originalRows for v in basis]
 mat=fmpq_mat([[cols[j][i] for j in range(len(cols))] for i in range(D)])
 rr,rank=mat.rref()
 selected=[]
 for i in range(rank):
  selected.append(next(j for j in range(mat.ncols()) if rr[i,j]))
 assert len(selected)==rank
 upair=feval(physical_unit_product)
 target=flat(power(upair,D))
 if rank:
  basisMat=fmpq_mat([[cols[j][i] for j in selected] for i in range(D)])
  rt,rowrank=basisMat.transpose().rref();assert rowrank==rank
  rows=[next(j for j in range(D) if rt[i,j]) for i in range(rank)]
  sq=fmpq_mat([[basisMat[i,j] for j in range(rank)] for i in rows])
  inv=sq.inv()
  assert sq*inv==fmpq_mat([[int(i==j) for j in range(rank)] for i in range(rank)])
  assert inv*sq==fmpq_mat([[int(i==j) for j in range(rank)] for i in range(rank)])
  vec=inv*fmpq_mat([[target[i]] for i in rows])
  returned=basisMat*vec
  closedB=all(returned[i,0]==target[i] for i in range(D))
 else:closedB=not any(target)
 say("whole_B_true_finite_original_paid_power_target",
     originalFiniteAlgebraDimension=D,
     definingEquations=["full monic original u cover","whole monic B quadratic"],
     allPrimaryPowersKept=True,
     actualOriginalIdealMatrixRows=D,actualOriginalIdealMatrixColumns=3*D,
     actualRank=int(rank),remainingQuotientDimension=D-int(rank),
     target="(Q*(1-Q)*(u-1)*K*L*Mn)^(2*degree_u_cover)",
     targetPower=D,fullTargetColumnReturned=closedB,
     actualOriginalBasisColumnsUsed=selected,
     onlyRationalNumberPivotsInverted=True,
     noPhysicalNormInverted=True,wholeBHeadZeroExcluded=closedB)
closedA=bool(aRemaining and aRemaining.degree()==0)
say("corrected_whole_head_zero_final_scope",
    ABranchExcluded=closedA,BBranchExcluded=closedB,
    wholeCorrectedHeadZeroExcluded=closedA and closedB,
    totalExactDivisionsReturned=exact_divisions,
    totalUnivariateBezoutIdentitiesReturned=bezout_checks,
    assumptions=["Phi=0","Q*(1-Q)*Pf!=0","P02!=0","bc!=0"],
    noWithdrawnOldHeadResultUsed=True,
    originalPhiExcluded=False,ordinaryISPClaim=False)

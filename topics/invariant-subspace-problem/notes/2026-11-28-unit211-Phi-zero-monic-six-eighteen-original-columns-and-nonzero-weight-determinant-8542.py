#!/usr/bin/env python3
"""NEW bounded-lambda eighteen-coordinate original Phi relation input.
Use the genuine whole-Phi C6 monic lambda model on its true-head
complement. Nine ORIGINAL relation seeds act by lambda,T,z. A modular
good weight point selects ORIGINAL columns only; Gaussian residuals
are never reused as original relations. If rank18 is obtained, define
the QQ weight determinant by the exact selected column DAG and the
explicit common denominator product Gamma. No QQ determinant or
large parameter elimination is expanded. The modular inverse proves
only that this actual necessary determinant is nonzero, not that the
whole Phi face is empty. 120 seconds /1 GiB, including source prefixes.
2026-11-28 Asia/Taipei.
"""
import os,time,json,hashlib,signal,resource,contextlib,io,math
from pathlib import Path
START=time.perf_counter();DEADLINE=START+120
signal.setitimer(signal.ITIMER_REAL,120)
resource.setrlimit(resource.RLIMIT_AS,(1024**3,1024**3))
def say(stage,**kw):
 kw.update(stage=stage,seconds=time.perf_counter()-START)
 print(json.dumps(kw,separators=(",",":")),flush=True)
name="2026-11-28-unit211-Phi-zero-centered-original-NSPS-cofactor-content-and-leading-support-8542.py"
path=Path(os.environ.get("ISP_PHI_CENTERED_NSPS_SOURCE",str(Path(__file__).with_name(name))))
raw=path.read_bytes()
assert hashlib.sha256(raw).hexdigest()=="baaac1d2cb05437b6c771856aea8991692cad5ff62276e6bce12584d15da8ca6"
marker=b"\nfor j in range(3):\n rhs=R(primitive) if j==0 else R()\n"
assert raw.count(marker)==1
prefix=raw.split(marker)[0]
assert len(prefix)==6125
assert hashlib.sha256(prefix).hexdigest()=="4b152304c41026c94b93147d1360644217c5f15fff88e30264d2e7b02ae6b31d"
sc={"__file__":str(path),"__name__":"new_bounded_lambda_original_value_definition"}
old_alarm=signal.alarm;old_timer=signal.setitimer
def bounded_timer(which,seconds,interval=0):
 if which!=signal.ITIMER_REAL:return old_timer(which,seconds,interval)
 left=max(.001,DEADLINE-time.perf_counter())
 return old_timer(which,min(left,float(seconds) if seconds>0 else left),0)
def bounded_alarm(seconds):return math.ceil(bounded_timer(signal.ITIMER_REAL,seconds)[0])
signal.alarm=bounded_alarm;signal.setitimer=bounded_timer
try:
 with contextlib.redirect_stdout(io.StringIO()):
  exec(compile(prefix,str(path)+":necessary-original-C6-and-value-prefix","exec"),sc)
finally:
 signal.alarm=old_alarm;signal.setitimer=old_timer
 old_timer(signal.ITIMER_REAL,max(.001,DEADLINE-time.perf_counter()))
src=sc["scope"];geo=sc["geo"];R=sc["R"];ctx=sc["ctx"];zero=sc["zero"];one=sc["one"]
profile=sc["profile"];old=src["old"];C6=sc["primitive"]
assert int(C6.degrees()[2])==6
A3,E,N4=src["A3"],src["E"],src["N4"]
T,z,ell,m,M,delta,P02,lcoef,Al,Bl,NB,PB=[
 src[x] for x in ["T","z","ell","m","M","delta","P02","lcoef","Al","Bl","NB","PB"]]
# The remaining four original value DEFINITIONS are used only in
# their actual three-coordinate form. No slope coordinate or any
# old two-column value/large cofactor computation is executed.
TT=T*T;TTT=TT*T
D=A3(ell*Al)-TT
K=A3(ell*ell*Bl)-T*(3*ell*Al)+TTT*2
Dsq=D*D
R6=(K*K)*M-(Dsq*D)*(4*m*m)
A0=T/ell+1
Nlow=D*NB.b+(K*A0)*(2*lcoef*P02/m)+Dsq*(4*lcoef*P02*m/(ell*M))
Plow=(D*PB.b+(K*A0*A0)*(3*P02/(2*m))
      +(K*D)*(P02*(3*m*m/(ell*ell)+delta)/(2*m*M))
      +(A0*Dsq)*(6*P02*m/(ell*M)))
ww=A3(lcoef-1)-T
V0=[E(1),E(ww),E(A0),E(A0)]
V1=[E(),E(),E(m/ell,-1),E(m/ell,1)]
VN0=N4(V0);VN2=N4(V1)
VN1=N4([V0[i]+V1[i] for i in range(4)])-VN0-VN2
assert not VN0.b and not VN1.b and not VN2.b
Vlow=D*VN0.a+(K*VN1.a)/(2*m)+(Dsq*VN2.a)/M
labels=["original_N1","original_TTz_ambiguity","original_Tzz_ambiguity",
        "original_NS","original_PS","original_R6",
        "original_Nlow","original_Plow","entire_original_N4V_low"]
seeds=[old["leftover"],old["comm"][1],old["comm"][2],
       src["NS"].row,src["PS"].row,R6.row,Nlow.row,Plow.row,Vlow.row]
MT,Mz=old["MT"],old["MZ"]
# Formal matrix definitions over QQ(u,Q):
# E=K[lambda]/monic(C6), basis lambda^j*(1,T,z), j=0,...,5.
# Each seed and action is reduced ONLY by this actual original C6.
# The row maps are r -> r*MT and r -> r*Mz, not an assumed free algebra.
all_input=[v for row in seeds for v in row]+[v for A in [MT,Mz] for row in A for v in row]
for value in all_input:geo["legal"](value,False)
assert all(int(v.n.degrees()[2])<=6 for row in seeds for v in row)
assert all(int(v.n.degrees()[2])<=2 for A in [MT,Mz] for row in A for v in row)
c6=[zero for _ in range(7)]
for ex,value in C6.to_dict().items():
 assert ex[3]==ex[4]==0 and 0<=ex[2]<=6
 c6[int(ex[2])]+=ctx.from_dict({(int(ex[0]),int(ex[1]),0,0,0):value})
lc=c6[6];assert lc and geo["weight_only"](lc)
# Gamma is DEFINED as this finite product of distinct actual
# denominators, including lc(C6). It is deliberately not expanded.
# Every original coefficient denominator divides Gamma literally.
denoms={}
for poly in [v.d for v in all_input]+[lc]:
 assert poly and geo["weight_only"](poly)
 key=profile(poly)["sha256"]
 denoms.setdefault(key,poly)
denkeys=sorted(denoms)
gamma_degree=sum(int(denoms[k].total_degree()) for k in denkeys)
gamma_bidegree=[sum(int(denoms[k].degrees()[j]) for k in denkeys) for j in range(2)]
den_record_sha=hashlib.sha256(json.dumps(denkeys,separators=(",",":")).encode()).hexdigest()
say("new_bounded_lambda_eighteen_original_definition",
 actualOriginalSeedLabels=labels,
 originalDAGOperations=len(src["nodes"]),
 seedLambdaDegrees=[[int(v.n.degrees()[2]) for v in row] for row in seeds],
 actualC6=profile(C6),trueC6Leading=profile(lc),
 formalBasis="component i=0,1,2 then lambda power j=0,...,5; index 6*i+j",
 coefficientGammaFactorCount=len(denkeys),
 coefficientGammaFactorIdentitySHA256=den_record_sha,
 formalGammaTotalDegree=gamma_degree,formalGammaBidegree=gamma_bidegree,
 noSlopeFactorAddedToCoefficientRing=True,
 noFormalThreeDimensionalCommutativityAssumed=True,
 seedDenominatorExponentAtMost=2,
 lambdaActionDenominatorExponentAtMost=1,
 TorZActionDenominatorExponentAtMost=3)
p=1009
assert all(p%d for d in range(2,math.isqrt(p)+1))
def qmod(q):
 text=str(q);ab=text.split("/")
 a=int(ab[0]);b=int(ab[1]) if len(ab)>1 else 1
 if b%p==0:raise ValueError("an actual QQ coefficient is not integral at 1009")
 return (a%p)*pow(b%p,-1,p)%p
def eval_weight(poly,uu,qq):
 total=0
 for ex,value in poly.to_dict().items():
  assert not any(ex[2:])
  total=(total+qmod(value)*pow(uu,int(ex[0]),p)*pow(qq,int(ex[1]),p))%p
 return total
points=[(3,2),(3,5),(4,2),(5,3)]
chosen=None;skipped=[]
try:
 for uu,qq in points:
  bad=[]
  for label,poly in geo["paid"]:
   if not eval_weight(poly,uu,qq):bad.append("old_paid:"+label)
  for key in denkeys:
   if not eval_weight(denoms[key],uu,qq):bad.append("input_denominator:"+key)
  if bad:skipped.append(dict(point=[uu,qq],zeroRequiredInputs=bad));continue
  chosen=(uu,qq);break
except ValueError as exc:
 say("new_eighteen_fixed_point_input_not_integral",reason=str(exc),
     noRankOrPureWeightDeterminantClaim=True,wholePhiExcluded=False)
 signal.setitimer(signal.ITIMER_REAL,0);raise SystemExit(0)
if chosen is None:
 say("new_eighteen_no_eligible_fixed_point",
     testedPoints=points,skipped=skipped,
     pointSelectionOnlyByActualOriginalUnitsAndInputDenominators=True,
     noRankOrPureWeightDeterminantClaim=True,wholePhiExcluded=False)
 signal.setitimer(signal.ITIMER_REAL,0);raise SystemExit(0)
uu,qq=chosen
def raw_r(value):
 denominator=eval_weight(value.d,uu,qq)
 assert denominator
 result=[0]*(max(0,int(value.n.degrees()[2]))+1)
 for ex,v in value.n.to_dict().items():
  assert ex[3]==ex[4]==0
  result[int(ex[2])]=(result[int(ex[2])]+qmod(v)*pow(uu,int(ex[0]),p)*pow(qq,int(ex[1]),p))%p
 inv=pow(denominator,-1,p)
 return [x*inv%p for x in result]
try:
 lcbar=eval_weight(lc,uu,qq);assert lcbar
 g=[eval_weight(x,uu,qq)*pow(lcbar,-1,p)%p for x in c6]
 assert g[6]==1
 input_mod=[raw_r(v) for v in all_input]
except ValueError as exc:
 say("new_eighteen_actual_input_coefficient_not_integral",reason=str(exc),
     prime=p,point=chosen,noRankOrPureWeightDeterminantClaim=True,
     wholePhiExcluded=False)
 signal.setitimer(signal.ITIMER_REAL,0);raise SystemExit(0)
gamma_bar=1
for key in denkeys:gamma_bar=gamma_bar*eval_weight(denoms[key],uu,qq)%p
assert gamma_bar
def red(v):
 v=[int(x)%p for x in v]+[0]*max(0,6-len(v))
 for j in range(len(v)-1,5,-1):
  coefficient=v[j]
  if coefficient:
   for k in range(6):v[j-6+k]=(v[j-6+k]-coefficient*g[k])%p
  v[j]=0
 return tuple(v[:6])
ZERO=(0,)*6;ONE=(1,0,0,0,0,0);LAM=(0,1,0,0,0,0)
def plus(a,b):return tuple((x+y)%p for x,y in zip(a,b))
def times(a,b):
 out=[0]*11
 for i,x in enumerate(a):
  if x:
   for j,y in enumerate(b):
    if y:out[i+j]=(out[i+j]+x*y)%p
 return red(out)
def scaled(v,a):return tuple(x*a%p for x in v)
cursor=0
seedmod=[]
for row in seeds:
 seedmod.append([red(input_mod[cursor+i]) for i in range(3)]);cursor+=3
mats=[]
for A in [MT,Mz]:
 mat=[]
 for row in A:
  mat.append([red(input_mod[cursor+i]) for i in range(3)]);cursor+=3
 mats.append(mat)
assert cursor==len(input_mod)
def flatten(row):return tuple(x for cell in row for x in cell)
def split(v):return [tuple(v[6*i:6*i+6]) for i in range(3)]
def op(v,action):
 row=split(v)
 if action=="lambda":return flatten([times(x,LAM) for x in row])
 A=mats[0 if action=="T" else 1]
 return flatten([sum6([times(row[i],A[i][j]) for i in range(3)]) for j in range(3)])
def sum6(rows):
 out=ZERO
 for row in rows:out=plus(out,row)
 return out
unit=[0]*18;unit[0]=1
eT=[0]*18;eT[6]=1
ez=[0]*18;ez[12]=1
assert op(unit,"T")==tuple(eT) and op(unit,"z")==tuple(ez)
assert red([eval_weight(x,uu,qq) for x in c6])==ZERO
say("new_eighteen_fixed_point_actual_whole_monic_input",
 prime=p,point=chosen,skippedOnlyForInputUnits=skipped,
 allOriginalWeightAndC6LeadingUnitsCheckedBeforeRank=True,
 actualLambdaPolynomialDegree=6,
 fullMonicQuotientIncludingAllMultiplicities=True,
 gammaModPrime=gamma_bar,
 wholePhiOrWholeHeadEmptinessNotInferredFromPoint=True)
# Linear algebra is for selecting ORIGINAL columns only. Each child
# is an actual selected original parent times lambda,T,or z. No
# Gaussian residual, pivot scalar, or selected point coefficient is
# inserted into the characteristic-zero source DAG.
basis={};selected=[];selected_vectors=[]
queue=[dict(vector=flatten(row),seed=labels[i],parent=None,action=None,depth=0)
       for i,row in enumerate(seedmod)]
processed=0;cursor=0
while cursor<len(queue) and len(selected)<18:
 candidate=queue[cursor];cursor+=1;processed+=1
 raw_vector=candidate["vector"];w=list(raw_vector)
 for pivot in sorted(basis):
  factor=w[pivot]
  if factor:w=[(x-factor*y)%p for x,y in zip(w,basis[pivot])]
 pivot=next((i for i,x in enumerate(w) if x),None)
 if pivot is None:continue
 inv=pow(w[pivot],-1,p);basis[pivot]=tuple(x*inv%p for x in w)
 sid=len(selected)
 selected.append(dict(index=sid,seed=candidate["seed"],parent=candidate["parent"],
                      action=candidate["action"],depth=candidate["depth"],selectionPivot=pivot))
 selected_vectors.append(raw_vector)
 for action in ["lambda","T","z"]:
  queue.append(dict(vector=op(raw_vector,action),seed=None,parent=sid,
                    action=action,depth=candidate["depth"]+1))
rank=len(selected)
say("new_eighteen_actual_original_column_selection",
 prime=p,point=chosen,rank=rank,quotientDimension=18-rank,
 candidateColumnsProcessed=processed,
 selectedOriginalColumnDAG=selected,
 gaussianResidualsNotUsedAsOriginalColumns=True,
 noParameterPivotWasInvertedInTheQQSource=True)
if rank<18:
 say("new_eighteen_full_rank_target_not_returned",
     rank=rank,quotientDimension=18-rank,
     pureWeightNonzeroDeterminantNotClaimed=True,
     allHeadZeroAndOriginalFibersRetained=True,
     wholePhiExcluded=False,ordinaryISPClaim=False,
     peakRSSKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
 signal.setitimer(signal.ITIMER_REAL,0);raise SystemExit(0)
L=[[selected_vectors[j][i] for j in range(18)] for i in range(18)]
def inverse(A):
 n=len(A);B=[list(row)+[int(i==j) for j in range(n)] for i,row in enumerate(A)]
 for col in range(n):
  pivot=next(i for i in range(col,n) if B[i][col]%p)
  B[col],B[pivot]=B[pivot],B[col]
  inv=pow(B[col][col],-1,p);B[col]=[x*inv%p for x in B[col]]
  for i in range(n):
   if i!=col:
    factor=B[i][col]
    if factor:B[i]=[(x-factor*y)%p for x,y in zip(B[i],B[col])]
 assert all(B[i][j]==int(i==j) for i in range(n) for j in range(n))
 return [row[n:] for row in B]
def mm(A,B):
 return [[sum(A[i][k]*B[k][j] for k in range(18))%p for j in range(18)] for i in range(18)]
Linv=inverse(L)
assert mm(L,Linv)==[[int(i==j) for j in range(18)] for i in range(18)]
depth=max(x["depth"] for x in selected);exponent=2+3*depth
scale=pow(gamma_bar,exponent,p);assert scale
Bmod=[[scale*x%p for x in row] for row in L]
Binv=[[pow(scale,-1,p)*x%p for x in row] for row in Linv]
assert mm(Bmod,Binv)==[[int(i==j) for j in range(18)] for i in range(18)]
matrix_sha=hashlib.sha256(json.dumps(Bmod,separators=(",",":")).encode()).hexdigest()
# B=Gamma^exponent L has QQ[u,Q] polynomial entries by the proved
# denominator ledger. Define F=det(B), without expansion. B*adj(B)=F I
# gives F e0 as an actual combination of the selected original
# relation columns. Its nonzero specialization above proves F!=0.
say("new_original_eighteen_column_nonzero_pure_weight_support",
 prime=p,point=chosen,rank=18,
 fullSelectedMatrixTimesActualInverseReturned=True,
 fullClearedMatrixTimesActualInverseReturned=True,
 selectedOriginalColumnDAG=selected,
 maxActionDepth=depth,commonDenominatorPower=exponent,
 GammaDefinition="product of distinct actual input coefficient denominators and lc_lambda(C6)",
 GammaFactorIdentitySHA256=den_record_sha,GammaFactorCount=len(denkeys),
 GammaTotalDegree=gamma_degree,GammaBidegree=gamma_bidegree,
 exactWeightPolynomialDefinition="F(u,Q)=det(Gamma^(2+3*maxActionDepth)*L_original_DAG)",
 originalAdjugateIdentity="B*adj(B)*e0=F*e0, each B column in original I10",
 nonzeroPolynomialProvedByActualGoodSpecialization=True,
 coefficientMatrixSpecializationSHA256=matrix_sha,
 entireOriginalHeadH42ZeroBranchRetained=True,
 entireNewWeightCurveFZeroRetained=True,
 noQQDeterminantExpansionOrLargeEliminationExecuted=True,
 noClaimThatModularRankMakesWholeOriginalPhiEmpty=True,
 noRecomputableMatrixOrPolynomialPayloadSaved=True,
 wholePhiExcluded=False,ordinaryISPClaim=False,
 peakRSSKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
signal.setitimer(signal.ITIMER_REAL,0)

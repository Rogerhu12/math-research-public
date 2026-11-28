#!/usr/bin/env python3
"""NEW whole current Phi chart: full original highest-degree NV/F6 rows.
The ENTIRE first quadratic head is now paid by the H1 theorem.
Read only the necessary three-rule prefix of 100ce, before its old
D-cofactor. Take the genuine weighted highest-degree functor, including
the COMPLETE original F6 and NV expression, and return an actual
constant-row combination over QQ(u,Q). Clear final weight denominators.
Lift the same combination to the original lambda rows: C*lambda^N
equals a strictly lower weighted-degree row in (1,T,z), modulo the
actual original ideal. This gives a monic lambda polynomial on C!=0,
while retaining the ENTIRE C=0 weight locus. No old weak Popov,
P6/P9 cofactor, F6 recurrence payload, or norm gate is replayed.
120s/1GiB; small definitions, degrees and hashes only.
2026-11-28 Asia/Taipei.
"""
import os,time,json,hashlib,signal,resource,contextlib,io,math
from pathlib import Path
START=time.perf_counter();DEADLINE=START+120
signal.alarm(120);resource.setrlimit(resource.RLIMIT_AS,(1024**3,1024**3))
def say(stage,**kw):
 kw.update(stage=stage,seconds=time.perf_counter()-START)
 print(json.dumps(kw,separators=(",",":")),flush=True)
def read_prefix():
 name="2026-11-27-unit211-Phi-zero-first-quadratic-head-three-original-rows-D-input-8542.py"
 path=Path(os.environ.get("ISP_PHI_FIRST_HEAD_RULE_SOURCE",str(Path(__file__).with_name(name))))
 raw=path.read_bytes()
 assert hashlib.sha256(raw).hexdigest()=="100ce4dfb7380da1591cd453aae392e2dafcaaceb3a601c4500d07852841ecaf"
 mark=b"\ndet0=determinant(rows)\n";assert raw.count(mark)==1
 prefix=raw.split(mark)[0]
 assert len(prefix)==7097
 assert hashlib.sha256(prefix).hexdigest()=="9467955925e4f6bd05aaf74c5d8fb7e747a03c0a5119fb17ee2b87e7703a701b"
 ns={"__file__":str(path),"__name__":"new_original_highest_degree_source_only"}
 original_alarm=signal.alarm
 def bounded_alarm(seconds):
  remaining=max(.001,DEADLINE-time.perf_counter())
  requested=float(seconds) if seconds>0 else remaining
  previous=signal.setitimer(signal.ITIMER_REAL,min(remaining,requested))
  return math.ceil(previous[0])
 signal.alarm=bounded_alarm
 try:
  with contextlib.redirect_stdout(io.StringIO()):
   exec(compile(prefix,str(path)+":necessary-rules-only","exec"),ns)
 finally:
  signal.alarm=original_alarm
  signal.setitimer(signal.ITIMER_REAL,max(.001,DEADLINE-time.perf_counter()))
 return ns
old=read_prefix()
R=old["R"];ctx=old["ctx"];zero=old["zeroP"];one=old["oneP"]
up,Qp,Lp,Tp,zp=ctx.gens()
u,Q,ell,delta,m,M,bc,T0,J,P02,Pf=[old[s] for s in
 ["u","Q","ell","delta","m","M","bc","T0","J","P02","Pf"]]
MT=old["MT"];MZ=old["MZ"];rules=old["rules"]
head=old["head_det"]
weight=[0,1,1]
def weight_only(p):return all(not any(e[2:]) for e in p.to_dict())
def profile(p):
 h=hashlib.sha256();nbytes=0;dd=p.to_dict()
 for e,c in sorted(dd.items()):
  raw=(json.dumps([list(map(int,e)),str(c)],separators=(",",":"))+"\n").encode()
  h.update(raw);nbytes+=len(raw)
 return dict(degrees=list(map(int,p.degrees())),terms=len(dd),
             bytes=nbytes,sha256=h.hexdigest())
def rprofile(x):return dict(numerator=profile(x.n),denominator=profile(x.d))
def exact(a,b):
 q=a/b;assert q*b==a
 return q
paid=[("u",u.n),("u-1",(u-1).n),("Q",Q.n),("1-Q",delta.n),
 ("ell",ell.n),("u-ell",m.n),("M",M.n),("P02",P02.n),
 ("T0",T0.n),("J-Q",(J-Q).n),("u+Q-1",(u+Q-1).n),
 ("whole_Phi_first_quadratic_head_now_paid",head.n)]
for _,p in paid:assert weight_only(p)
def strip_paid(p):
 assert p and weight_only(p)
 remaining=p;factor=one;history=[]
 for label,atom in paid:
  multiplicity=0
  while True:
   gg=remaining.gcd(atom)
   if gg.total_degree()==0:break
   remaining=exact(remaining,gg);factor*=gg;multiplicity+=1
  if multiplicity:history.append(dict(unit=label,passes=multiplicity))
 c=remaining.coefficient(0)
 remaining=exact(remaining,ctx.constant(c));factor*=c
 assert factor*remaining==p
 return remaining,factor,history
def pay(p):
 q,_,_=strip_paid(p)
 assert q.total_degree()==0,"an original coefficient has an unpaid weight denominator"
def check_weight(x):
 x=R(x);assert weight_only(x.n) and weight_only(x.d);pay(x.d);return x
def lambda_coefficient(x,j):
 x=R(x);assert weight_only(x.d)
 if j<0:
  assert not x;return R()
 out={}
 for e,c in x.n.to_dict().items():
  assert e[3]==0 and e[4]==0
  assert int(e[2])<=j
  if int(e[2])==j:out[(int(e[0]),int(e[1]),0,0,0)]=c
 return check_weight(R(ctx.from_dict(out),x.d))
def row_top(row,degree):
 return [lambda_coefficient(c,degree-weight[j]) for j,c in enumerate(row)]
# These are the actual associated-graded multiplication matrices.
# No substitution at lambda=1 is applied to the full lower-degree rows.
mt=[[lambda_coefficient(MT[i][j],1+weight[i]-weight[j])
     for j in range(3)] for i in range(3)]
mz=[[lambda_coefficient(MZ[i][j],1+weight[i]-weight[j])
     for j in range(3)] for i in range(3)]
rm=old["rm"];mm=old["mm"]
low1=row_top(old["leftover"],2)
amb1=row_top(old["comm"][1],3)
amb2=row_top(old["comm"][2],3)
aa,bb=mm(mt,mz),mm(mz,mt)
assert all(aa[i][j]-bb[i][j]==row_top(old["comm"][i],2+weight[i])[j]
           for i in range(3) for j in range(3))
say("new_actual_original_associated_graded_three_rule_source",
 wholeFirstHeadAlreadyPaid=True,basisWeights=weight,
 sixActualMatrixEntryDegreeBoundsReturned=True,
 threeRemainingOriginalRowsDegrees=[2,3,3],
 noFullLambdaRowModuleOrOldDTargetExecuted=True)

# The graded highest-component functor: degree is a PROVED upper bound.
# Addition at unequal bounds keeps only the higher component; products
# add bounds. Vanishing components never silently lower the full bound.
# t and s below denote T/lambda and z/lambda ONLY in this functor.
top_operation_count=0
class Top:
 __slots__=("degree","value")
 def __init__(self,value=0,degree=0):
  if isinstance(value,Top):self.degree=value.degree;self.value=value.value;return
  value=R(value);assert weight_only(value.d)
  assert all(e[2]==0 and int(e[3])+int(e[4])<=degree for e in value.n.to_dict())
  self.degree=degree;self.value=value
 def __neg__(self):return Top(-self.value,self.degree)
 def __add__(self,o):
  global top_operation_count
  o=Top(o);d=max(self.degree,o.degree)
  value=(self.value if self.degree==d else R())+(o.value if o.degree==d else R())
  top_operation_count+=1;return Top(value,d)
 __radd__=__add__
 def __sub__(self,o):return self+-Top(o)
 def __rsub__(self,o):return Top(o)+-self
 def __mul__(self,o):
  global top_operation_count
  o=Top(o);top_operation_count+=1
  return Top(self.value*o.value,self.degree+o.degree)
 __rmul__=__mul__
 def __truediv__(self,o):
  # Only an original weight coefficient is divided, never a spectral
  # leading coefficient or an element of an unproved quotient field.
  o=R(o);assert weight_only(o.n) and weight_only(o.d)
  pay(o.n);pay(o.d)
  return Top(self.value/o,self.degree)
 def __pow__(self,n):
  assert n>=0
  out=Top(1);base=self
  while n:
   if n&1:out=out*base
   n//=2
   if n:base=base*base
  return out
l=Top(1,1);t=Top(R(Tp),1);s=Top(R(zp),1)
A2=2*l*l-2*l+1;B3=4*l**3-6*l*l+3*l-1
DD=A2*ell-t*t
KK=B3*(ell*ell)-t*A2*(3*ell)+2*t**3
sn=B3*ell-A2*t
zn=t*B3-A2*A2
Znum=sn*u-2*t*DD
Snum=sn+(3-2*l)*DD
GG=l*P02+(u-1)*T0
ww=l-1-t
ff=(GG*T0-(t+ell)*(Q*P02))/Pf
NF4=((3-4*l)*DD*DD*Q-zn*DD*J)*(4*m)+2*Snum*(KK*(-2*u*Q)+Znum*J)
NC4=(GG*zn*DD*(4*m)-2*GG*Snum*Znum-Snum*KK*(Q*T0)
     +ww*(3-2*l)*DD*DD*(4*m*Q*u)+ww*sn*DD*(2*m*Q*u)
     -ww*KK*DD*(2*Q*(u-ell*Q)))
F6=KK*KK*M-DD**3*(4*m*m)
NV=NF4*ff+NC4+Snum*Znum*s*(2*bc)
assert F6.degree==6 and NV.degree==7
tt=R(Tp);ss=R(zp)
D2=2*ell-tt*tt;K3=4*ell*ell-6*ell*tt+2*tt**3
s3=2*tt*(tt-1);z3=u*(4*ell-2*tt)-2*tt*D2
f1=P02*(T0-Q*tt)/Pf
nf6=-4*m*J*(4*tt-4)*D2+2*s3*(-2*u*Q*K3+J*z3)
nc7=4*m*P02*(4*tt-4)*D2-2*P02*s3*z3
assert DD.value==D2 and KK.value==K3 and Snum.value==s3 and Znum.value==z3
assert F6.value==M*K3*K3-4*m*m*D2**3
assert NV.value==nf6*f1+nc7+2*bc*s3*z3*ss
# Reduce the ACTUAL highest polynomial by the same genuine mean rules.
# The fixed order is first T powers, then z powers; no free commutation.
cache={(0,0):[R(1),R(),R()]}
def monomial_row(a,b):
 if (a,b) not in cache:
  if b:cache[a,b]=rm(monomial_row(a,b-1),mz)
  else:cache[a,b]=rm(monomial_row(a-1,0),mt)
 return cache[a,b]
def reduce_top(p):
 p=R(p);assert weight_only(p.d);pay(p.d)
 coeff={}
 for e,c in p.n.to_dict().items():
  assert e[2]==0
  key=(int(e[3]),int(e[4]))
  term=ctx.from_dict({(int(e[0]),int(e[1]),0,0,0):c})
  coeff[key]=coeff.get(key,zero)+term
 out=[R(),R(),R()]
 for (a,b),co in coeff.items():
  q=check_weight(R(co,p.d));vec=monomial_row(a,b)
  out=[x+q*y for x,y in zip(out,vec)]
 for x in out:check_weight(x)
 return out
frow=reduce_top(F6.value)
nvrow=reduce_top(NV.value)
say("new_complete_original_F6_NV_highest_rows",
 originalFullDegrees=[6,7],
 exactFullOriginalExpressionsDefinedInSource=True,
 highestNVExplicitProductReturned=True,
 gradedFunctorOperationCount=top_operation_count,
 highestF6Row=[rprofile(x) for x in frow],
 highestNVRow=[rprofile(x) for x in nvrow],
 reductionOrder="e0*MT^a*MZ^b",
 actualOriginalRowsNotGenericValueSurrogates=True,
 noOldFullF6RowPayloadOrRecurrenceExecuted=True)

# A fixed ordered input: the new full NV and F6 highest rows are used
# before N1 and the two genuine ambiguities. Gaussian is only 5-by-3
# over the weight field; every row has its complete five-source witness.
raw=[nvrow,frow,low1,amb1,amb2]
labels=["full_NV_degree7","full_F6_degree6","original_N1_degree2",
        "original_T2z_ambiguity_degree3","original_Tz2_ambiguity_degree3"]
grades=[7,6,2,3,3]
basis={};selected=[]
for source_index,original_row in enumerate(raw):
 rr=original_row[:];comb=[R(int(i==source_index)) for i in range(5)]
 for pivot in sorted(basis):
  br,bc0=basis[pivot];factor=rr[pivot]
  if factor:
   rr=[x-factor*y for x,y in zip(rr,br)]
   comb=[x-factor*y for x,y in zip(comb,bc0)]
 pivot=next((i for i,x in enumerate(rr) if x),None)
 if pivot is None:
  assert all(sum((comb[k]*raw[k][j] for k in range(5)),R())==0 for j in range(3))
  continue
 factor=rr[pivot];rr=[x/factor for x in rr];comb=[x/factor for x in comb]
 assert rr[pivot]==1
 for oldpivot in list(basis):
  br,bc0=basis[oldpivot];factor=br[pivot]
  if factor:
   basis[oldpivot]=([x-factor*y for x,y in zip(br,rr)],
                    [x-factor*y for x,y in zip(bc0,comb)])
 basis[pivot]=(rr,comb);selected.append(source_index)
 assert all(sum((comb[k]*raw[k][j] for k in range(5)),R())==rr[j] for j in range(3))
 say("new_highest_original_weight_row_basis_step",
     original=labels[source_index],rank=len(basis),pivot=pivot,
     fullThreeCoefficientSourceCombinationReturned=True)
 if len(basis)==3:break
if 0 not in basis or basis[0][0]!=[R(1),R(),R()]:
 say("new_highest_original_weight_unit_unresolved",
     actualRank=len(basis),allFiveOriginalRowsRetained=True,
     noMonicLambdaOrWholePhiExclusionClaim=True)
 signal.setitimer(signal.ITIMER_REAL,0);raise SystemExit(0)
row,alpha=basis[0]
assert row==[R(1),R(),R()]
assert all(sum((alpha[i]*raw[i][j] for i in range(5)),R())==int(j==0) for j in range(3))
C=one
for co in alpha:
 assert weight_only(co.n) and weight_only(co.d)
 gg=C.gcd(co.d);C=exact(C,gg)*co.d
betas=[]
for co in alpha:
 quotient=exact(C,co.d);betas.append(co.n*quotient)
assert all(sum((R(betas[i])*raw[i][j] for i in range(5)),R())==R(C)*int(j==0)
           for j in range(3))
core,paid_scale,removed=strip_paid(C)
active=[i for i,x in enumerate(alpha) if x]
N=max(grades[i] for i in active)
say("new_original_highest_unit_and_exact_filtered_lift_finished",
 sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 originalActiveRows=[labels[i] for i in active],
 selectedSourceIndices=selected,
 allFiveSourceThreeCoefficientProductsReturned=True,
 actualFinalWeightDenominator=profile(C),
 finalWeightMultipliers=[profile(p) for p in betas],
 removedOnlyAlreadyPaidWeights=removed,
 retainedEntireWeightSupport=profile(core),
 exactWeightIdentity="C*e0=sum_i beta_i*highest_original_row_i",
 liftDegree=N,
 exactFullOriginalLiftDefinition="sum_i beta_i*lambda^(N-grade_i)*full_original_row_i",
 actualFullLiftConclusion="C*lambda^N=a0+a1*T+a2*z modulo the original ideal",
 strictLowerLambdaDegreeBounds=[N-1,N-2,N-2],
 fullThreeRowLiftDefinition="multiply this same scalar relation by 1,T,z and use actual mean rules",
 determinantDefinition="det(C*lambda^N*I-(a0*I+a1*MT+a2*MZ))",
 exactDeterminantLeadingCoefficient="C^3",
 exactDeterminantLambdaDegree=3*N,
 monicLambdaOnlyOnFinalWeightSupportComplement=True,
 entireFinalWeightSupportZeroLocusRetained=True,
 originalModuleIsGeneratedByAtMost=3*N,
 freeOriginalModuleNotAssumed=True,
 noLambdaInverseUsed=True,
 globalWeightDenominatorIsAlreadyPaid=(core.total_degree()==0),
 wholePhiExcluded=False,ordinaryISPClaim=False,
 noOldP6P9CofactorNormWeakPopovOrGramGateReplayed=True,
 coefficientPayloadOrEncodingOrSplitSaved=False,
 peakRSSKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
signal.setitimer(signal.ITIMER_REAL,0);signal.alarm(0)

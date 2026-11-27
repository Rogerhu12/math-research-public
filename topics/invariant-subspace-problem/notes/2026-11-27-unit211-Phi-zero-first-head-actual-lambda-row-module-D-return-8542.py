#!/usr/bin/env python3
"""NEW actual original lambda row module on the first Phi quadratic head.
Read the saved actual F6 row through the exact <100KB fragment manifest.
Work in QQ(u,Q)[lambda]^3 with original N1, both actual multiplication
ambiguities, and F6. Weak Popov reductions only invert weight-field
coefficients. Test original lambda^a D^k targets and, if necessary,
add one fixed level of actual MT/MZ images of the original four rows.
Every final witness is fully multiplied back against the original
raw rows, and ALL final weight denominators are cleared. Their zero
sets are retained; generic row rank or gcd one is not global emptiness.
120 seconds /1 GiB. No former D-cofactor, F6 recurrence or resultant
is rerun. Dependencies: pinned manifest plus its six F6 row fragments.
"""
import json,time,hashlib,base64,zlib,signal,resource
from pathlib import Path
from flint import fmpq,fmpq_mpoly_ctx
signal.alarm(120)
resource.setrlimit(resource.RLIMIT_AS,(1024**3,1024**3))
began=time.perf_counter()
def say(stage,**kw):
 kw.update(stage=stage,seconds=time.perf_counter()-began)
 print(json.dumps(kw),flush=True)
ctx=fmpq_mpoly_ctx.get(('u','Q','lam','T','z'),'lex')
up,Qp,Lp,Tp,zp=ctx.gens();zeroP=ctx.constant(0);oneP=ctx.constant(1)
def poly(x):return x if hasattr(x,'to_dict') else ctx.constant(x)
class R:
 def __init__(self,n=0,d=None,reduce=True):
  if isinstance(n,R):self.n=n.n;self.d=n.d;return
  n=poly(n);d=oneP if d is None else poly(d);assert d
  if not n:self.n=zeroP;self.d=oneP;return
  if reduce:
   g=n.gcd(d);n=n/g;d=d/g
  lc=d.coefficient(0);self.n=n/lc;self.d=d/lc
 def __bool__(self):return bool(self.n)
 def __add__(self,o):
  o=R(o)
  if not self:return o
  if not o:return self
  g=self.d.gcd(o.d);a=self.d/g;b=o.d/g
  return R(self.n*b+o.n*a,a*o.d)
 __radd__=__add__
 def __neg__(self):return R(-self.n,self.d,False)
 def __sub__(self,o):return self+-R(o)
 def __rsub__(self,o):return R(o)+-self
 def __mul__(self,o):
  o=R(o)
  if not self or not o:return R()
  g=self.n.gcd(o.d);h=o.n.gcd(self.d)
  return R((self.n/g)*(o.n/h),(self.d/h)*(o.d/g),False)
 __rmul__=__mul__
 def __truediv__(self,o):o=R(o);assert o;return self*R(o.d,o.n,False)
 def __rtruediv__(self,o):return R(o)/self
 def __pow__(self,n):
  return R(self.d**(-n),self.n**(-n),False) if n<0 else R(self.n**n,self.d**n,False)
 def __eq__(self,o):
  o=R(o)
  if self.n==o.n and self.d==o.d:return True
  return self.n*o.d==o.n*self.d
u,Q,lam,Tr=map(R,(up,Qp,Lp,Tp))
z=R(zp)
ell=1-2*(u-1)*(u-2)/Q
delta=1-Q;m=u-ell;V2=2*u-ell*Q;T0=V2-2*u*u
J=2*u*(1-u)+ell*Q
P02=(2-3*u)*V2-Q*u+2*u**3;Pf=T0*(J-Q)
M=ell*V2-u*u;bc=M/(4*delta)
A2=2*lam*lam-2*lam+1
G=lam*P02+(u-1)*T0
Pc=Q*P02*(ell+Tr)-G*T0
ff=-Pc/Pf
assert T0+4*u-4+Q==0
assert T0==-Q-4*(u-1) and J-Q==-4*(u-1)**2
assert P02==2*(u-1)*ell*Q
assert Pf*ff+Pc==0
aa=1-ell
vn=J*ff-G+bc*z
wstar=T0+4*u*ff
nn=Q*wstar-2*vn
ww=lam-1-Tr
ii=((vn+aa*u*Q)**2-2*u*Q*vn+2*aa*u*u*Q*Q
    -4*aa*u*Q*Q*ff+bc*z*z+z*(4*bc*u*Q-ell*vn))
Rbar=ii+(m/(2*delta))*z*nn
W4=(8*bc*delta*Q*Q*ell*T0-4*ell*delta*vn*vn-ell*nn*nn
    +4*m*vn*nn+32*bc*delta*Q*ff*vn+16*bc*bc*delta*z*z
    +32*bc*bc*delta*Q*(u-1)*z-8*bc*ell*delta*z*vn+4*bc*m*z*nn)
s0=2*ell*vn-(m/delta)*nn
d0=-2*m*vn+ell*nn
Obar=(32*bc*bc*aa*Q*Q*delta*(u-1)+4*bc*Q*delta*s0
      +32*bc*bc*Q*delta*vn-64*bc*bc*Q*Q*delta*ff
      +4*bc*Q*(1-u+2*ff)*d0-s0*d0-8*bc*bc*m*z*z
      -16*bc*bc*Q*z*(m*(u-1)+ell*delta)+8*bc*bc*z*nn)
al=ell*(1-u)-m
ber=ell*delta-m*(1-u)
av=(2*u-1)*ell+3*m
bur=(2*u-1)*m+3*ell*delta
Nstar=(al*(4*delta*vn*vn+nn*nn)+4*ber*vn*nn
       +8*bc*delta*Q*vn*wstar-24*bc*delta*Q*Q*ff*wstar
       +16*aa*bc*delta*Q*Q*(u-1)*wstar+64*bc*delta*Q*Q*u*ff*ff
       -32*bc*delta*Q*u*ff*vn+16*bc*delta*Q*Q*(1+aa)*T0*ff
       +16*bc*delta*Q*(aa*Q-T0)*vn+4*bc*delta*av*z*vn
       -2*bc*bur*z*nn+16*bc*bc*delta*Q*z*(2*ff+T0-aa*Q)
       -8*u*bc*bc*delta*z*z)
N1=Nstar-16*bc*delta*Q*Q*lam*P02*ww

def param(p):return all(e[3]==0 and e[4]==0 for e in p.to_dict())
def info(p):
 return dict(degrees=list(map(int,p.degrees()))[:3],
             terms=len(p.to_dict()),
             sha256=hashlib.sha256(str(sorted(p.to_dict().items())).encode()).hexdigest())
def extract_quad(p):
 p=R(p);assert param(p.d)
 cc=[zeroP for _ in range(6)]
 slots={(0,0):0,(1,0):1,(0,1):2,(2,0):3,(1,1):4,(0,2):5}
 for e,c in p.n.to_dict().items():
  assert (int(e[3]),int(e[4])) in slots
  j=slots[(int(e[3]),int(e[4]))]
  ee=tuple(e[:3])+(0,0);cc[j]=cc[j]+ctx.from_dict({ee:c})
 ans=[R(p0,p.d) for p0 in cc]
 rebuild=ans[0]+ans[1]*Tr+ans[2]*z+ans[3]*Tr*Tr+ans[4]*Tr*z+ans[5]*z*z
 assert rebuild==p
 return ans
quads=[extract_quad(p) for p in [Rbar,W4,Obar,N1]]
head=[r[3:] for r in quads[:3]]
lower=[r[:3] for r in quads[:3]]
def determinant(a):
 return a[0][0]*(a[1][1]*a[2][2]-a[1][2]*a[2][1])-a[0][1]*(a[1][0]*a[2][2]-a[1][2]*a[2][0])+a[0][2]*(a[1][0]*a[2][1]-a[1][1]*a[2][0])
def adjugate(a):
 out=[[R() for _ in range(3)] for _ in range(3)]
 for i in range(3):
  for j in range(3):
   rr=[k for k in range(3) if k!=j];cc=[k for k in range(3) if k!=i]
   v=a[rr[0]][cc[0]]*a[rr[1]][cc[1]]-a[rr[0]][cc[1]]*a[rr[1]][cc[0]]
   out[i][j]=v if (i+j)%2==0 else -v
 return out
def mm(a,b):
 return [[sum((a[i][k]*b[k][j] for k in range(3)),R()) for j in range(3)] for i in range(3)]
def rm(r,b):
 return [sum((r[k]*b[k][j] for k in range(3)),R()) for j in range(3)]
head_det=determinant(head);assert head_det
head_adj=adjugate(head)
assert all(v==(head_det if i==j else 0) for i,row in enumerate(mm(head,head_adj)) for j,v in enumerate(row))
rules=[[-sum((head_adj[i][k]*lower[k][j] for k in range(3)),R())/head_det
        for j in range(3)] for i in range(3)]
assert all(sum((head[i][k]*rules[k][j] for k in range(3)),R())+lower[i][j]==0
           for i in range(3) for j in range(3))
say("new_exact_three_generator_original_mean_chart",
    quadraticHeadNumerator=info(head_det.n),quadraticHeadDenominator=info(head_det.d),
    variables=["T","z"],generators=["1","T","z"],
    allNineOriginalRuleCoefficientIdentitiesReturned=True,
    onlyOnFirstHeadNonzeroChart=True,firstHeadZeroCurveRetained=True)
MT=[[R(0),R(1),R(0)],rules[0],rules[1]]
MZ=[[R(0),R(0),R(1)],rules[1],rules[2]]
commA=mm(MT,MZ);commB=mm(MZ,MT)
comm=[[a-b for a,b in zip(ar,br)] for ar,br in zip(commA,commB)]
assert all(c==0 for c in comm[0])
# This is the fixed reduction of the fourth original polynomial.
leftover=[quads[3][j]+sum((quads[3][3+k]*rules[k][j] for k in range(3)),R())
          for j in range(3)]
rows=[leftover,comm[1],comm[2]]
# The commutator rows are genuine original-ideal rows: apply the
# displayed three original quadratic identities in the two orders
# to T^2*z and T*z^2.  No commutation in the free rank-three module
# is assumed; these very differences remain imposed as extra rows.
Drow=[R(ell*A2)-rules[0][0],-rules[0][1],-rules[0][2]]
assert all(param(rr.n) and param(rr.d) for row in rows+[Drow] for rr in row)
say("new_fixed_original_N1_and_true_multiplication_ambiguity_DAG",
    rows=["original_N1","T_square_z_two_orders","T_z_square_two_orders"],
    actualExtraRowNumerators=[[info(rr.n) for rr in row] for row in rows],
    target="D=ell*A2-T^2",
    originalCoefficientDAGNotOnlyPointwiseNecessary=True,
    noUnprovedAssociativityUsed=True)

# Read only the first record's six pieces; the same manifest also
# indexes P9 pieces, which this NEW row-module input does not use.
manifest_name="2026-11-27-unit211-Phi-zero-first-head-F6-D-exact-input-manifest-8542.json"
manifest_bytes=Path(__file__).with_name(manifest_name).read_bytes()
assert hashlib.sha256(manifest_bytes).hexdigest()=="98f0a4d5af1fe650cacb56db3e11a90bd7d2426b2af670cdd41b0a3ca1b2f5e7"
record=json.loads(manifest_bytes)["records"]["originalF6Row"]
strings=[]
for i,part in enumerate(record["parts"]):
 raw=Path(__file__).with_name(part["name"]).read_bytes()
 assert len(raw)==part["bytes"] and len(raw)<100000
 assert hashlib.sha256(raw).hexdigest()==part["sha256"]
 piece=json.loads(raw)
 assert piece["record"]=="originalF6Row" and piece["index"]==i+1
 assert len(piece["dataChunk"])==part["dataCharacters"]
 strings.append(piece["dataChunk"])
combined="".join(strings)
assert len(combined)==record["concatenatedBase64Characters"]
assert hashlib.sha256(combined.encode()).hexdigest()==record["concatenatedBase64Sha256"]
raw=zlib.decompress(base64.b64decode(combined))
assert hashlib.sha256(raw).hexdigest()=="503bd798a55c546048f1216bece8da431d36b14116873c08e35c35546f99a103"
obj=json.loads(raw);assert obj["variables"]==["u","Q","lambda"]
F6row=[]
for pair in obj["coefficients"]:
 pn=ctx.from_dict({tuple(e)+(0,0):fmpq(c) for e,c in pair["numerator"]})
 pd=ctx.from_dict({tuple(e)+(0,0):fmpq(c) for e,c in pair["denominator"]})
 assert all(e[2]==e[3]==e[4]==0 for e in pd.to_dict())
 F6row.append(R(pn,pd))
assert len(F6row)==3
say("saved_actual_original_F6_row_loaded_without_recurrence_replay",
    fragmentCount=len(strings),allFragmentAndWholePayloadHashesReturned=True,
    originalF6Numerators=[info(v.n) for v in F6row],
    originalF6Denominators=[info(v.d) for v in F6row])
def weight_only(p):return all(e[2]==e[3]==e[4]==0 for e in p.to_dict())
def qt(a):
 a=[R(x) for x in a]
 while a and not a[-1]:a.pop()
 assert all(weight_only(x.n) and weight_only(x.d) for x in a)
 return a
def qa(a,b):
 c=[R(0) for _ in range(max(len(a),len(b)))]
 for i,x in enumerate(a):c[i]=c[i]+x
 for i,x in enumerate(b):c[i]=c[i]+x
 return qt(c)
def qneg(a):return qt([-x for x in a])
def qs(a,b):return qa(a,qneg(b))
def qscale_shift(a,c,shift):
 assert shift>=0
 if not c or not a:return []
 return [R(0) for _ in range(shift)]+qt([x*c for x in a])
def extract_lambda(rr):
 rr=R(rr);assert weight_only(rr.d)
 if not rr:return []
 n=int(rr.n.degrees()[2]);a=[zeroP]*(n+1)
 for e,c in rr.n.to_dict().items():
  assert e[3]==e[4]==0
  j=int(e[2]);ex=(int(e[0]),int(e[1]),0,0,0)
  a[j]=a[j]+ctx.from_dict({ex:c})
 return qt([R(p,rr.d) for p in a])
def rebuild_lambda(a):
 ans=R(0)
 for i,c in enumerate(a):ans=ans+c*lam**i
 return ans
def row_poly(row):
 ans=[extract_lambda(x) for x in row]
 assert all(rebuild_lambda(a)==b for a,b in zip(ans,row))
 return ans
def leading(row):
 d=max((len(a)-1 for a in row),default=-1)
 if d<0:return None
 return d,max(j for j,a in enumerate(row) if len(a)-1==d)
def row_sub_multiple(row,other,c,shift):
 return [qs(a,qscale_shift(b,c,shift)) for a,b in zip(row,other)]
def tag_sub_multiple(tags,other,c,shift):
 return [qs(a,qscale_shift(b,c,shift)) for a,b in zip(tags,other)]
def tag_add_multiple(tags,other,c,shift):
 return [qa(a,qscale_shift(b,c,shift)) for a,b in zip(tags,other)]
raw_seeds=[];seed_labels=[];weak={};row_operations=0
def basis_degrees():
 return {str(j):leading(item["row"])[0] for j,item in sorted(weak.items())}
def add_original_seed(raw,label):
 global row_operations
 raw=list(raw);raw_seeds.append(raw);seed_labels.append(label)
 for item in weak.values():item["tags"].append([])
 count=len(raw_seeds)
 row=row_poly(raw);tags=[[] for _ in range(count)];tags[-1]=[R(1)]
 say("new_original_lambda_module_seed",seed=count-1,label=label,
     leading=leading(row),currentWeakDegrees=basis_degrees())
 while True:
  lead=leading(row)
  if lead is None:
   say("new_original_lambda_seed_exactly_dependent",seed=count-1,
       currentWeakDegrees=basis_degrees(),rowOperations=row_operations)
   return
  degree,column=lead
  if column not in weak:
   weak[column]={"row":row,"tags":tags}
   say("new_original_lambda_weak_popov_basis_changed",
       currentWeakDegrees=basis_degrees(),rowOperations=row_operations)
   return
  previous=weak[column];old_degree=leading(previous["row"])[0]
  if degree<old_degree:
   weak[column]={"row":row,"tags":tags}
   row,tags=previous["row"],previous["tags"]
   say("new_original_lambda_weak_popov_shorter_pivot",
       column=column,newDegree=degree,oldDegree=old_degree,
       currentWeakDegrees=basis_degrees())
   continue
  c=row[column][-1]/previous["row"][column][-1]
  assert weight_only(c.n) and weight_only(c.d)
  shift=degree-old_degree
  row=row_sub_multiple(row,previous["row"],c,shift)
  tags=tag_sub_multiple(tags,previous["tags"],c,shift)
  now=leading(row);assert now is None or now<lead
  row_operations+=1
  say("new_actual_lambda_polynomial_row_operation",
      operation=row_operations,lambdaShift=shift,
      weightMultiplierNumerator=info(c.n),weightMultiplierDenominator=info(c.d),
      newLeading=now,currentWeakDegrees=basis_degrees(),
      temporaryWeightDenominatorNotDeclaredPhysicalUnit=True)
def reduce_target(raw):
 row=row_poly(raw);witness=[[] for _ in raw_seeds];steps=0
 while True:
  lead=leading(row)
  if lead is None:return witness,steps,None
  degree,column=lead
  if column not in weak:return None,steps,lead
  item=weak[column];bd=leading(item["row"])[0]
  if degree<bd:return None,steps,lead
  c=row[column][-1]/item["row"][column][-1]
  shift=degree-bd
  row=row_sub_multiple(row,item["row"],c,shift)
  witness=tag_add_multiple(witness,item["tags"],c,shift)
  now=leading(row);assert now is None or now<lead
  steps+=1
initial=[leftover,comm[1],comm[2],F6row]
initial_labels=["original_N1","true_T_square_z_ambiguity",
                "true_T_z_square_ambiguity","saved_full_original_F6"]
for raw,label in zip(initial,initial_labels):add_original_seed(raw,label)
MT2=mm(MT,MT)
MD=[[R(ell*A2 if i==j else 0)-MT2[i][j] for j in range(3)] for i in range(3)]
assert all(a==b for a,b in zip(MD[0],Drow))
found=None
for closure_level in range(2):
 target=[R(1),R(0),R(0)]
 for powerD in range(1,4):
  target=rm(target,MD)
  for powerLambda in range(4):
   actual_target=[v*lam**powerLambda for v in target]
   witness,steps,remainder_lead=reduce_target(actual_target)
   say("new_actual_original_D_power_row_module_target",
       closureLevel=closure_level,powerD=powerD,powerLambda=powerLambda,
       reductionSteps=steps,zeroRemainder=witness is not None,
       remainderLeading=remainder_lead,currentWeakDegrees=basis_degrees())
   if witness is not None:
    found=(powerD,powerLambda,actual_target,witness);break
  if found is not None:break
 if found is not None:break
 if closure_level==0:
  # These images are formed from the original four raw rows, not
  # from Gaussian rows containing unpaid weight inverses.
  # MT*v == T*v and Mz*v == z*v modulo the same three original means,
  # so all eight images are true original-ideal rows using only the
  # already paid weight/head denominators.
  for raw,label in zip(initial,initial_labels):
   add_original_seed(rm(raw,MT),label+"_actual_MT_image")
   add_original_seed(rm(raw,MZ),label+"_actual_Mz_image")
if found is None:
 say("new_original_lambda_row_module_D_target_unresolved",
     originalSeedCount=len(raw_seeds),currentWeakDegrees=basis_degrees(),
     rowOperations=row_operations,
     allOriginalRowsRemainInSameLocalizedIdeal=True,
     noWeightNecessaryPolynomialReturned=True,
     genericRankNotUsedForGlobalEmptiness=True,
     wholePhiFaceExcluded=False,ordinaryISPClaim=False)
 raise SystemExit(0)
powerD,powerLambda,actual_target,witness=found
alpha=[rebuild_lambda(p) for p in witness]
assert all(sum((a*r[j] for a,r in zip(alpha,raw_seeds)),R())==actual_target[j]
           for j in range(3))
final_den=oneP
for p in witness:
 for c in p:
  assert weight_only(c.d)
  gg=final_den.gcd(c.d)
  q=final_den/gg;assert q*gg==final_den
  final_den=q*c.d
assert weight_only(final_den)
betas=[]
for p in witness:
 beta=zeroP
 for i,c in enumerate(p):
  q=final_den/c.d;assert q*c.d==final_den
  beta=beta+c.n*q*Lp**i
 betas.append(beta)
assert all(sum((R(b)*r[j] for b,r in zip(betas,raw_seeds)),R())==
           R(final_den)*actual_target[j] for j in range(3))
say("complete_new_original_lambda_module_final_weight_denominator_identity",
    originalTarget="lambda^a * D^k",
    powerD=powerD,powerLambda=powerLambda,
    originalSeedLabels=seed_labels,
    finalWeightDenominator=info(final_den),
    clearedMultiplierProfiles=[info(b) for b in betas],
    completeAllThreeOriginalRationalCoefficientProductsReturned=True,
    allFinalWeightDenominatorsCleared=True,
    noTemporaryWeightPivotAssumedNonzeroAtOriginalPoints=True)
atoms=[("u",u.n),("u-1",(u-1).n),("Q",Q.n),("1-Q",delta.n),
       ("ell",ell.n),("u-ell",m.n),("M",M.n),("P02",P02.n),
       ("T0",T0.n),("J-Q",(J-Q).n),("u+Q-1",(u+Q-1).n),
       ("first_original_quadratic_head_chart_only",head_det.n)]
core=final_den;stripped=[]
for label,pp in atoms:
 while True:
  gg=core.gcd(pp)
  if gg.total_degree()==0:break
  q=core/gg;assert q*gg==core;core=q
  stripped.append([label,info(gg)])
core=core/core.coefficient(0);assert weight_only(core)
payload=json.dumps({"variables":["u","Q"],
    "terms":[[list(map(int,e[:2])),str(c)] for e,c in sorted(core.to_dict().items())]},
    separators=(",",":")).encode()
encoded=base64.b64encode(zlib.compress(payload,9)).decode()
back=json.loads(zlib.decompress(base64.b64decode(encoded)))
assert ctx.from_dict({tuple(e)+(0,0,0):fmpq(c) for e,c in back["terms"]})==core
for offset in range(0,len(encoded),80000):
 piece=encoded[offset:offset+80000]
 say("new_exact_weight_cover_payload_piece",
     index=offset//80000+1,dataChunk=piece,
     dataChunkSha256=hashlib.sha256(piece.encode()).hexdigest())
say("complete_new_first_head_original_lambda_module_weight_necessary_cover",
    core=info(core),powerD=powerD,powerLambda=powerLambda,
    exactClearedOriginalIdentity=True,
    strippedOnlyPaidWeightsAndNamedOriginalHead=stripped,
    payloadEncoding="concatenated dataChunk base64+zlib+json",
    payloadSha256=hashlib.sha256(payload).hexdigest(),
    payloadBytes=len(payload),
    concatenatedBase64Sha256=hashlib.sha256(encoded.encode()).hexdigest(),
    firstHeadZeroCurveRetained=True,
    allRemainingWeightDenominatorZeroCurvesRetained=True,
    entireFirstHeadChartExcluded=core.total_degree()==0,
    genericFieldUnitNotUsedForGlobalEmptiness=True,
    formerDTargetsAndF6RecurrenceNotRecomputed=True,
    wholePhiFaceExcluded=False,ordinaryISPClaim=False)

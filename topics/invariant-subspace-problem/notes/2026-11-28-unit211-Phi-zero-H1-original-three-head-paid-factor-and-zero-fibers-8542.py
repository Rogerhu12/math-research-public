#!/usr/bin/env python3
"""NEW original H1 scaled quadratic head: paid polynomial factors and exact zero fibres.
Only the 0ea9 source CONSTRUCTION through four cleared original rows is
used, never its old cofactors/norm-resultant tail. The new target is the
actual R/W/N1 head itself, with complete same-original-unit products.
If a nonconstant remainder survives, factor its true QQ norm and retain
each whole factor. At a new phi, first take the exact QQ gcd of g4 and
the actual head, then remove only QQ components of paid original units.
The whole finite-free original return uses the 125418 definitions only,
not its old six-factor driver. No modular saturation or generic-field
emptiness shortcut, and no change to P201/804 without a new theorem.
120 seconds /1 GiB. 2026-11-28 Asia/Taipei. No coefficient payload.
"""
import os,time,json,hashlib,signal,resource,contextlib,io
from pathlib import Path
from flint import fmpq,fmpq_poly
started=time.perf_counter();deadline=started+120
signal.alarm(120);resource.setrlimit(resource.RLIMIT_AS,(1024**3,1024**3))
def say(stage,**kw):
 kw.update(stage=stage,seconds=time.perf_counter()-started)
 print(json.dumps(kw,separators=(",",":")),flush=True)
def read_source(basename,sha,env):
 path=Path(os.environ.get(env,str(Path(__file__).with_name(basename))))
 raw=path.read_bytes();assert hashlib.sha256(raw).hexdigest()==sha
 return path,raw.decode()
vp,vs=read_source(
 "2026-11-28-unit211-Phi-zero-H1-polynomial-v-source-scaled-matrices-fixed-norm-input-8542.py",
 "5f6ba628dd4a660a7cedc7bb338a7cebc9cdc1ac3b6d6958a36409cb578b00ef",
 "ISP_H1_POLYNOMIAL_V_SOURCE")
marker="\n DD=ell*A2-Tr*Tr;B3="
assert vs.count(marker)==1
prefix=vs.split(marker,1)[0]+"\n return cleared,units\n"
assert "def whole_polynomial_module" not in prefix
ns={"__file__":str(vp),"__name__":"__four_original_polynomial_rows_for_NEW_head_target__"}
with contextlib.redirect_stdout(io.StringIO()):
 exec(compile(prefix,str(vp)+"::<new-head-only>","exec"),ns)
 original_rows,units=ns["new_original_polynomials"]()
signal.setitimer(signal.ITIMER_REAL,max(.001,deadline-time.perf_counter()))
A,P,pol,up,one,zero,qrow,det3,exact,monic,pdigest=[
 ns[k] for k in ["A","P","pol","up","one","zero","qrow","det3","exact","monic","pdigest"]]
u,Q=ns["u"],ns["Q"]
qr=[qrow(p) for p in original_rows]
heads=[[c.c[0] if c.c else A() for c in row[3:]] for row in qr]
assert det3(heads[:3])==0
original_head=det3([heads[i] for i in [0,1,3]])
assert original_head and original_head.d==one
ln=Q-2*(u-1)*(u-2);mn=u*Q-ln
units=units+[("whole_Q_equals_one_minus_u",Q+u-1),
 ("whole_rho_quadratic_head",(ln-Q)*(1-Q)*Q-2*mn*mn)]
head=A(original_head);paid_product=A(1);removed=[]
def score(a):
 assert a.d==one
 return sum(max(0,int(n.degree())+1) for n in a.n)
for label,unit in units:
 inverse=unit.inverse("NEW exact original head factor "+label)
 for k in range(64):
  new=head*inverse
  if new.d!=one or score(new)>=score(head):break
  assert unit*new==head
  head=new;paid_product=paid_product*unit
  if removed and removed[-1]["unit"]==label:removed[-1]["power"]+=1
  else:removed.append(dict(unit=label,power=1))
assert paid_product*head==original_head and head.d==one
say("new_H1_original_head_paid_factor_product",
 paidOriginalUnitsRemoved=removed,
 completeFourCoordinatePolynomialProductReturned=True,
 residualQDegree=max(i for i,c in enumerate(head.n) if c),
 residualCoefficientDegree=max(int(n.degree()) for n in head.n),
 residualIdentity=ns["pprofile"](P(head)),
 noUnpaidWeightFactorRemoved=True,originalHeadZeroStillRetained=True)
if not any(head.n[1:]) and head.n[0].degree()==0:
 say("new_H1_entire_original_three_head_is_a_paid_unit",
  exactRemainingConstant=str(head.n[0][0]),
  completeOriginalUnitFactorIdentity=True,
  allOriginalH1HeadZeroFibresExcluded=True,
  P201WeightPairUpperBoundUnchanged=804,ordinaryISPClaim=False)
 signal.alarm(0)
 raise SystemExit(0)

def det_poly(mat):
 mm=[row[:] for row in mat];n=len(mm);prev=one;sgn=1
 if not n:return one
 for j in range(n-1):
  if not mm[j][j]:
   sw=next((i for i in range(j+1,n) if mm[i][j]),None)
   if sw is None:return zero
   mm[j],mm[sw]=mm[sw],mm[j];sgn=-sgn
  pivot=mm[j][j]
  for i in range(j+1,n):
   for k in range(j+1,n):
    mm[i][k]=exact(mm[i][k]*pivot-mm[i][j]*mm[j][k],prev)
   mm[i][j]=zero
  prev=pivot
 return sgn*mm[-1][-1]
cols=[head*A([0]*j+[1]) for j in range(4)]
assert all(c.d==one for c in cols)
norm=det_poly([[cols[j].n[i] for j in range(4)] for i in range(4)])
assert norm
constant,factors=norm.factor();product=pol(constant)
for ff,e in factors:product=product*ff**e
assert product==norm
factors=[(monic(ff),int(e)) for ff,e in factors]
say("new_H1_actual_residual_head_QQ_norm_factorization",
 normIdentity=pdigest(norm),
 completeQQFactorProductReturned=True,
 factors=[dict(identity=pdigest(ff),multiplicity=e) for ff,e in factors],
 noEncodedOrSplitCoefficientPayload=True,allActualHeadZeroFactorsRetained=True)
known=[
 up,up-1,up-fmpq(3,2),up-fmpq(12,5),up-fmpq(5,2),
 pol([fmpq(-15,4),8,-5,1]),pol([4,-9,10,-5,1]),
 pol([fmpq(-52,9),20,fmpq(-995,36),fmpq(349,18),fmpq(-83,12),1]),
 pol([-8,fmpq(124,3),fmpq(-187,2),fmpq(709,6),fmpq(-4279,48),fmpq(319,8),fmpq(-39,4),1]),
 pol([fmpq(-864,11),fmpq(4464,11),fmpq(-7408,11),fmpq(6026,11),fmpq(-5255,22),fmpq(426,11),fmpq(291,22),fmpq(-81,11),1])]
known_sha={pdigest(ff)["sha256"] for ff in known}
known_sha.add("98fe71762eb2c2d0fd5a4e5ed09066704be36b65ee2e81ae88aa8a9f7a56b4cc")

hp,hs=read_source(
 "2026-11-28-unit211-Phi-zero-H1-six-nonlinear-source-poles-integral-original-fibers-8542.py",
 "877e4a078ded683c7db5488b101a09e0582a5831b0ffe7c05a69d6a89abdd4bf",
 "ISP_H1_INTEGRAL_MODEL_SOURCE")
hm="\ndef original_nonlinear_factors():"
assert hs.count(hm)==1
helper=hs.split(hm,1)[0]
assert "for modulus in original_nonlinear_factors" not in helper
env={"__file__":str(hp),"__name__":"__generic_original_integral_definitions_only__"}
with contextlib.redirect_stdout(io.StringIO()):
 exec(compile(helper,str(hp)+"::<new-head-zero-only>","exec"),env)
signal.setitimer(signal.ITIMER_REAL,max(.001,deadline-time.perf_counter()))

def exact_head_zero_QQ_model(modulus):
 env["A"]=env["QQA"];env["phi"]=monic(modulus);env["inverse_cache"]={}
 KA=env["A"];UP=env["U"];xgcd=env["xgcd"];divide=env["divide"]
 uu=KA(up);qq=UP([KA(),KA(1)])
 fullg=env["weight_quartic"](uu,qq)
 hh=UP([KA(n) for n in head.n])
 gh,aa,bb=xgcd(fullg,hh,"NEW actual head-zero QQ gcd")
 assert aa*fullg+bb*hh==gh
 if gh.degree()==0:
  say("new_H1_exact_head_zero_QQ_empty_component",
      phi=pdigest(modulus),actualG4HeadBezoutOneReturned=True)
  return [one]
 good=UP(gh);removed=UP(1);cuts=[]
 for label,value in env["cleared_weight_units"](uu,qq):
  value=UP(value)
  while good.degree()>0:
   gg,a,b=xgcd(good,value,"NEW head-zero original paid-unit gcd "+label)
   assert a*good+b*value==gg
   if gg.degree()==0:break
   new,rem=divide(good,gg,"NEW head-zero QQ unit-factor short division")
   assert not rem and new*gg==good
   good=new;removed=removed*gg;assert good*removed==gh
   cuts.append(dict(originalPaidUnit=label,removedQDegree=gg.degree()))
  if good.degree()==0:break
 for label,value in env["cleared_weight_units"](uu,qq):
  if good.degree()==0:break
  gg,a,b=xgcd(good,UP(value),"NEW complete head-zero good QQ model "+label)
  assert gg==1 and a*good+b*UP(value)==1
 say("new_H1_actual_head_zero_QQ_physical_model",
  phi=pdigest(modulus),originalG4HeadGcdDegree=gh.degree(),
  physicalGoodQDegree=good.degree(),exactPaidUnitCuts=cuts,
  originalG4AndActualHeadBezoutAndAllDivisionProductsReturned=True,
  zeroPointSourceIsActualHeadNotOnlyItsNorm=True)
 return [c.p for c in good.c]

statuses=[]
for modulus,multiplicity in factors:
 identity=pdigest(modulus)
 if identity["sha256"] in known_sha:
  rec=dict(phi=identity,normMultiplicity=multiplicity,headZeroExcluded=True,
   reason="entire u fibre already closed by original units or published C55 theorem",
   oldClosedFactorRecomputed=False)
  statuses.append(rec);say("new_H1_head_norm_factor_already_paid",**rec);continue
 try:
  qcoeff=exact_head_zero_QQ_model(modulus)
 except env["Nonunit"] as exc:
  rec=dict(phi=identity,headZeroExcluded=False,reason="QQ full component nonunit: "+str(exc))
  statuses.append(rec);say("accurate_new_H1_head_zero_component_retained",**rec);continue
 if len(qcoeff)==1:
  rec=dict(phi=identity,headZeroExcluded=True,
   reason="exact QQ original head-zero fibre contains only paid original unit zeros")
  statuses.append(rec);say("new_H1_head_zero_factor_complete",**rec);continue
 model=None;eligibility=[]
 for prime in env["PRIMES"]:
  try:model=env["build_modular_original_module"](modulus,qcoeff,prime)
  except env["Nonunit"] as exc:
   eligibility.append(dict(prime=prime,eligible=False,reason=str(exc)));continue
  eligibility.append(dict(prime=prime,eligible=True));break
 if model is None:
  rec=dict(phi=identity,headZeroExcluded=False,eligibility=eligibility,
   reason="no whole original lambda-six integral model in fixed eligibility primes")
  statuses.append(rec);say("accurate_new_H1_head_zero_component_retained",**rec);continue
 passed,history=env["complete_original_projection_ideal"](model,modulus)
 rec=dict(phi=identity,headZeroExcluded=passed,eligibility=eligibility,
  prime=model["prime"],finiteFreeRank=model["finiteFreeRank"],actualOriginalRankHistory=history,
  noPrimeChangedAfterOriginalIdealTest=True,
  conclusionScope="actual h=0 fibre only, not every Q root of this u factor")
 statuses.append(rec);say("new_H1_head_zero_factor_original_return",**rec)
say("new_H1_actual_head_factor_and_zero_fibres_finished",
 sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 actualResidualHeadNorm=pdigest(norm),factors=statuses,
 wholeOriginalH1ThreeHeadZeroExcluded=all(x["headZeroExcluded"] for x in statuses),
 noOldDixonOrPolynomialNormResultantTailExecuted=True,
 noOldC55OrSixNonlinearDriverReplayed=True,
 P201WeightPairUpperBoundUnchanged=804,
 noCoefficientPayloadTransmitted=True,ordinaryISPClaim=False,
 peakRSSKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
signal.alarm(0)

#!/usr/bin/env python3
"""NEW original Gauss return: the now-paid integral P201 versus three norms.

The published old monic P201 is now proved to belong to Z_(1009)[u],
with complete squarefree degree-201 reduction. This NEW input compares
that genuine reduction with the three fixed ORIGINAL polynomial norms.
All modular Bezout chains are multiplied back, including the composed
combination against P201 and every completed original norm. Fixed
lambda degrees and full Q4 regular norm are retained.

If H is the monic QQ gcd of P201 and these original necessary norms,
then H divides a monic Z_(1009) polynomial and is itself integral.
Its degree is therefore at most the ACTUAL final modular gcd degree.
This gives at most 4d weight pairs, 72d five-coordinate points and 144d
full normalized points; d=0 alone closes this whole H1 scope.
There is no identification of a modular irreducible factor with a QQ
factor. Since P201 is squarefree modulo 1009, any unclosed modular
factor labels a genuine whole Hensel block, not a chosen QQ branch.

Only necessary input coefficients are reconstructed. No old QQ Dixon
Gaussian, infinity degree certificate, assignment bound or C55 value
fiber is executed. No coefficient data is printed or saved.
120s / 1GiB. 2026-11-28 Asia/Taipei.
"""
import os,time,json,hashlib,signal,resource,contextlib,io
from pathlib import Path
from flint import fmpq,fmpq_poly,nmod_poly
START=time.perf_counter();DEADLINE=START+120;PRIME=1009
signal.alarm(120);resource.setrlimit(resource.RLIMIT_AS,(1024**3,1024**3))
def say(stage,**kw):
 kw.update(stage=stage,seconds=time.perf_counter()-START)
 print(json.dumps(kw,separators=(",",":")),flush=True)
def read_source(name,sha,environ):
 pp=Path(os.environ.get(environ,str(Path(__file__).with_name(name))))
 raw=pp.read_bytes();assert hashlib.sha256(raw).hexdigest()==sha
 return pp,raw.decode()
def digest(poly):
 raw=json.dumps([int(c) for c in poly.coeffs()],separators=(",",":")).encode()
 return dict(degree=int(poly.degree()),bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest())
def keep_deadline():
 signal.setitimer(signal.ITIMER_REAL,max(.001,DEADLINE-time.perf_counter()))
# The NEW comparison needs the true P201bar coefficients. Reconstruct
# them inside this runner from their paid original definition; do not
# transport a recomputable coefficient file through the tools/repository.
pp,ps=read_source(
 "2026-11-28-unit211-Phi-zero-H1-P201-modular-pole-support-degree-saturation-8542.py",
 "6a2dc6a4b2434c60d8d3c6532bda0c4b23524583665ac7b558e00a7db48b42f3",
 "ISP_H1_P201_REDUCTION_SOURCE")
end="\ntry:\n completed=main()"
cut="\n unit,factors=den.factor()"
assert ps.count(end)==ps.count(cut)==1
necessary=ps.split(end,1)[0].split(cut,1)[0]+"""
 # Here deg(den)=356<1009, so rad=den/gcd(den,den') is exact.
 assert den.degree()==356 and den.degree()<p
 rad=mmonic(mexact(den,den.gcd(den.derivative())))
 assert rad.gcd(rad.derivative()).degree()==0
 known=mp([0,1])*mp([-1,1])*Cbar
 shared=rad.gcd(known)
 support=mmonic(mexact(rad,shared))
 assert support*shared==rad
 assert support.degree()==201 and support.gcd(known).degree()==0
 return support
"""
penv={"__file__":str(pp),"__name__":"__P201_coefficients_for_new_original_Gauss_return__"}
with contextlib.redirect_stdout(io.StringIO()):
 exec(compile(necessary,str(pp)+":necessary-input","exec"),penv)
 Pbar=penv["main"]()
keep_deadline()
assert isinstance(Pbar,nmod_poly)
pid=digest(Pbar)
assert pid["degree"]==201
assert pid["sha256"]=="013656af6b2c65fe4d306c891b50aca9612b13ed9ae46c7e61d2e50b228dd029"
assert Pbar[Pbar.degree()]==1 and Pbar.gcd(Pbar.derivative()).degree()==0
say("new_P201_original_norm_Bezout_fixed_integral_input",
 prime=PRIME,actualP201Reduction=pid,
 monicCharacteristicZeroP201IntegralityAndDegreePaid=True,
 newTarget="complete original univariate Bezout against P201",
 oldQQDixonGaussianReplayed=False,
 originalConstantOneTargetRepublished=False,
 noCoefficientPayloadTransmitted=True)

vp,vs=read_source(
 "2026-11-28-unit211-Phi-zero-H1-polynomial-v-source-scaled-matrices-fixed-norm-input-8542.py",
 "5f6ba628dd4a660a7cedc7bb338a7cebc9cdc1ac3b6d6958a36409cb578b00ef",
 "ISP_H1_POLYNOMIAL_V_SOURCE")
tail="\nall_projections=[];all_names=[];all_modular_returns=[];common=None"
assert vs.count(tail)==1
definitions=vs.split(tail,1)[0]
old="headNorm= pdigest(polynomial_norm(head)),"
assert definitions.count(old)==1
definitions=definitions.replace(old,"headNormPreviouslyPublished=True,")
venv={"__file__":str(vp),"__name__":"__fixed_original_norm_inputs_for_new_P201_target__"}
with contextlib.redirect_stdout(io.StringIO()):
 exec(compile(definitions,str(vp)+":necessary-original-coefficients","exec"),venv)
keep_deadline()
# Only coefficient arithmetic definitions; do not call the former
# standalone norm driver or any degree-assignment/infinity certificate.
fh="\ndef modular_fixed_original_returns(projections,names):\n"
body=vs.split(fh,1)[1].split("\n converted=[]",1)[0]
body="\n".join(line[1:] if line.startswith(" ") else line for line in body.splitlines())
menv=dict(venv)
exec(compile(body,str(vp)+":actual-modular-coefficient-arithmetic","exec"),menv)
MA,MU,mp=menv["MA"],menv["MU"],menv["mp"]
common=Pbar;original_inputs=[Pbar];combination=[nmod_poly([1],PRIME)]
returned_norms=[];stopped_on_nonunit=None
expected=[
 ("RWN_O_scaled_T_commutator",[6,6],48,3179,
  "de730ca7321798d6f0d8477f4c4e1463e28dc8973fad83e388f91b1cf7f6e286"),
 ("RWN_O_scaled_T_complete_F6",[6,9],60,5131,
  "4851fda73cad1c4ab0f037677b0a1881dc5000ce0765960e3785acbf63bd6959"),
 ("RWN_O_scaled_T_complete_NV",[6,10],64,5407,
  "f655efcd20f3fec80d6b56090c53b895957fa66e17e21bf61045afe45e0acc02")]
generator=venv["whole_polynomial_module"]()
for index,expected_input in enumerate(expected):
 try:
  with contextlib.redirect_stdout(io.StringIO()):
   inputs,names=next(generator)
  label,degrees,size,ndegree,nsha=expected_input
  assert names[-1]==label
  assert [f.degree() for f in inputs]==degrees
  converted=[]
  for ff in inputs:
   assert all(aa.d==venv["one"] for aa in ff.c)
   converted.append(MU([MA([mp(co) for co in aa.n]) for aa in ff.c]))
  assert [f.degree() for f in converted]==degrees
  with contextlib.redirect_stdout(io.StringIO()):
   res,steps=menv["fixed_resultant"](converted[0],converted[1],
         "new actual P201 intersection with "+label)
  assert res.d==menv["mo"]
  norm=menv["mdet"](res.regular_numerator())
  norm_id=digest(norm)
  assert norm_id["degree"]==ndegree and norm_id["sha256"]==nsha
  # Each norm is the reduction of a fixed QQ polynomial determinant.
  # Its QQ u-degree need not be preserved: the monic P201 is the anchor.
  old_common=common
  common,a,b=old_common.xgcd(norm)
  assert a*old_common+b*norm==common
  original_inputs.append(norm)
  combination=[a*c for c in combination]+[b]
  assert sum((c*f for c,f in zip(combination,original_inputs)),nmod_poly([],PRIME))==common
  assert not Pbar%common
  quot,rem=divmod(Pbar,common);assert quot*common+rem==Pbar and not rem
  assert common.gcd(common.derivative()).degree()==0
  return_info=dict(label=label,fixedSymbolicLambdaDegrees=degrees,
   completeRegularNormSylvesterOrder=size,
   actualOriginalModularNorm=norm_id,
   allFixedLambdaLeadingDegreesKept=True,
   completeQ4ResultantAndNormReturned=True,
   allEuclideanDivisionsMultipliedBack=True,
   actualNewCommon=digest(common),
   twoPolynomialBezoutProductReturned=True,
   composedBezoutAgainstP201AndEveryCompletedNormReturned=True,
   composedCoefficientIdentities=[digest(c) for c in combination],
   actualP201ShortDivisionReturned=True)
  returned_norms.append(return_info)
  say("new_P201_fixed_original_norm_actual_Bezout",**return_info)
  if common.degree()==0:break
 except menv["Nonunit"] as exc:
  stopped_on_nonunit=str(exc)
  say("accurate_new_P201_original_norm_arithmetic_not_returned",
   index=index,reason=stopped_on_nonunit,
   onlyCompletedBezoutInputsUsed=True,allUnreturnedOriginalFibresRetained=True)
  break
keep_deadline()
unit,factors=common.factor();product=nmod_poly([int(unit)],PRIME);info=[]
for ff,ee in factors:
 assert int(ee)==1
 product=product*ff
 info.append(dict(**digest(ff),multiplicity=1))
assert product==common
d=int(common.degree())
assert 0<=d<=201
say("new_P201_original_norm_intersection_finished",
 sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 prime=PRIME,exactIntegralP201Reduction=pid,
 completeOriginalNormReturns=returned_norms,
 actualModularCommon=digest(common),actualModularFactors=info,
 allFactorProductsAndComposedBezoutReturned=True,
 newQQCommonDegreeUpperBound=d,
 newDistinctWeightPairUpperBound=4*d,
 newDistinctFiveCoordinatePointUpperBound=72*d,
 newDistinctFullNormalizedPointUpperBound=144*d,
 wholeH1Excluded=(d==0),
 scope="original Phi=0 physical D!=0 whole H1 graph",
 noQQIrreducibleFactorIdentification=True,
 onlyActualP201HenselBlocksInCommonRemain=True,
 incompleteArithmeticReason=stopped_on_nonunit,
 noOldDegreeAssignmentOrInfinityProofReplayed=True,
 noOldQQDixonGaussianReplayed=True,
 coefficientPayloadTransmitted=False,encodedOrSplitPayloadCreated=False,
 ordinaryISPClaim=False,peakRSSKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
signal.alarm(0)

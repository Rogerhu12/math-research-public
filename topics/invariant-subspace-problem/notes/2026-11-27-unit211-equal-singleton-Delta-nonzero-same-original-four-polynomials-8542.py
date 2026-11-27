#!/usr/bin/env python3
"""NEW entire remaining h=k, Delta nonzero: same original NV linear recovery.
The complete Delta zero face is now excluded. Regenerate only the original
compact row construction, not any former cofactor or projection gate.
Use the very same affine NV row to recover z, then return all four full
original mean/N1 polynomials in lambda,u,Q. Keep every new leading zero.
180 seconds /4 GiB. One fixed original construction-source dependency."""
import json,time,hashlib,signal,resource,contextlib,io,math,base64,zlib
from pathlib import Path
start=time.perf_counter();deadline=start+180;signal.alarm(180)
resource.setrlimit(resource.RLIMIT_AS,(4*1024**3,4*1024**3))
def say(stage,**kw):
 kw.update(stage=stage,seconds=time.perf_counter()-start);print(json.dumps(kw),flush=True)
dep=Path(__file__).with_name("2026-11-27-unit211-equal-singleton-global-compact-original-three-column-cofactors-8542.py")
raw=dep.read_bytes()
assert hashlib.sha256(raw).hexdigest()=="7bd915c3505e7c7e6bdd1aff7ec85362a29a2771b9f65f4ff5f8b8d067482bd8"
marker=b"\ndef cofactor(names):";assert raw.count(marker)==1
ns={"__file__":str(dep),"__name__":"__new_Delta_nonzero_same_original_NV_construction_only__"}
with contextlib.redirect_stdout(io.StringIO()):
 exec(compile(raw.split(marker)[0],str(dep),"exec"),ns)
signal.alarm(max(1,math.ceil(deadline-time.perf_counter())))
ctx=ns["ctx"];lp,up,qp=ctx.gens();zero,one=ctx.constant(0),ctx.constant(1)
R=ns["R"];rows=ns["rows"];profile=ns["profile"]
# This single addition is justified by the now complete original Delta zero exclusion.
ns["paid_atoms"].append(("whole_original_collision_Delta",ns["Delta"].n))
strip_paid=ns["strip_paid"];audit_den=ns["audit_den"]
a0,a1,a2=rows["NV"];assert not a2 and a1
audit_den(a1)
z0=-R(a0)/R(a1)
f0=-(ns["Pc"]+ns["bc"]*ns["Phi"]*z0)/ns["Pf"]
Fnum=ns["S"]*ns["xi"]*ns["Pc"]-ns["Phi"]*ns["NC"]
assert z0==ns["Tnum"]/(ns["bc"]*ns["Delta"])
assert f0==Fnum/ns["Delta"]
assert ns["Pf"]*f0+ns["Pc"]+ns["bc"]*ns["Phi"]*z0==0
assert ns["NF"]*f0+ns["NC"]+ns["bc"]*ns["S"]*ns["xi"]*z0==0
say("new_entire_Delta_nonzero_same_original_coordinates",
    allOriginalP1NVRecoveryProductsReturned=True,
    actualOriginalFormulas={"f":"Fnum/Delta","z=Qt":"Tnum/(bc*Delta)"},
    onlyNewUnitFromCompleteOriginalDeltaZeroExclusion=True,
    allNewLeadingZeroFibersRetained=True,noOldCofactorGateReplayed=True)
values={}
factor_values={}
def encode(pp):
 return [[list(map(int,e)),str(c)] for e,c in sorted(pp.to_dict().items())]
def save_values(stage,values):
 data={"variables":["lambda","u","Q"],"polynomials":{k:encode(v) for k,v in values.items()}}
 raw=json.dumps(data,separators=(",",":")).encode()
 back=json.loads(zlib.decompress(zlib.compress(raw,9)))
 assert all(ctx.from_dict({tuple(e):ns["fmpq"](c) for e,c in back["polynomials"][k]})==v
            for k,v in values.items())
 # Essential exact small input; do not emit any large regenerable matrices.
 say(stage,encoding="base64+zlib+json",uncompressedBytes=len(raw),
     payloadSHA256=hashlib.sha256(raw).hexdigest(),
     data=base64.b64encode(zlib.compress(raw,9)).decode(),
     allExactCoefficientReconstructionProductsReturned=True)
for name in ["R","W","O","N1"]:
 p0,p1,p2=rows[name]
 rawpoly=p0*a1*a1-p1*a0*a1+p2*a0*a0
 assert R(rawpoly)==R(a1*a1)*(R(p0)+R(p1)*z0+R(p2)*z0*z0)
 if not rawpoly:
  values[name]=zero
  say("new_Delta_nonzero_original_mean_identically_zero",name=name);continue
 core,paid,removed=strip_paid(rawpoly)
 scalar=core.coefficient(0);core=core/scalar;paid*=scalar
 assert paid*core==rawpoly
 values[name]=core
 headq=ctx.from_dict({(int(e[0]),int(e[1]),0):c for e,c in core.to_dict().items()
                      if int(e[2])==int(core.degrees()[2])})
 headlam=ctx.from_dict({(0,int(e[1]),int(e[2])):c for e,c in core.to_dict().items()
                      if int(e[0])==int(core.degrees()[0])})
 say("new_Delta_nonzero_full_same_original_necessary_polynomial",name=name,
     originalPolynomial=profile(rawpoly),necessaryPolynomial=profile(core,True),
     onlyPaidRemovals=removed,allOriginalSamePointProductsReturned=True,
     QLeadingCoefficient=profile(headq,True),
     lambdaLeadingCoefficient=profile(headlam,True),
     everyNewHeadZeroRetained=True,claimExcluded=core.total_degree()==0)
save_values("new_complete_Delta_nonzero_original_four_polynomials_exact_input",values)
for name,core in values.items():
 if not core:continue
 scalar,factors=core.factor();product=ctx.constant(scalar)
 records=[]
 for j,(fac,mult) in enumerate(factors):
  product*=fac**mult;label=name+"_factor_"+str(j)
  factor_values[label]=fac
  records.append(dict(name=label,multiplicity=int(mult),profile=profile(fac,True)))
 assert product==core
 say("new_Delta_nonzero_original_polynomial_complete_QQ_factor_product",
     name=name,scalar=str(scalar),irreducibleQQFactors=records,
     wholeQQFactorProductActuallyReturned=True,noNewFactorDeclaredUnit=True)
save_values("new_complete_Delta_nonzero_original_factor_inputs",factor_values)
say("new_entire_remaining_collision_Delta_nonzero_original_return_finished",
 sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 originalFourResidualsReturned=True,allSameOriginalFAndZ=True,
 allLambdaAndWeightLeadingZeroFibersRetained=True,
 noMultivariateGcdEmptinessInference=True,
 individualNBPBStillRequired=True,ordinaryISPClaim=False,
 peakRssKiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
signal.alarm(0)

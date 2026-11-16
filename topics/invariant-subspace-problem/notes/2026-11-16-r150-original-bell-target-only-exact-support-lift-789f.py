#!/usr/bin/env python3
"""Exact E source lift of a verified single original Bell field witness.

Author: Astra-ISP-789f / normal_annihilator.
AI-assisted: GPT-6 Astra Pro. Date: 2026-11-16.
A finite-field source chooses support and a genuine E unit only.
All original E monomial rows, including rows zero modulo127, are kept.
Save the entire rational unit solution before verification. Only an exact
full17-variable, all-three-E-components identity for 1 closes the problem.
"""
from __future__ import annotations
import argparse, gzip, hashlib, importlib.util, json, os, resource
import signal, subprocess, sys, time
from pathlib import Path
from flint import fmpq, fmpq_mat, nmod_mat

FORMAT="r150-original-bell-target-only-exact-support-lift-v1"
TARGET_DRIVER_SHA="8ac1e9275f9e3d3412f2744c0fe31acc06d58eda677ec270c9a37e39f9372b39"
TARGET_DRIVER_BYTES=26853
TARGET_FORMAT="r150-original-bell-target-only-source-v1"
FIELD_DRIVER_SHA="da80b727c47a050f3e268f00d1d6598336866a41b354d6aecb5edbb1ca1e730d"
FIELD_DRIVER_BYTES=31156
HELPER_SHA="31df769fb0fd3a41eb7606f500aae8b46952219c24927bd3265ed3dc34d7fe10"
PRIME=127
class Budget(Exception): pass
def need(ok,message):
    if not ok: raise ValueError(message)
def load_module(p,name):
    sp=importlib.util.spec_from_file_location(name,p); m=importlib.util.module_from_spec(sp); sp.loader.exec_module(m); return m
def raw_identity(p):
    h=hashlib.sha256()
    with p.open("rb") as f:
        while True:
            b=f.read(1048576)
            if not b: break
            h.update(b)
    return {"path":p.name,"bytes":p.stat().st_size,"sha256":h.hexdigest()}
def pinned_field(p):
    h=raw_identity(p); need(h["bytes"]==FIELD_DRIVER_BYTES and h["sha256"]==FIELD_DRIVER_SHA,"exact whole-field-source driver")
    return load_module(p,"r150_original_field_source_frozen")
def regular_column(a,power,f):
    v=[fmpq(0) for _ in range(5)]
    for i in range(3): v[i+power]=a[i]
    for k in (4,3):
        z=v[k]
        if z:
            for i in range(3): v[k-3+i]-=z*f[i]
        v[k]=fmpq(0)
    return v[:3]
def worker(a,fd):
    start=time.monotonic(); a.worker_output.mkdir(parents=True,exist_ok=True)
    inp=raw_identity(a.worker_input); model=json.loads(gzip.decompress(a.worker_input.read_bytes()))
    need(model["format"]==FORMAT+"-unit-input","exact E unit worker format")
    r=int(model["rank"]); need(1<=r<=2048,"bounded regular-representation order")
    f=[fmpq(x) for x in model["monicCubicLowerCoefficients"]]
    U=model["unitEntries"]; rhs=model["rightHandSide"]
    need(len(U)==r and all(len(row)==r for row in U) and len(rhs)==r,"complete original E unit and rhs")
    q=fmpq_mat(3*r,3*r); b=fmpq_mat(3*r,1)
    for i,row in enumerate(U):
        for j,x in enumerate(row):
            need(len(x)==3,"complete E coefficient triple"); x=[fmpq(t) for t in x]
            for power in range(3):
                z=regular_column(x,power,f)
                for k in range(3): q[3*i+k,3*j+power]=z[k]
        for k in range(3): b[3*i+k,0]=fmpq(rhs[i][k])
    begun=time.monotonic(); sol=q.solve(b,algorithm="dixon"); elapsed=time.monotonic()-begun
    # This complete candidate is written BEFORE multiplying back the unit.
    candidate={"format":FORMAT+"-unit-solution","binding":model["binding"],"unitInput":inp,
        "rank":r,"fullRegularSolution":[str(sol[i,0]) for i in range(3*r)],
        "allSolutionCoordinatesSaved":True,"allUnitRowsVerified":False}
    desc=fd.gz_save(a.worker_output/"complete-exact-E-unit-solution.json.gz",candidate)
    fd.json_save(a.worker_output/"unit-candidate-descriptor.json",desc)
    verified=(q*sol==b)
    need(verified,"all original regular-representation unit rows")
    rec={"format":FORMAT+"-unit-worker-receipt","binding":model["binding"],"status":"completed",
        "solution":desc,"allRegularRepresentationRowsVerified":True,"verifiedCoordinates":3*r,
        "dixonSeconds":elapsed,"elapsedSeconds":time.monotonic()-start,
        "maximumNumeratorBits":max(int(sol[i,0].numer()).bit_length() for i in range(3*r)),
        "maximumDenominatorBits":max(int(sol[i,0].denom()).bit_length() for i in range(3*r))}
    fd.json_save(a.worker_output/"unit-worker-receipt.json",rec); print(json.dumps(rec,separators=(",",":")),flush=True); return 0

def original_coefficients(model):
    z=fmpq(0); polys=[]
    for p in model["originalSeventeenGradients"]:
        one={}
        for e,c in p:
            e=tuple(e); need(len(e)==17 and e not in one,"all original gradient monomials"); one[e]=(fmpq(c),z,z)
        polys.append(one)
    bb={}
    for k,p in enumerate(model["BellFieldComponents"]):
        for e,c in p:
            e=tuple(e); v=bb.setdefault(e,[z,z,z]); v[k]+=fmpq(c)
    v=bb.setdefault((0,)*17,[z,z,z]); v[0]-=1
    polys.append({e:tuple(a) for e,a in bb.items() if any(a)})
    need(len(polys)==18,"all original affine generators")
    return polys
def original_entry(polys,row,slot):
    i,mu=slot; e=tuple(x-y for x,y in zip(row,mu))
    if min(e)<0: return (fmpq(0),)*3
    return polys[i].get(e,(fmpq(0),)*3)
def leading_columns(R,rank):
    piv=[]
    for i in range(rank):
        j=next((j for j in range(R.ncols()) if R[i,j]),None)
        need(j is not None,"full modular row-rank profile"); piv.append(j)
    need(piv==sorted(set(piv)),"ordered distinct modular pivots"); return piv
def qpoly(ctx,p):
    return ctx.from_dict({tuple(e):fmpq(c) for e,c in p})

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--field-driver",type=Path,required=True)
    ap.add_argument("--target-driver",type=Path)
    ap.add_argument("--helper",type=Path)
    ap.add_argument("--field-out",type=Path)
    ap.add_argument("--out",type=Path)
    ap.add_argument("--seconds",type=float,default=600)
    ap.add_argument("--memory-mib",type=int,default=4096)
    ap.add_argument("--max-unit-rank",type=int,default=512)
    ap.add_argument("--max-support",type=int,default=2048)
    ap.add_argument("--max-profile-elements",type=int,default=20000000)
    ap.add_argument("--unit-worker-input",type=Path,dest="worker_input")
    ap.add_argument("--worker-output",type=Path)
    a=ap.parse_args()
    need(512<=a.memory_mib<=8192,"bounded exact-source memory")
    resource.setrlimit(resource.RLIMIT_AS,(a.memory_mib*1048576,)*2)
    fd=pinned_field(a.field_driver)
    if a.worker_input is not None:
        need(a.worker_output is not None,"unit candidate output directory"); return worker(a,fd)
    need(a.target_driver is not None and a.helper is not None and a.field_out is not None and a.out is not None,"all exact-lift inputs")
    target_pin=raw_identity(a.target_driver)
    need(target_pin["bytes"]==TARGET_DRIVER_BYTES and target_pin["sha256"]==TARGET_DRIVER_SHA,
        "immutable target-only producer source")
    target_module=load_module(a.target_driver,"r150_actual_target_only_parent")
    need(0<a.seconds<=1800 and 1<=a.max_unit_rank<=2048 and 1<=a.max_support<=10000
        and 1<=a.max_profile_elements<=100000000,"bounded exact-support profile")
    hp=raw_identity(a.helper); need(hp["sha256"]==HELPER_SHA and hp["bytes"]==16964,"same original physical-model helper")
    a.out.mkdir(parents=True,exist_ok=True); start=time.monotonic(); deadline=start+a.seconds
    source=raw_identity(Path(__file__)); child=None
    rec={"format":FORMAT,"status":"running","source":source,"parameters":{
        "seconds":a.seconds,"memoryMiB":a.memory_mib,"maxUnitRank":a.max_unit_rank,
        "maxSupport":a.max_support,"maxProfileElements":a.max_profile_elements,
        "allOriginal17VariablesRetained":True,"characteristicZeroOriginalIdentityVerified":False}}
    receipt=a.out/"original-full-bell-exact-support-lift-receipt.json"
    manifest_path=a.out/"manifest.json"; manifest=None
    def save():
        rec["elapsedSeconds"]=time.monotonic()-start
        rec["parameters"]["peakParentRssKiB"]=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        rec["parameters"]["peakChildRssKiB"]=resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss
        fd.json_save(receipt,rec)
    def tick():
        if time.monotonic()>=deadline-2: raise Budget("exact original-source budget")
    def stop(signum,frame): raise Budget("signal "+str(signum))
    signal.signal(signal.SIGTERM,stop); signal.signal(signal.SIGINT,stop)
    code=1
    try:
        save(); tick()
        parent=json.loads((a.field_out/"manifest.json").read_bytes())
        expected_semantic=target_module.semantic(TARGET_DRIVER_SHA,9)
        need(parent["format"]==TARGET_FORMAT+"-manifest" and parent["semantic"]==expected_semantic
            and parent["binding"]==fd.digest(fd.canonical(expected_semantic)),
            "exact target-only original-parent semantic binding")
        rec["parameters"]["targetOnlyProducer"]=target_pin
        rec["parameters"]["fieldParentBinding"]=parent["binding"]
        if "positiveCandidate" not in parent:
            rec["status"]="completed-prefix"; rec["parameters"]["outcome"]="no-verified-single-original-field-source-yet"
            rec["parameters"]["targetDiscoveryReturned"]="discovery" in parent
            rec["parameters"]["noMathematicalNegativeConclusion"]=True
            save(); return 0
        packed=fd.gz_load(a.field_out,parent["model"])
        need(packed["format"]==TARGET_FORMAT+"-model" and packed["binding"]==parent["binding"]
            and fd.digest(fd.canonical(packed["data"]))==parent["modelDataSHA256"],
            "complete original model and data-only SHA")
        model=packed["data"];candidate=fd.gz_load(a.field_out,parent["positiveCandidate"])
        need(candidate["format"]==TARGET_FORMAT+"-positive" and candidate["binding"]==parent["binding"]
            and candidate["prime"]==127 and candidate["matchedPlace"]==100
            and candidate["homogeneousParameterPower"]==9
            and candidate["all18FieldOriginalSourceProductsVerified"]
            and candidate["all18HomogeneousOriginalProductsVerified"]
            and candidate["independentFlintHomogeneousAndAffineProductsVerified"]
            and candidate["characteristicZeroOriginalIdentityVerified"] is False
            and fd.digest(fd.canonical(candidate))==parent["positiveDataSHA256"],
            "actual whole single-column original field certificate")
        semantic={"format":FORMAT,"sourceSha256":source["sha256"],"fieldDriverSHA":FIELD_DRIVER_SHA,
            "targetOnlyProducerSHA256":TARGET_DRIVER_SHA,"helperSHA":HELPER_SHA,
            "fieldParentBinding":parent["binding"],"model":parent["model"],
            "fieldCandidate":parent["positiveCandidate"],
            "algorithm":"all-original-E-rows-selected-support-unit-and-full-polynomial-products"}
        binding=fd.digest(fd.canonical(semantic)); rec["binding"]=binding
        rec["parameters"]["completeOriginalModel"]=parent["model"]
        rec["parameters"]["fieldPositiveCandidate"]=parent["positiveCandidate"]
        if manifest_path.exists():
            manifest=json.loads(manifest_path.read_bytes())
            need(manifest["format"]==FORMAT+"-manifest" and manifest["binding"]==binding,"same exact-source checkpoint")
        else:
            manifest={"format":FORMAT+"-manifest","binding":binding,"verifiedComponents":[]}
            fd.json_save(manifest_path,manifest)
        m=fd.module(a.helper); polys=original_coefficients(model)
        source_polys=candidate["fullOriginalAffineSources"]
        need(len(source_polys)==18,"all original affine field-source labels")
        slots=[]; field_coeff=[]
        power=int(candidate["homogeneousParameterPower"])
        for i,poly in enumerate(source_polys):
            pp=fd.record_dict(poly,17)
            for mu,coef in sorted(pp.items()):
                need(sum(x*w for x,w in zip(mu,fd.WEIGHTS[:-1]))<=power-fd.SOURCE_WEIGHTS[i],
                    "each actual affine source term is within the paid homogeneous support")
                slots.append([i,list(mu)]); field_coeff.append(coef)
        n=len(slots); rec["parameters"]["allCandidateSourceTerms"]=n
        if n>a.max_support:
            rec["status"]="completed-prefix"; rec["parameters"]["outcome"]="actual-support-exceeds-resource-gate"
            save(); return 0
        need(n>0,"nonempty original source support")
        rows={(0,)*17}
        for i,mu in slots:
            for nu in polys[i]: rows.add(tuple(x+y for x,y in zip(mu,nu)))
        rows=sorted(rows); M=len(rows); rowpos={e:i for i,e in enumerate(rows)}
        rec["parameters"].update(completeOriginalMonomialRows=M,
            fieldZeroOriginalRowsRetained=True,completeProfileElements=M*n)
        if M*n>a.max_profile_elements:
            rec["status"]="completed-prefix"; rec["parameters"]["outcome"]="complete-profile-exceeds-resource-gate"
            save(); return 0
        bfield=nmod_mat([[int(e==(0,)*17)] for e in rows],PRIME)
        if "profile" in manifest:
            profile=fd.gz_load(a.out,manifest["profile"])
            need(profile["binding"]==binding and profile["allSourceSlots"]==slots
                and profile["allOriginalMonomialRows"]==[list(e) for e in rows],"unchanged complete selected support and all original rows")
        else:
            tick(); begin=time.monotonic(); ar=[[0]*n for _ in rows]
            for j,(i,mu) in enumerate(slots):
                for nu,x in polys[i].items():
                    e=tuple(v+w for v,w in zip(mu,nu))
                    ar[rowpos[e]][j]=sum(fd.q127(x[k])*pow(100,k,PRIME) for k in range(3))%PRIME
            A=nmod_mat(ar,PRIME); del ar
            c=nmod_mat([[x] for x in field_coeff],PRIME)
            need(A*c==bfield,"same complete field source after all E support rows are restored")
            rr,rank=A.rref(); rank=int(rank); J=leading_columns(rr,rank); del rr
            need(rank>0,"actual nonzero source image")
            AT=nmod_mat([[A[i,j] for i in range(M)] for j in J],PRIME)
            rt,rrank=AT.rref(); need(rrank==rank,"actual independent source columns")
            I=leading_columns(rt,rank); del rt,AT
            unit=nmod_mat([[A[i,j] for j in J] for i in I],PRIME)
            det=int(unit.det()); need(det!=0,"actual original selected unit determinant")
            bI=nmod_mat([[bfield[i,0]] for i in I],PRIME); x=unit.solve(bI)
            AJ=nmod_mat([[A[i,j] for j in J] for i in range(M)],PRIME)
            need(AJ*x==bfield,"all original field rows from the selected source section")
            profile={"format":FORMAT+"-profile","binding":binding,"rank":rank,
                "allSourceSlots":slots,"allOriginalMonomialRows":[list(e) for e in rows],
                "selectedOriginalRows":I,"selectedSourceColumns":J,"unitDeterminant127":det,
                "allOriginalFieldRowsVerified":True,"noCharacteristicZeroRankUpperClaim":True,
                "fieldSelectedSolution":[int(x[j,0]) for j in range(rank)]}
            manifest["profile"]=fd.gz_save(a.out/"complete-original-E-source-support-profile.json.gz",profile)
            fd.json_save(manifest_path,manifest)
            rec["parameters"]["profileSeconds"]=time.monotonic()-begin
            del A,AJ,unit,x,c,bI
        rank=profile["rank"]; I=profile["selectedOriginalRows"]; J=profile["selectedSourceColumns"]
        need(len(I)==len(J)==rank and len(set(I))==len(set(J))==rank,"complete selected E unit shape")
        rec["parameters"]["profile"]=manifest["profile"]; rec["parameters"]["actualUnitRank"]=rank
        if rank>a.max_unit_rank:
            rec["status"]="completed-prefix"; rec["parameters"]["outcome"]="paid-unit-rank-exceeds-current-exact-solve-gate"
            save(); return 0
        tick()
        if "unitInput" not in manifest:
            UU=[]
            for rowid in I:
                UU.append([[str(q) for q in original_entry(polys,rows[rowid],slots[colid])] for colid in J])
            unit_data={"format":FORMAT+"-unit-input","binding":binding,"rank":rank,
                "monicCubicLowerCoefficients":[str(fmpq(x,model["matchedCubic"][-1])) for x in model["matchedCubic"][:3]],
                "unitEntries":UU,
                "rightHandSide":[[str(int(rows[rowid]==(0,)*17)),"0","0"] for rowid in I],
                "originalProfile":manifest["profile"],"fieldNonzeroUnitDeterminant":profile["unitDeterminant127"]}
            manifest["unitInput"]=fd.gz_save(a.out/"complete-original-selected-E-unit.json.gz",unit_data)
            fd.json_save(manifest_path,manifest); del UU,unit_data
        unit_path=a.out/manifest["unitInput"]["path"]
        fd.gz_load(a.out,manifest["unitInput"])
        rec["parameters"]["unitInput"]=manifest["unitInput"]
        unit_dir=a.out; unit_dir.mkdir(exist_ok=True)
        solution_path=unit_dir/"complete-exact-E-unit-solution.json.gz"
        if not solution_path.exists():
            tick(); log=a.out/"exact-unit-worker.log"; begin=time.monotonic()
            argv=[sys.executable,str(Path(__file__).resolve()),"--field-driver",str(a.field_driver.resolve()),
                "--unit-worker-input",str(unit_path.resolve()),"--worker-output",str(unit_dir.resolve()),
                "--memory-mib",str(a.memory_mib)]
            rec["parameters"]["unitStage"]={"status":"running","regularOrder":3*rank}; save()
            with log.open("wb") as f:
                child=subprocess.Popen(argv,stdout=f,stderr=subprocess.STDOUT)
                try: ret=child.wait(timeout=max(1,deadline-time.monotonic()-3))
                except subprocess.TimeoutExpired:
                    child.terminate()
                    try: child.wait(timeout=5)
                    except subprocess.TimeoutExpired: child.kill(); child.wait()
                    child=None
                    rec["parameters"]["unitStage"].update(status="budget-checkpoint",elapsedSeconds=time.monotonic()-begin,
                        log=raw_identity(log),completeCandidateSaved=solution_path.exists())
                    save(); raise Budget("exact unit worker has no completed full verification yet")
                child=None
            rec["parameters"]["unitStage"].update(status="returned",exitCode=ret,
                elapsedSeconds=time.monotonic()-begin,log=raw_identity(log),completeCandidateSaved=solution_path.exists())
            if not solution_path.exists():
                with log.open("rb") as f:
                    f.seek(max(0,log.stat().st_size-6000)); rec["parameters"]["unitStage"]["logTail"]=f.read().decode("utf-8",errors="replace")
                need(False,"exact unit worker returned without a complete candidate")
        solution_bytes=gzip.decompress(solution_path.read_bytes())
        data=json.loads(solution_bytes)
        need(data["format"]==FORMAT+"-unit-solution" and data["binding"]==binding
            and data["unitInput"]==raw_identity(unit_path) and data["rank"]==rank
            and len(data["fullRegularSolution"])==3*rank and data["allSolutionCoordinatesSaved"],
            "complete saved exact unit solution bound to all original E entries")
        if "unitSolution" not in manifest:
            manifest["unitSolution"]={**raw_identity(solution_path),"logicalBytes":len(solution_bytes),"logicalSha256":fd.digest(solution_bytes)}
            fd.json_save(manifest_path,manifest)
        need(raw_identity(solution_path)=={k:manifest["unitSolution"][k] for k in ("path","bytes","sha256")},
            "same saved unit candidate bytes")
        need(len(solution_bytes)==manifest["unitSolution"]["logicalBytes"] and fd.digest(solution_bytes)==manifest["unitSolution"]["logicalSha256"],"complete unit candidate logical SHA")
        rec["parameters"]["unitSolution"]=manifest["unitSolution"]
        # Never rely on the unit-solve flag: full original E multiplication follows.
        if "nonzeroResidual" in manifest:
            old_residual=fd.gz_load(a.out,manifest["nonzeroResidual"])
            need(old_residual["binding"]==binding and old_residual["unitSolution"]==manifest["unitSolution"],
                "same fully saved nonzero original candidate residual")
            rec["parameters"]["nonzeroCandidateResidual"]=manifest["nonzeroResidual"]
            rec["parameters"]["outcome"]="selected-field-source-section-does-not-give-original-E-identity"
            rec["parameters"]["noGlobalNegativeConclusion"]=True
            rec["status"]="completed"; save(); return 0

        need(model["matchedCubic"]==m.MATCHED,"same exact matched coefficient field")
        sol=[fmpq(x) for x in data["fullRegularSolution"]]
        coeffs=[[{} for _ in range(3)] for _ in range(18)]
        complete_sources=[[] for _ in range(18)]
        for j,col in enumerate(J):
            i,mu=slots[col]; mu=tuple(mu); value=sol[3*j:3*j+3]
            if any(value):
                complete_sources[i].append([list(mu),[str(x) for x in value]])
            for k in range(3):
                if value[k]: coeffs[i][k][mu]=value[k]
        sp=[[m.CTX.from_dict(coeffs[i][k]) for k in range(3)] for i in range(18)]
        original_q=[qpoly(m.CTX,p) for p in model["originalSeventeenGradients"]]
        bell=[qpoly(m.CTX,p) for p in model["BellFieldComponents"]]
        bell[0]-=1
        f=[fmpq(x,model["matchedCubic"][-1]) for x in model["matchedCubic"][:3]]
        bell_matrix=[[m.CTX.from_dict({}) for _ in range(3)] for _ in range(3)]
        for power_j in range(3):
            v=[m.CTX.from_dict({}) for _ in range(5)]
            for k in range(3): v[k+power_j]=bell[k]
            for k in (4,3):
                for j in range(3): v[k-3+j]-=v[k]*f[j]
                v[k]=m.CTX.from_dict({})
            for k in range(3): bell_matrix[k][power_j]=v[k]
        need(manifest["verifiedComponents"]==list(range(len(manifest["verifiedComponents"])))
            and len(manifest["verifiedComponents"])<=3,"whole exact-component checkpoint order")
        all_zero=True
        for k in range(3):
            if k in manifest["verifiedComponents"]: continue
            tick(); begun=time.monotonic()
            rec["parameters"]["verificationPhase"]="complete-original-E-component-%d"%k; save()
            total=m.CTX.from_dict({})
            for i in range(17):
                total+=original_q[i]*sp[i][k]; tick()
            for j in range(3):
                total+=bell_matrix[k][j]*sp[17][j]; tick()
            if k==0: total-=1
            if total!=m.ZERO:
                rd=fd.gz_save(a.out/("complete-original-E-residual-component-%d.json.gz"%k),
                    {"format":FORMAT+"-nonzero-candidate-residual","binding":binding,"component":k,
                     "unitSolution":manifest["unitSolution"],"completeResidual":m.pv(total),
                     "meaning":"This selected source section did not lift; not an ideal nonmembership conclusion."})
                manifest["nonzeroResidual"]=rd; fd.json_save(manifest_path,manifest)
                rec["parameters"]["nonzeroCandidateResidual"]=rd
                rec["parameters"]["outcome"]="selected-field-source-section-does-not-give-original-E-identity"
                rec["parameters"]["noGlobalNegativeConclusion"]=True
                rec["status"]="completed"; all_zero=False; code=0; break
            manifest["verifiedComponents"].append(k); fd.json_save(manifest_path,manifest)
            rec["parameters"]["verifiedOriginalEComponents"]=list(manifest["verifiedComponents"])
            rec["parameters"]["lastComponentSeconds"]=time.monotonic()-begun; save()
            print(json.dumps({"phase":"complete-original-E-polynomial-product","component":k,
                "all17VariablesRetained":True,"allMonomialsZero":True,
                "elapsedSeconds":time.monotonic()-begun},separators=(",",":")),flush=True)
        if all_zero:
            need(manifest["verifiedComponents"]==[0,1,2],"all three complete original E products")
            affine={"format":FORMAT+"-exact-affine-source","binding":binding,
                "originalModel":parent["model"],"fieldParentBinding":parent["binding"],
                "sourceLabels":fd.SOURCE_LABELS[:-1]+["Bell-minus-one"],
                "all18OriginalESourcePolynomials":complete_sources,
                "coefficientBasis":["1","d","d^2"],"matchedCubic":model["matchedCubic"],
                "unitSolution":manifest["unitSolution"],"homogeneousWeightBound":power,
                "allThreeFullOriginalPolynomialProductsVerified":True,
                "identity":"sum(source_i * original_generator_i, i=0..17) = 1",
                "allMeanAndHankelVariablesRetained":True,
                "parameterDenominatorsUsed":False}
            ad=fd.gz_save(a.out/"complete-original-characteristic-zero-affine-source.json.gz",affine)
            exponent=(power+2)//3; common_weight=3*exponent; slp=[[] for _ in range(17)]
            for i in range(17):
                for mu,value in complete_sources[i]:
                    tt=common_weight-fd.SOURCE_WEIGHTS[i]-sum(x*w for x,w in zip(mu,fd.WEIGHTS[:-1]))
                    need(tt>=0,"complete weighted-homogenization source bound")
                    if tt%3==0:
                        slp[i].append({"monomial":mu,"coefficientE":value,"originalBellPower":tt//3})
            bd=fd.gz_save(a.out/"complete-original-characteristic-zero-bell-power-source-slp.json.gz",
                {"format":FORMAT+"-bell-power-source-slp","binding":binding,
                 "verifiedAffineSource":ad,"originalModel":parent["model"],
                 "bellExponent":exponent,"commonHomogeneousWeight":common_weight,
                 "all17OriginalGradientSourceExpressions":slp,
                 "identity":"original_Bell^bellExponent = sum(original_gradient_i * source_expression_i)",
                 "deduction":"Homogenize the verified affine identity to tt^power, multiply to weight divisible by3, reduce tt^3=Bell, and take the coefficient of1 in the free basis 1,tt,tt^2.",
                 "derivedFromAllThreeVerifiedOriginalEProducts":True,
                 "expandedBellPowerProductSeparatelyComputed":False})
            manifest["exactAffineSource"]=ad; manifest["exactBellPowerSourceSLP"]=bd
            fd.json_save(manifest_path,manifest)
            rec["parameters"].update(outcome="complete-original-characteristic-zero-Bell-nonzero-ideal-closed",
                characteristicZeroOriginalIdentityVerified=True,allOriginalEComponentsVerified=True,
                originalAffineSource=ad,originalBellPowerSourceSLP=bd,provedBellPower=exponent,
                allOriginalMeanAndHankelVariablesRetained=True,
                fullOriginalSourceSupportTerms=sum(len(p) for p in complete_sources))
            rec["status"]="completed"; code=0
    except Budget as e:
        rec["status"]="budget-checkpoint"; rec["parameters"]["error"]={"type":type(e).__name__,"message":str(e)}
        rec["parameters"]["noMathematicalNegativeConclusion"]=True; code=75
    except BaseException as e:
        rec["status"]="failed"; rec["parameters"]["error"]={"type":type(e).__name__,"message":str(e)}; code=1
    finally:
        if child is not None and child.poll() is None:
            child.terminate()
            try: child.wait(timeout=5)
            except subprocess.TimeoutExpired: child.kill(); child.wait()
        if manifest_path.exists(): rec["parameters"]["manifest"]=raw_identity(manifest_path)
        if manifest is not None:rec["parameters"]["wholePhaseState"]=manifest
        save(); print(json.dumps(rec,sort_keys=True,separators=(",",":")),flush=True)
    return code
if __name__=="__main__": raise SystemExit(main())

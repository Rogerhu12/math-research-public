#!/usr/bin/env python3
"""Lift three original Bell-fourth rational targets by one Q unit and three RHS.
Author: Astra-ISP-789f / normal_annihilator.
AI-assisted: GPT-6 Astra Pro. Date: 2026-11-16.

The field witness only selects a source support and a Q-invertible unit.
All rational output rows are retained, including every field-zero row.
No failed chosen section is called ideal nonmembership. Only three full
original polynomial products prove the E-valued original Bell fourth power identity.
"""
from __future__ import annotations
import argparse,gc,gzip,hashlib,importlib.util,json,resource,signal,subprocess,sys,time
from pathlib import Path
from flint import fmpq,fmpq_poly,fmpq_mat,nmod_mat,nmod_mpoly_ctx

FORMAT="r150-original-bell-fourth-even-three-rational-exact-source-v1"
PRODUCER_FORMAT="r150-original-bell-fourth-even-extension-three-rational-targets-v1"
PRODUCER_BYTES=40008
PRODUCER_SHA="a07425b29d36c685a7165436ae3acb51d633d159ccc7864294c21e9c92a580d2"
MODEL_BYTES=31156
MODEL_SHA="da80b727c47a050f3e268f00d1d6598336866a41b354d6aecb5edbb1ca1e730d"
HELPER_BYTES=16964
HELPER_SHA="31df769fb0fd3a41eb7606f500aae8b46952219c24927bd3265ed3dc34d7fe10"
P=7
WEIGHTS=(1,)*6+(2,)*11
SOURCE_WEIGHTS=(4,)*11+(5,)*6
class Budget(Exception):pass
def need(ok,message):
    if not ok:raise ValueError(message)
def identity(p):
    h=hashlib.sha256()
    with p.open("rb") as f:
        for b in iter(lambda:f.read(1048576),b""):h.update(b)
    return {"path":p.name,"bytes":p.stat().st_size,"sha256":h.hexdigest()}
def module(p,name):
    sp=importlib.util.spec_from_file_location(name,p)
    m=importlib.util.module_from_spec(sp);sp.loader.exec_module(m);return m
def pinned(p,size,digest,label):
    d=identity(p);need(d["bytes"]==size and d["sha256"]==digest,"immutable "+label);return d
def qdict(records):
    ans={}
    for ee,c in records:
        e=tuple(ee);need(len(e)==17 and e not in ans,"all distinct original rational monomials")
        v=fmpq(c);need(v!=0,"nonzero stored original coefficient");ans[e]=v
    return ans
def qpoly(m,records):
    return m.CTX.from_dict(qdict(records))
def leading_columns(R,r):
    piv=[]
    for i in range(r):
        j=next((j for j in range(R.ncols()) if R[i,j]),None)
        need(j is not None,"actual nonzero modular row");piv.append(j)
    need(piv==sorted(set(piv)),"ordered distinct modular pivot columns")
    return piv
def entry(polys,row,slot):
    i,mu=slot;e=tuple(x-y for x,y in zip(row,mu))
    if min(e)<0:return fmpq(0)
    return polys[i].get(e,fmpq(0))
def worker(a,fd):
    begin=time.monotonic();a.worker_output.mkdir(parents=True,exist_ok=True)
    raw=gzip.decompress(a.worker_input.read_bytes());data=json.loads(raw)
    need(data["format"]==FORMAT+"-unit-input","exact rational unit input")
    r=int(data["rank"]);need(1<=r<=4096,"bounded actual rational unit order")
    U=data["unitEntries"];B=data["rightHandSides"]
    need(len(U)==r and all(len(z)==r for z in U) and len(B)==r and
         all(len(z)==3 for z in B),"complete Q unit with three RHS")
    Q=fmpq_mat([[fmpq(c) for c in z] for z in U])
    R=fmpq_mat([[fmpq(c) for c in z] for z in B])
    started=time.monotonic();X=Q.solve(R,algorithm="dixon");solve_time=time.monotonic()-started
    candidate={"format":FORMAT+"-unit-solution","binding":data["binding"],
        "unitInput":identity(a.worker_input),"rank":r,"rightHandSideCount":3,
        "fullRationalSolutionRows":[[str(X[i,k]) for k in range(3)] for i in range(r)],
        "allSolutionCoordinatesSaved":True,"allOriginalUnitProductsVerified":False}
    desc=fd.gz_save(a.worker_output/"complete-original-rational-three-rhs-unit-solution.json.gz",candidate)
    fd.json_save(a.worker_output/"unit-candidate-descriptor.json",desc)
    need(Q*X==R,"all3r original rational unit products")
    rec={"format":FORMAT+"-unit-worker-receipt","status":"completed","binding":data["binding"],
        "solution":desc,"allOriginalRationalUnitProductsVerified":True,"verifiedUnitCoordinates":3*r,
        "matrixOrder":r,"rightHandSideCount":3,"dixonSeconds":solve_time,
        "maximumNumeratorBits":max(int(X[i,k].numer()).bit_length() for i in range(r) for k in range(3)),
        "maximumDenominatorBits":max(int(X[i,k].denom()).bit_length() for i in range(r) for k in range(3)),
        "elapsedSeconds":time.monotonic()-begin}
    fd.json_save(a.worker_output/"unit-worker-receipt.json",rec)
    print(json.dumps(rec,sort_keys=True,separators=(",",":")),flush=True);return 0
def q7(q):
    q=fmpq(q);d=int(q.denom())%P
    need(d!=0,"actual rational denominator is a 7-unit")
    return int(q.numer())%P*pow(d,-1,P)%P
def row_section(A,labels,cap):
    """Select literal original rows and columns; never use transformed rows as sources."""
    R,r=A.rref();r=int(r)
    if r>cap:return {"rank":r,"exceedsCap":True}
    if r==0:return {"rank":0,"rows":[],"columns":[],"determinant":1,"exceedsCap":False}
    J=leading_columns(R,r);del R
    T=nmod_mat([[A[i,j] for i in range(A.nrows())] for j in J],P)
    RT,rt=T.rref();need(int(rt)==r,"actual independent selected original columns")
    positions=leading_columns(RT,r)
    U=nmod_mat([[A[i,j] for j in J] for i in positions],P)
    determinant=int(U.det());need(determinant!=0,"selected literal original finite-field unit")
    return {"rank":r,"rows":[labels[i] for i in positions],"columns":J,
            "determinant":determinant,"exceedsCap":False}
def profile_fixture():
    data=[[1,0,2,0,3],[0,1,0,2,4],[1,1,2,2,0],[2,0,4,0,6],[0,0,1,1,1],[1,2,4,5,5]]
    I=[];sec=None
    for start in range(0,len(data),2):
        labels=I+list(range(start,min(start+2,len(data))))
        A=nmod_mat([data[i] for i in labels],P)
        sec=row_section(A,labels,10);I=sec["rows"]
    full=nmod_mat(data,P);r=int(full.rank());J=sec["columns"]
    need(r==sec["rank"] and len(I)==len(J)==r,"whole batched profile rank agrees with independent full rank")
    U=nmod_mat([[data[i][j] for j in J] for i in I],P)
    rows=nmod_mat([data[i] for i in I],P)
    section=nmod_mat([[data[i][j] for j in J] for i in range(len(data))],P)
    need(section*U.solve(rows)==full,"all original columns reconstructed in literal selected row/column fixture")
    need(row_section(nmod_mat([[0,0],[0,0]],P),[0,1],2)["rank"]==0,"whole zero-row fixture")
    return {"completeBatchedLiteralUnitSelectionVerified":True,"allFixtureOriginalProductsVerified":True}
def load_target(fd,field_out,desc,binding,k,rational):
    z=fd.gz_load(field_out,desc)
    suffix="-rational-fourth" if rational else "-field-fourth"
    need(z["format"]==PRODUCER_FORMAT+suffix and z["binding"]==binding and
         z["component"]==k and z["targetWeight"]==12,"complete same original target component")
    return z["records"]
def exact_fourth_component(m,model,k,bell,cube):
    F=m.Field();total=m.ZERO
    for i in range(3):
        for j in range(3):
            c=F.mul(fmpq_poly([0]*i+[1]),fmpq_poly([0]*j+[1]))[k]
            need(str(c)==model["coefficientMultiplicationTable"][i][j][k],"same original exact coefficient algebra")
            if c:total+=(cube[i]*bell[j])*c
    m.weighted(total,12)
    return total
def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--model-driver",type=Path,required=True)
    ap.add_argument("--producer",type=Path)
    ap.add_argument("--helper",type=Path)
    ap.add_argument("--field-out",type=Path)
    ap.add_argument("--out",type=Path)
    ap.add_argument("--seconds",type=float,default=600)
    ap.add_argument("--memory-mib",type=int,default=4096)
    ap.add_argument("--max-unit-rank",type=int,default=512)
    ap.add_argument("--max-support",type=int,default=3072)
    ap.add_argument("--profile-batch-rows",type=int,default=256)
    ap.add_argument("--unit-worker-input",dest="worker_input",type=Path)
    ap.add_argument("--worker-output",type=Path)
    a=ap.parse_args()
    need(512<=a.memory_mib<=8192,"bounded exact-source memory")
    resource.setrlimit(resource.RLIMIT_AS,(a.memory_mib*1048576,)*2)
    model_pin=pinned(a.model_driver,MODEL_BYTES,MODEL_SHA,"whole original model driver")
    fd=module(a.model_driver,"r150_three_q_original_model")
    if a.worker_input is not None:
        need(a.worker_output is not None,"complete rational worker output directory")
        return worker(a,fd)
    need(all(z is not None for z in (a.producer,a.helper,a.field_out,a.out)),"all original exact-source inputs")
    need(0<a.seconds<=3600 and 1<=a.max_unit_rank<=4096 and
         1<=a.max_support<=32768 and 16<=a.profile_batch_rows<=1024,"bounded exact-support gates")
    producer_pin=pinned(a.producer,PRODUCER_BYTES,PRODUCER_SHA,"three-target field producer")
    helper_pin=pinned(a.helper,HELPER_BYTES,HELPER_SHA,"original physical model helper")
    producer=module(a.producer,"r150_three_q_actual_parent")
    need(producer.FORMAT==PRODUCER_FORMAT,"correct actual field producer")
    a.out.mkdir(parents=True,exist_ok=True)
    begin=time.monotonic();deadline=begin+a.seconds;child=None;state=None
    manifest=a.out/"manifest.json";receipt=a.out/"original-bell-fourth-exact-source-receipt.json"
    own=identity(Path(__file__))
    rec={"format":FORMAT,"source":own,"status":"running","parameters":{
        "seconds":a.seconds,"memoryMiB":a.memory_mib,"maxUnitRank":a.max_unit_rank,
        "maxSupport":a.max_support,"profileBatchRows":a.profile_batch_rows,
        "allOriginal17VariablesAnd17GradientsRetained":True,"rationalRightHandSideCount":3,
        "characteristicZeroOriginalIdentityVerified":False}}
    def save():
        rec["elapsedSeconds"]=time.monotonic()-begin
        rec["parameters"]["peakParentRssKiB"]=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        rec["parameters"]["peakChildRssKiB"]=resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss
        if state is not None:rec["parameters"]["wholePhaseState"]=state
        fd.json_save(receipt,rec)
    def checkpoint():
        fd.json_save(manifest,state);rec["parameters"]["manifest"]=identity(manifest);save()
    def tick():
        if time.monotonic()>=deadline-3:raise Budget("three-rational-target exact-source budget")
    def stop(signum,frame):raise Budget("signal "+str(signum))
    signal.signal(signal.SIGTERM,stop);signal.signal(signal.SIGINT,stop)
    code=1
    try:
        save();tick()
        parent=json.loads((a.field_out/"manifest.json").read_bytes())
        psem=producer.semantic(PRODUCER_SHA)
        need(parent["format"]==PRODUCER_FORMAT+"-manifest" and parent["semantic"]==psem and
             parent["binding"]==fd.digest(fd.canonical(psem)),"exact three-target original-parent semantic binding")
        rec["parameters"].update(producer=producer_pin,helper=helper_pin,modelDriver=model_pin,
            fieldParentBinding=parent["binding"])
        if "positiveCandidate" not in parent:
            rec["status"]="completed-prefix";rec["parameters"].update(
                outcome="no-complete-three-original-field-sources-yet",noMathematicalNegativeConclusion=True)
            save();return 0
        packed=fd.gz_load(a.field_out,parent["baseModel"])
        need(packed["format"]==PRODUCER_FORMAT+"-base-model" and packed["binding"]==parent["binding"],"complete original rational model")
        model=packed["data"]
        candidate=fd.gz_load(a.field_out,parent["positiveCandidate"])
        need(candidate["format"]==PRODUCER_FORMAT+"-positive" and candidate["binding"]==parent["binding"] and
             candidate["prime"]==P and candidate["targetWeight"]==12 and
             candidate["originalGradientCount"]==17 and candidate["rationalTargetCount"]==3 and
             candidate["allThreeFullOriginalFieldPolynomialProductsVerified"] and
             candidate["allOriginal17VariablesRetained"] and
             candidate["characteristicZeroIdentityVerified"] is False and
             candidate["matchedCubic"]==model["matchedCubic"] and
             fd.digest(fd.canonical(candidate))==parent["positiveDataSHA256"],
             "actual three full original field-source certificates")
        sem={"format":FORMAT,"sourceSha256":own["sha256"],"modelDriverSHA256":MODEL_SHA,
            "producerSHA256":PRODUCER_SHA,"helperSHA256":HELPER_SHA,
            "fieldParentBinding":parent["binding"],"model":parent["baseModel"],"targetComponents":parent["targetComponents"],
            "candidate":parent["positiveCandidate"],"profileBatchRows":a.profile_batch_rows,
            "algorithm":"union-source-support-sparse-original-rows-batched-unit-three-Q-RHS-all-original-rational-products"}
        binding=fd.digest(fd.canonical(sem));rec["binding"]=binding
        if manifest.exists():
            state=json.loads(manifest.read_bytes())
            need(state["format"]==FORMAT+"-manifest" and state["binding"]==binding and
                 state["semantic"]==sem,"same exact rational-source checkpoint")
        else:
            state={"format":FORMAT+"-manifest","binding":binding,"semantic":sem,"verifiedComponents":[]}
            checkpoint()
        m=fd.module(a.helper)
        need(model["matchedCubic"]==m.MATCHED and model["all17OriginalGradientPolynomialsVerified"] and
             model["allWeightedEulerCoefficientsVerified"],"same exact original coefficient field and model")
        rec["parameters"]["batchedUnitArithmeticSelftest"]=profile_fixture()
        polys=[qdict(p) for p in model["originalSeventeenGradients"]]
        need(len(polys)==17 and len(parent["targetComponents"])==3,"all seventeen original rational gradients and three targets")
        components=candidate["allOriginalSourcePolynomialsByTarget"]
        need(len(components)==3 and all(len(z)==17 for z in components) and
             candidate["allEvenProjectionApplied"] and candidate["originalSquareExtension"]=="H_i=z_i^2",
             "all51 actual original-H source polynomials after valid even projection")
        by_target=[];slot_set=set()
        for k,component in enumerate(components):
            one={}
            for i,p in enumerate(component):
                pp=producer.dict7(p)
                for mu,c in pp.items():
                    need(sum(x*w for x,w in zip(mu,WEIGHTS))==12-SOURCE_WEIGHTS[i],
                         "exact original source homogeneous weight")
                    key=(i,mu);slot_set.add(key);one[key]=c
            by_target.append(one)
        ordered=sorted(slot_set);slots=[[i,list(mu)] for i,mu in ordered];n=len(slots)
        need(n==candidate["unionOriginalSourceSupportSize"] and n>0,"complete union of three actual source supports")
        support_sha=fd.digest(fd.canonical(slots))
        rec["parameters"].update(allCandidateSupportSlots=n,originalSupportSHA256=support_sha)
        if n>a.max_support:
            rec["status"]="completed-prefix";rec["parameters"]["outcome"]="actual-support-exceeds-current-resource-gate"
            checkpoint();return 0
        names=tuple(model["originalVariableNames"]);ctx=nmod_mpoly_ctx.get(names,P,"lex")
        fgens=[producer.dict7(p) for p in model["fieldOriginalSeventeenGenerators"]]
        targets7=[producer.dict7(load_target(fd,a.field_out,z["field"],parent["binding"],k,False))
                  for k,z in enumerate(parent["targetComponents"])]
        need(all(z["component"]==k and z["everyCoefficient7Integral"] and z["fullIndependentPrime7ProductVerified"]
                 for k,z in enumerate(parent["targetComponents"])),"all three original fourth target descriptors")
        for k in range(3):
            tick();total=ctx.from_dict({})
            for i in range(17):
                total+=ctx.from_dict(fgens[i])*ctx.from_dict(producer.dict7(components[k][i]));tick()
            need(total==ctx.from_dict(targets7[k]),"all original field polynomial rows reverified for actual source "+str(k))
        rec["parameters"]["allThreeOriginalFieldSourceIdentitiesReverified"]=True
        # Sparse field rows are only used to choose a true unit. Every rational row,
        # including every coefficient vanishing modulo7, is verified by the final Q polynomial products.
        source_rows={}
        for j,(i,mu) in enumerate(ordered):
            for e,c in fgens[i].items():
                out=tuple(x+y for x,y in zip(e,mu))
                one=source_rows.setdefault(out,{})
                need(j not in one,"one original coefficient per source slot and output row")
                one[j]=c
            if j%32==0:tick()
        rows=sorted(source_rows);M=len(rows);row_pos={e:i for i,e in enumerate(rows)}
        rows_sha=fd.digest(fd.canonical([list(e) for e in rows]))
        need(all(e in row_pos for q in targets7 for e in q),"every nonzero field target row occurs in the complete source row set")
        rec["parameters"].update(allNonzeroFieldSourceRows=M,sparseFieldSourceEntries=sum(map(len,source_rows.values())),
            originalFieldRowsSHA256=rows_sha,fullWeightTwelveMacaulayMatrixConstructed=False,
            allRationalRowsVerifiedOnlyByFinalFullPolynomialProducts=True)
        if "profile" not in state:
            if "rowProfilePrefix" in state:
                pre=fd.gz_load(a.out,state["rowProfilePrefix"])
                need(pre["format"]==FORMAT+"-row-prefix" and pre["binding"]==binding and
                     pre["supportSHA256"]==support_sha and pre["rowDictionarySHA256"]==rows_sha,
                     "same literal source support and original row-prefix checkpoint")
                cursor=int(pre["scannedRows"]);I=[tuple(e) for e in pre["selectedRows"]];J=pre["selectedColumns"]
                need(0<=cursor<=M and len(I)==len(J)==pre["rank"] and len(set(I))==len(I) and
                     all(e in row_pos and row_pos[e]<cursor for e in I),"all cached unit rows are paid original rows")
                if I:
                    U=nmod_mat([[source_rows[e].get(j,0) for j in J] for e in I],P)
                    need(int(U.det())==pre["unitDeterminant7"]!=0,"cached actual original unit reverified")
            else:cursor=0;I=[];J=[]
            started=time.monotonic()
            while cursor<M and len(I)<n:
                tick();end=min(cursor+a.profile_batch_rows,M);labels=I+rows[cursor:end]
                A=nmod_mat([[source_rows[e].get(j,0) for j in range(n)] for e in labels],P)
                section=row_section(A,labels,a.max_unit_rank);del A
                if section["exceedsCap"]:
                    rec["status"]="completed-prefix";rec["parameters"].update(
                        outcome="actual-source-profile-rank-exceeds-current-Q-unit-resource-gate",
                        nextWholeBatchActualRank=section["rank"],lastPaidRows=cursor,
                        noRationalRankUpperOrNegativeClaim=True)
                    checkpoint();return 0
                I=section["rows"];J=section["columns"];cursor=end
                pre={"format":FORMAT+"-row-prefix","binding":binding,"supportSHA256":support_sha,
                    "rowDictionarySHA256":rows_sha,"scannedRows":cursor,"rank":len(I),
                    "selectedRows":[list(e) for e in I],"selectedColumns":J,
                    "unitDeterminant7":section["determinant"]}
                state["rowProfilePrefix"]=fd.gz_save(a.out/("whole-batched-original-row-profile-prefix-%08d.json.gz"%cursor),pre)
                checkpoint()
            r=len(I);need(r>0 and len(J)==r and (cursor==M or r==n),"complete actual field profile without a rational rank claim")
            U=nmod_mat([[source_rows[e].get(j,0) for j in J] for e in I],P)
            determinant=int(U.det());need(determinant!=0,"actual literal original rational unit modulo7")
            BI=nmod_mat([[targets7[k].get(e,0) for k in range(3)] for e in I],P)
            X=U.solve(BI)
            for k in range(3):
                total=ctx.from_dict({});section_sources=[{} for _ in range(17)]
                for h,j in enumerate(J):
                    i,mu=ordered[j];c=int(X[h,k])
                    if c:section_sources[i][mu]=c
                for i in range(17):total+=ctx.from_dict(fgens[i])*ctx.from_dict(section_sources[i]);tick()
                need(total==ctx.from_dict(targets7[k]),"all original field rows in the chosen source section "+str(k))
            profile={"format":FORMAT+"-profile","binding":binding,"rank":r,
                "allSourceSlots":slots,"allFieldSourceRowDictionarySHA256":rows_sha,
                "allNonzeroFieldSourceRows":M,"scannedOriginalRows":cursor,
                "selectedOriginalMonomials":[list(e) for e in I],"selectedSourceColumns":J,
                "unitDeterminant7":determinant,
                "fieldSelectedSolutionRows":[[int(X[i,k]) for k in range(3)] for i in range(r)],
                "allThreeOriginalFieldPolynomialRowsVerified":True,"noRationalRankUpperClaim":True}
            state["profile"]=fd.gz_save(a.out/"complete-original-three-rational-source-profile.json.gz",profile)
            rec["parameters"]["profileSeconds"]=time.monotonic()-started;checkpoint()
            del U,BI,X
        else:profile=fd.gz_load(a.out,state["profile"])
        need(profile["format"]==FORMAT+"-profile" and profile["binding"]==binding and
             profile["allSourceSlots"]==slots and profile["allFieldSourceRowDictionarySHA256"]==rows_sha and
             profile["allNonzeroFieldSourceRows"]==M and profile["allThreeOriginalFieldPolynomialRowsVerified"],
             "same exact original support and field polynomial-row source certificate")
        r=int(profile["rank"]);I=[tuple(e) for e in profile["selectedOriginalMonomials"]];J=profile["selectedSourceColumns"]
        need(len(I)==len(J)==r and len(set(I))==len(set(J))==r and
             all(e in row_pos for e in I) and all(0<=j<n for j in J),"actual original unit monomial and source indices")
        actual_unit=nmod_mat([[source_rows[e].get(j,0) for j in J] for e in I],P)
        need(int(actual_unit.det())==profile["unitDeterminant7"]!=0,"every restored original unit remains nonzero")
        rec["parameters"].update(actualUnitRank=r,profile=state["profile"],rationalMatrixOrder=r,rightHandSideCount=3)
        if r>a.max_unit_rank:
            rec["status"]="completed-prefix";rec["parameters"]["outcome"]="actual-Q-unit-order-exceeds-current-solve-gate"
            checkpoint();return 0
        if "unitInput" not in state:
            tick();RHS=[["0"]*3 for _ in range(r)];where={e:i for i,e in enumerate(I)}
            for k,z in enumerate(parent["targetComponents"]):
                records=load_target(fd,a.field_out,z["rational"],parent["binding"],k,True)
                for ee,c in records:
                    e=tuple(ee)
                    if e in where:RHS[where[e]][k]=str(fmpq(c))
                need(all(q7(RHS[h][k])==targets7[k].get(I[h],0) for h in range(r)),
                     "all exact target unit RHS reduce to their original field values")
                del records;gc.collect();tick()
            data={"format":FORMAT+"-unit-input","binding":binding,"rank":r,
                "unitEntries":[[str(entry(polys,e,slots[j])) for j in J] for e in I],
                "rightHandSides":RHS,"originalProfile":state["profile"],
                "fieldUnitDeterminant":profile["unitDeterminant7"]}
            state["unitInput"]=fd.gz_save(a.out/"complete-original-rational-unit-three-rhs.json.gz",data)
            checkpoint();del data,RHS
        del source_rows,rows,row_pos,targets7,fgens,by_target,slot_set,components,actual_unit
        gc.collect()
        fd.gz_load(a.out,state["unitInput"])
        unit_path=a.out/state["unitInput"]["path"]
        solution_path=a.out/"complete-original-rational-three-rhs-unit-solution.json.gz"
        if not solution_path.exists():
            tick();log=a.out/"exact-three-rhs-unit-worker.log";started=time.monotonic()
            argv=[sys.executable,str(Path(__file__).resolve()),"--model-driver",str(a.model_driver.resolve()),
                "--unit-worker-input",str(unit_path.resolve()),"--worker-output",str(a.out.resolve()),
                "--memory-mib",str(a.memory_mib)]
            rec["parameters"]["unitStage"]={"status":"running","matrixOrder":r,"rightHandSideCount":3};save()
            with log.open("wb") as f:
                child=subprocess.Popen(argv,stdout=f,stderr=subprocess.STDOUT)
                try:ret=child.wait(timeout=max(1,deadline-time.monotonic()-3))
                except subprocess.TimeoutExpired:
                    child.terminate()
                    try:child.wait(timeout=5)
                    except subprocess.TimeoutExpired:child.kill();child.wait()
                    child=None
                    rec["parameters"]["unitStage"].update(status="budget-checkpoint",log=identity(log),
                        elapsedSeconds=time.monotonic()-started,completeCandidateSaved=solution_path.exists())
                    save();raise Budget("complete rational three-RHS candidate not fully consumed yet")
                child=None
            rec["parameters"]["unitStage"].update(status="returned",exitCode=ret,log=identity(log),
                elapsedSeconds=time.monotonic()-started,completeCandidateSaved=solution_path.exists())
            if not solution_path.exists():
                with log.open("rb") as f:
                    f.seek(max(0,log.stat().st_size-6000))
                    rec["parameters"]["unitStage"]["logTail"]=f.read().decode("utf-8",errors="replace")
                need(False,"rational unit worker returned without a complete saved candidate")
        raw=gzip.decompress(solution_path.read_bytes());soldata=json.loads(raw)
        need(soldata["format"]==FORMAT+"-unit-solution" and soldata["binding"]==binding and
             soldata["unitInput"]==identity(unit_path) and soldata["rank"]==r and
             soldata["rightHandSideCount"]==3 and soldata["allSolutionCoordinatesSaved"] and
             len(soldata["fullRationalSolutionRows"])==r and
             all(len(z)==3 for z in soldata["fullRationalSolutionRows"]),"all3r exact source coordinates saved")
        sd={**identity(solution_path),"logicalBytes":len(raw),"logicalSha256":fd.digest(raw)}
        if "unitSolution" in state:need(state["unitSolution"]==sd,"same complete saved rational unit candidate")
        else:state["unitSolution"]=sd;checkpoint()
        rec["parameters"]["unitSolution"]=sd
        # A saved Dixon candidate is consumed before any new solve, but its full
        # original unit equations and its original field values are still verified here.
        unit_data=fd.gz_load(a.out,state["unitInput"])
        Uq=fmpq_mat([[fmpq(c) for c in row] for row in unit_data["unitEntries"]])
        Bq=fmpq_mat([[fmpq(c) for c in row] for row in unit_data["rightHandSides"]])
        Xq=fmpq_mat([[fmpq(c) for c in row] for row in soldata["fullRationalSolutionRows"]])
        need(Uq*Xq==Bq,"all3r restored original rational unit products")
        need([[q7(Xq[i,k]) for k in range(3)] for i in range(r)]==
             profile["fieldSelectedSolutionRows"],"all Q source coefficients reduce to the actual selected field unit solution")
        rec["parameters"]["allOriginalRationalUnitCoordinatesVerified"]=3*r
        del unit_data,Uq,Bq,Xq;gc.collect()
        if "nonzeroResidual" in state:
            old=fd.gz_load(a.out,state["nonzeroResidual"])
            need(old["binding"]==binding and old["unitSolution"]==sd,"same paid nonzero chosen-section residual")
            rec["parameters"].update(outcome="this-chosen-source-section-does-not-lift-to-Q",
                nonzeroCandidateResidual=state["nonzeroResidual"],noIdealNonmembershipConclusion=True)
            rec["status"]="completed";save();return 0
        sol=[[fmpq(z) for z in row] for row in soldata["fullRationalSolutionRows"]]
        support=[[{} for _ in range(17)] for _ in range(3)]
        for j,col in enumerate(J):
            i,mu=slots[col];mu=tuple(mu)
            for k in range(3):
                if sol[j][k]:support[k][i][mu]=sol[j][k]
        sources=[[m.CTX.from_dict(z) for z in component] for component in support]
        original=[qpoly(m,p) for p in model["originalSeventeenGradients"]]
        bell=[qpoly(m,p) for p in model["BellFieldComponents"]]
        cube=[qpoly(m,p) for p in model["naturalCubeRationalComponents"]]
        need(state["verifiedComponents"]==list(range(len(state["verifiedComponents"]))) and
             len(state["verifiedComponents"])<=3,"whole exact polynomial verification cursor")
        all_zero=True
        for k in range(3):
            if k in state["verifiedComponents"]:continue
            tick();started=time.monotonic();total=m.ZERO
            for i in range(17):
                total+=original[i]*sources[k][i];tick()
            expected=exact_fourth_component(m,model,k,bell,cube)
            records=load_target(fd,a.field_out,parent["targetComponents"][k]["rational"],parent["binding"],k,True)
            saved=qpoly(m,records);del records
            need(saved==expected,"independent entire exact original Bell fourth coefficient "+str(k))
            del saved;total-=expected;del expected;gc.collect()
            if total!=m.ZERO:
                state["nonzeroResidual"]=fd.gz_save(a.out/("complete-original-Q-residual-%d.json.gz"%k),
                    {"format":FORMAT+"-chosen-section-nonzero-residual","binding":binding,"component":k,
                     "unitSolution":sd,"completeOriginalResidual":m.pv(total),
                     "meaning":"Only this selected source section failed; other sections on the same support or a larger support remain possible."})
                rec["parameters"].update(outcome="this-chosen-source-section-does-not-lift-to-Q",
                    nonzeroCandidateResidual=state["nonzeroResidual"],noIdealNonmembershipConclusion=True)
                rec["status"]="completed";checkpoint();all_zero=False;code=0;break
            state["verifiedComponents"].append(k);checkpoint()
            rec["parameters"]["verifiedFullOriginalRationalComponents"]=state["verifiedComponents"]
            print(json.dumps({"phase":"complete-original-rational-fourth-product","component":k,
                "allOriginal17VariablesRetained":True,"allOriginalPolynomialCoordinatesZero":True,
                "elapsedSeconds":time.monotonic()-started},separators=(",",":")),flush=True)
        if all_zero:
            need(state["verifiedComponents"]==[0,1,2],"all three complete original characteristic-zero products")
            combined=[]
            for i in range(17):
                exps=set().union(*(set(support[k][i]) for k in range(3)))
                combined.append([[list(mu),[str(support[k][i].get(mu,fmpq(0))) for k in range(3)]]
                                 for mu in sorted(exps)])
            exact={"format":FORMAT+"-exact-original-bell-fourth-source","binding":binding,
                "originalModel":parent["baseModel"],"fieldParentBinding":parent["binding"],
                "coefficientBasis":["1","d","d^2"],"matchedCubic":model["matchedCubic"],
                "originalSourceLabels":model["sourceLabels"][:17],
                "allSeventeenSourcesByRationalComponent":[[m.pv(z) for z in c] for c in sources],
                "allSeventeenOriginalEFourthSources":combined,"unitSolution":sd,
                "targetWeight":12,"allThreeFullOriginalRationalPolynomialProductsVerified":True,
                "identity":"original_Bell^4 = sum(original_gradient_i * original_E_source_i, i=0..16)",
                "parameterDenominatorsUsed":False,"allOriginalMeanAndHankelVariablesRetained":True}
            desc=fd.gz_save(a.out/"complete-original-characteristic-zero-bell-fourth-source.json.gz",exact)
            affine=fd.gz_save(a.out/"complete-original-bell-one-source-slp.json.gz",
                {"format":FORMAT+"-bell-one-source-slp","binding":binding,"verifiedFourthSource":desc,
                 "gradientSources":"same seventeen verified E source polynomials",
                 "BellMinusOneSource":"-(original_Bell^3+original_Bell^2+original_Bell+1)",
                 "identity":"1 = sum(original_gradient_i * original_E_source_i) - (original_Bell-1)*(original_Bell^3+original_Bell^2+original_Bell+1)",
                 "deducedByExactPolynomialFactorization":True,"separateExpandedAffineProductClaimed":False})
            state["exactFourthSource"]=desc;state["exactBellOneSourceSLP"]=affine
            rec["parameters"].update(outcome="complete-original-characteristic-zero-Bell-fourth-source",
                characteristicZeroOriginalIdentityVerified=True,provedBellPower=4,
                allThreeFullOriginalRationalPolynomialProductsVerified=True,
                exactOriginalFourthSource=desc,exactOriginalBellOneSourceSLP=affine,
                fullOriginalSourceTerms=sum(len(p) for p in combined),rationalUnitOrder=r,
                noThreefoldRegularRepresentationUsed=True)
            rec["status"]="completed";checkpoint();code=0
    except Budget as e:
        rec["status"]="budget-checkpoint";rec["parameters"]["error"]={"type":type(e).__name__,"message":str(e)}
        rec["parameters"]["noMathematicalNegativeConclusion"]=True;code=75
    except BaseException as e:
        rec["status"]="failed";rec["parameters"]["error"]={"type":type(e).__name__,"message":str(e)};code=1
    finally:
        if child is not None and child.poll() is None:
            child.terminate()
            try:child.wait(timeout=5)
            except subprocess.TimeoutExpired:child.kill();child.wait()
        if manifest.exists():rec["parameters"]["manifest"]=identity(manifest)
        save();print(json.dumps(rec,sort_keys=True,separators=(",",":")),flush=True)
    return code
if __name__=="__main__":raise SystemExit(main())

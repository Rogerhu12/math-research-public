#!/usr/bin/env python3
"""Rebuild original Gamma200 inputs and run the new weight-eleven rank bound.
Author: Astra-ISP-b2a9acde-20261120 / root; AI-assisted GPT-6 Astra Pro.
Read-only Actions runner. Arrays, inputs, receipts and minor records stay in TMP.
The paid weight-ten matrix is never recomputed. Its immutable parent sources are
rebuilt solely because their temporary original coefficient streams are absent.
"""
import argparse, ast, datetime, gc, hashlib, importlib.util, json, os
import resource, signal, struct, subprocess, sys, time
from collections import Counter
from pathlib import Path
from types import SimpleNamespace

TOPIC="topics/invariant-subspace-problem/"
NOTES=TOPIC+"notes/"
OLD_PLAN=NOTES+"2026-11-16-r150-original-weight10-macaulay-session-request-789f.json"
OLD_PLAN_SHA="2dc4a2725835c6aa3f3c09f4b48dad893e8da2165266e2634ca3b1da49744e50"
RULES={"README.md":"282e86b03385d3b6245ce7100ae2e2af7b103c2d",
       TOPIC+"README.md":"4d6570e9cf346431ab781a1290076a6321aaaa00"}
G=200
TERMS=8037189
TARGET_TERMS=2604
PREPARED_FORMAT="r150-original-delta-weight10-homogeneous127-runtime-parent-v1"
SEED=0x4252414e43483131
NATIVE=NOTES+"2026-11-20-r150-weight11-projected-rank-b2a9.cpp"
HEADER=NOTES+"2026-11-15-r150-original-f127-bitplane-789f.hpp"
NATIVE_SHA="d1dad93a00276355d2fdb3f815e01fde5ee428e72f1ca074063e961e7aa62253"
HEADER_SHA="03272796bb20c883291d27c9a0b796197f8295ccd9b16552c13894657dc8afd3"

def need(v,s):
    if not v: raise ValueError(s)
def canon(x):
    return json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=True).encode("ascii")
def sha(b):
    return hashlib.sha256(b).hexdigest()
def identity(p):
    p=Path(p); h=hashlib.sha256()
    with p.open("rb") as f:
        for b in iter(lambda:f.read(1048576),b""): h.update(b)
    return {"path":p.name,"bytes":p.stat().st_size,"sha256":h.hexdigest()}
def exact(p,d):
    v=identity(p)
    need(v["bytes"]==d["bytes"] and v["sha256"]==d["sha256"],"whole exact file "+Path(p).name)
    return v
def module(p,h,name):
    need(identity(p)["sha256"]==h,"immutable source "+Path(p).name)
    spec=importlib.util.spec_from_file_location(name,p)
    m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    return m
def event(name,**kw):
    print(json.dumps({"event":name,**kw},sort_keys=True),flush=True)
def invert4(a):
    z=[[(int(x)%127) for x in row]+[int(i==j) for j in range(4)] for i,row in enumerate(a)]
    det=1
    for j in range(4):
        p=next((i for i in range(j,4) if z[i][j]),None)
        need(p is not None,"original normalization is a unit")
        if p!=j: z[p],z[j]=z[j],z[p]; det=-det%127
        q=z[j][j]; det=det*q%127
        z[j]=[(x*pow(q,-1,127))%127 for x in z[j]]
        for i in range(4):
            if i!=j:
                q=z[i][j];z[i]=[(x-q*y)%127 for x,y in zip(z[i],z[j])]
    inv=[r[4:] for r in z]
    for i in range(4):
        for j in range(4):
            need(sum(a[i][k]*inv[k][j] for k in range(4))%127==int(i==j),"original U V")
            need(sum(inv[i][k]*a[k][j] for k in range(4))%127==int(i==j),"original V U")
    return inv,det

def build_input(a,PINS,dest):
    """Compare every coefficient with its literal original source phase."""
    old=module(a.prepared_source,PINS["prepared_source"],"full_weight10_paid_runtime")
    v=module(a.vector_helper,PINS["vector_helper"],"full_weight10_original_vectors")
    prep_mp=a.prepared_out/"delta-weight10-manifest.json";prep_rp=a.prepared_out/"delta-weight10-receipt.json"
    prepared_identity=identity(prep_mp);prepared_receipt=identity(prep_rp)
    prepared=json.loads(prep_mp.read_bytes());pr=json.loads(prep_rp.read_bytes())
    pb=prepared["binding"]
    need(prepared["format"]==PREPARED_FORMAT+"-manifest" and sha(canon(prepared["semantic"]))==pb,"whole prepared200 semantic binding")
    need(prepared["semantic"]["source"]["sha256"]==PINS["prepared_source"] and
         all(prepared["semantic"][key]==PINS[arg] for key,arg in (
          ("modelSourceSHA256","model_source"),("chartSourceSHA256","chart_source"),
          ("producerSourceSHA256","producer_source"),("verifierSourceSHA256","vector_helper"))),"all prepared original source identities")
    need(pr["format"]==PREPARED_FORMAT and pr["binding"]==pb and pr["status"]=="completed-prefix" and
         pr["parameters"]["through"]=="prepare" and pr["source"]["sha256"]==PINS["prepared_source"],"actual completed prepare receipt, no partial or empty candidate")
    need(pr["parameters"]["manifest"]==prepared_identity and pr["parameters"]["completePreparedColumns"]==200,"actual prepare points to this complete manifest")
    for k in ("allCompletedOriginalParentHashesVerified","all200OriginalSourceProductsInheritedFromCompleteParent",
              "all17OriginalTransportsRechecked","all24MeanCoordinatesRechecked","bothLiteralAdjugatesRechecked","all200OriginalSourceWeightsVerified"):
        need(pr["parameters"][k] is True,"actual complete original prepare gate "+k)
    need(pr["parameters"]["originalInputColumns"]==G and pr["parameters"]["originalInputTerms"]==TERMS and
         pr["parameters"]["targetTerms"]==TARGET_TERMS and len(prepared["prepared"])==G,"all200/8037189/2604 actual inputs")
    exact(a.producer_out/"complete210-sources-manifest.json",old.PARENT_MANIFEST)
    prod_mp=json.loads((a.producer_out/"complete210-sources-manifest.json").read_bytes())
    prod_rp=json.loads((a.producer_out/"complete210-sources-receipt.json").read_bytes())
    actual_parent=identity(a.producer_out/"complete210-sources-receipt.json")
    need(prepared["semantic"]["parentReceipt"]==actual_parent and prod_mp["binding"]==old.PARENT_BINDING and
         sha(canon(prod_mp["semantic"]))==old.PARENT_BINDING and prod_rp["binding"]==old.PARENT_BINDING and prod_rp["status"]=="completed","same actual complete210 execution")
    need(prod_rp["source"]["sha256"]==PINS["producer_source"] and
         prod_rp["parameters"]["manifest"]=={"path":"complete210-sources-manifest.json",**old.PARENT_MANIFEST} and
         prod_rp["parameters"]["completeModel"]==prod_mp["phases"]["complete-original210-source-model"]==old.PARENT_FINAL,"all paid complete210 mathematical identities")
    for k in ("all104NewOriginal18ProductsVerified","all104TenVectorsVerified","all210OriginalSourcesVerified"):
        need(prod_rp["parameters"][k] is True,"complete210 original gate "+k)
    full=old.read_phase(a.producer_out,old.PARENT_FINAL,old.PARENT_FORMAT,old.PARENT_BINDING)
    need(full["allColumnCount"]==210 and len(full["parentColumns"])==106 and len(full["newColumns"])==104 and
         full["all106ParentSourcesVerified"] and full["all104NewTenVectorsVerified"] and
         full["all104NewOriginal18ProductsVerified"] and full["all104NewBellSourceCoefficientsZero"],"entire complete210 final phase")
    refs=prepared["originalReferences"]
    need(len(refs)==G and Counter(r["weight"] for r in refs)=={5:6,6:20,7:30,8:40,9:24,10:80},"complete Gamma200 source weights")
    # Rebuild the literal selected dictionary from the paid final210 object.
    literal=[];deleted=[]
    for rr in full["parentColumns"]:
        fmt,bb=old.OLD[rr["parent"]];need((rr["format"],rr["binding"])==(fmt,bb),"same old original source phase")
        if rr["kind"]=="original-seed":
            sid=rr["seedIndex"]
            if 106<=sid<116:deleted.append(sid);continue
            need(sid in old.LOW or sid in old.HIGH or 100<=sid<106,"only original nonBell seeds")
            weight=5 if sid>=100 else 6 if sid in old.LOW else 8
        elif rr["kind"]=="mean-first-image":weight=7
        else:need(rr["kind"]=="commutator-first-image","entire original first-image dictionary");weight=8
        literal.append({"origin":rr,"weight":weight,"kind":"old"})
    need(deleted==list(range(106,116)) and len(literal)==96,"only ten literal Bell columns deleted")
    for rr in full["newColumns"]:
        job=rr["literalSource"]
        need(prod_mp["phases"][job["phaseKey"]]==rr["descriptor"] and tuple(job["orderedOperators"]) in old.KEEP,"every new ordered source path")
        need((job["family"]=="mean" and 100<=job["originalSeedIndex"]<106 and job["weight"]==9) or
             (job["family"]=="commutator" and job["originalSeedIndex"] in old.LOW and job["weight"]==10),"all new original mean/commutator labels")
        literal.append({"kind":"new","weight":job["weight"],"origin":{"parent":"producer","format":old.PARENT_FORMAT,"binding":old.PARENT_BINDING,"descriptor":rr["descriptor"],"literalSource":job}})
    need(literal==refs and all(d["originalReference"]==refs[i] for i,d in enumerate(prepared["prepared"])),"exact original200 label sequence, no omitted zero or duplicate")
    roots={"model":a.model_out,"mean":a.mean_out,"weight8":a.weight8_out,"producer":a.producer_out}
    def source_record(i):
        rr=refs[i]["origin"];z=old.read_phase(roots[rr["parent"]],rr["descriptor"],rr["format"],rr["binding"])
        need(z["fullOriginal18ProductVerified"] and len(z["vector"])==10 and len(z["original18Source"])==18 and z["original18Source"][17]==[],"entire original18 source and exact zero Bell slot")
        if refs[i]["kind"]=="new":
            need(z["literalSource"]==rr["literalSource"] and z["allTenImageCoordinatesVerified"] and z["originalBellSourceIsZero"],"same true new source")
        elif rr["kind"]=="original-seed":
            need(z["seedIndex"]==rr["seedIndex"] and z["allTenParameterCoordinatesRetained"],"same complete original seed")
        else:
            key="meanSeedIndex" if rr["kind"]=="mean-first-image" else "commutatorSeedIndex"
            need(z[key]==rr["seedIndex"] and z["operator"]==rr["operator"],"same complete first-image source")
        for k,poly in enumerate(z["original18Source"][:17]):
            need(all(len(ee)==17 and all(type(t)is int and t>=0 for t in ee) and
                     type(c)is int and 0<c<127 and sum(ee[:6])+2*sum(ee[6:])+(4 if k<11 else 5)==refs[i]["weight"] for ee,c in poly),"every original source term at its true weight")
        return z
    def vector_from_packed(data,weight):
        need(len(data)==10,"every original output component")
        terms=[]
        for row,poly in enumerate(data):
            for ee,c in poly:
                need(len(ee)==17 and not any(ee[12:]) and all(type(e)is int and 0<=e<=10 for e in ee) and
                     type(c)is int and 0<c<127,"all original parameter coefficients, no moment variables")
                terms.append((v.position(row,tuple(ee[:12])),c))
        return v.normalized_terms(terms,weight)[0]
    m=module(a.model_source,PINS["model_source"],"new_weight11_original_model")
    ch=module(a.chart_source,PINS["chart_source"],"new_weight11_original_chart")
    exact(a.model_out/"original-parameter-module-manifest.json",old.MODEL_MANIFEST)
    mm=json.loads((a.model_out/"original-parameter-module-manifest.json").read_bytes())
    need(mm["binding"]==old.MODEL_BINDING,"same original model binding")
    dd=mm["phases"]["complete-original-ten-parameter-action127"]
    base=m.load_gz(a.model_out/dd["path"],dd,old.MODEL_BINDING)
    dd=mm["phases"]["complete-original-global-chart127"]
    chart=m.load_gz(a.model_out/dd["path"],dd,old.MODEL_BINDING)
    original=m.unpackvec(base["allOriginal18Generators"])
    physical=m.unpackvec(chart["originalComposedGradients"])
    transport=[m.unpackvec(row) for row in base["sourceCoordinateChange"]]
    need(len(original)==18 and len(physical)==17 and len(transport)==17,"all original gradient coordinates")
    need(all(len(row)==17 and m.dot(row,physical)==original[i] for i,row in enumerate(transport)),
         "all seventeen literal original transports")
    Y=m.CTX.gens()[:6]; W=m.CTX.gens()[6:12]
    bell=sum((y*w for y,w in zip(Y,W)),m.ZERO)
    need(original[17]==bell-1==m.unpack(chart["originalBellMinusOne"]),"same original Bell")
    mats=base["allFourOriginalMeanMatrices"]
    need(len(mats)==4 and all(len(t)==6 and all(len(r)==6 for r in t) for t in mats),"all four original mean matrices")
    mats=[[[int(x)%127 for x in row] for row in t] for t in mats]
    need(all(t[i][j]==t[j][i] for t in mats for i in range(6) for j in range(6)),"original symmetric matrices")
    means=[m.unpackvec(row) for row in base["allSixOriginalMeanColumns"]]
    need(len(means)==6 and all(len(r)==10 for r in means),"all six original mean vectors")
    for k in range(4):
        for i in range(6):
            need(means[i][6+k]==sum((mats[k][i][j]*Y[j] for j in range(6)),m.ZERO),
                 "all24 original mean coefficients")
    U=[[mats[i][0][j] for i in range(4)] for j in range(4)]
    inv,det=invert4(U); need(det==74,"the four fixed canonical targets, not a changed basis")
    qs=[]
    for j in range(4):
        t=[[sum(mats[k][i][l]*inv[k][j] for k in range(4))%127 for l in range(6)] for i in range(6)]
        need([t[0][i] for i in range(4)]==[int(i==j) for i in range(4)],"canonical four upper slots")
        qs.append(sum((t[i][l]*Y[i]*Y[l] for i in range(6) for l in range(6)),m.ZERO))
    targets=[]
    for q in qs:
        target=q*bell**3; ts=[]
        for ex,cf in target.to_dict().items():
            cf=int(cf)%127
            need(len(ex)==17 and not any(ex[12:]) and sum(ex[:6])+2*sum(ex[6:12])==11,
                 "whole original weight-eleven q*b^3")
            need(cf and all(type(e) is int and 0<=e<=11 for e in ex),"integer target exponents")
            key=sum(int(ex[i])<<(5*i) for i in range(12))<<4
            ts.append((key,cf))
        ts.sort(); need(ts and len({k for k,c in ts})==len(ts),"canonical full target terms")
        targets.append(tuple(ts))
    def write_record(f,i,w,terms):
        f.write(struct.pack("<IIQ",i,w,len(terms)))
        # The protocol is deliberately independent of any elimination state.
        f.write(b"".join(struct.pack("<QB",int(k),int(c)) for k,c in terms))
    source_identity_chain=hashlib.sha256()
    counted=0
    with dest.open("wb") as stream:
        stream.write(b"ISP11P01")
        stream.write(struct.pack("<9IQ",1,127,11,150646,37568,200,4,40000,5,SEED))
        for i,d in enumerate(prepared["prepared"]):
            z=source_record(i)
            terms=vector_from_packed(z["vector"],refs[i]["weight"])
            pd=d["vector"]
            inherited=v.read_vector(a.prepared_out/pd["path"],pd,pb)
            need(inherited==terms,"every original phase coefficient equals the full prepared vector "+str(i))
            write_record(stream,i,refs[i]["weight"],terms)
            source_identity_chain.update(canon({"i":i,"origin":refs[i],"vector":pd}))
            counted+=len(terms)
            del z,terms,inherited
            if i%20==19: event("original-vector-input",columns=i+1,terms=counted)
        need(counted==TERMS,"all8037189 original generator terms")
        for j,terms in enumerate(targets): write_record(stream,200+j,11,terms)
        stream.flush(); os.fsync(stream.fileno())
    need(dest.stat().st_size==52+204*16+9*(TERMS+sum(len(t) for t in targets)),"entire exact input length")
    result={"input":identity(dest),"preparedManifest":prepared_identity,
            "preparedReceipt":prepared_receipt,"originalSourceIdentitySHA256":source_identity_chain.hexdigest(),
            "sourceTerms":counted,"targetTerms":[len(t) for t in targets],"canonicalNormalizationDet127":det}
    event("complete-original-weight11-input",**result)
    gc.collect()
    return result

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--repo",type=Path,required=True)
    ap.add_argument("--pin",required=True)
    ap.add_argument("--request",type=Path,required=True)
    ap.add_argument("--work",type=Path,required=True)
    args=ap.parse_args()
    resource.setrlimit(resource.RLIMIT_AS,(12*1024**3,12*1024**3))
    need(tuple(sys.version_info[:3])==(3,12,14),"pinned Python3.12.14")
    import flint
    need(flint.__version__=="0.9.0","pinned python-flint0.9.0")
    req=json.loads(args.request.read_bytes())
    need(req["format"]=="isp-original-weight11-projected-rank-request-v1" and req["sequence"]==1,
         "this frozen request")
    need(identity(Path(__file__))["sha256"]==req["runnerSHA256"],"frozen runner source")
    need(req["nativeSHA256"]==NATIVE_SHA and req["bitplaneHeaderSHA256"]==HEADER_SHA,"frozen new native source")
    native_seconds=req["nativeSeconds"]; need(native_seconds==14400,"bounded new calculation")
    args.work.mkdir(parents=True,exist_ok=False)
    scripts=args.work/"scripts"; scripts.mkdir()
    def git(*cmd):
        return subprocess.check_output(["git",*cmd],cwd=args.repo,timeout=120)
    last_pull=0
    def pull(force=False):
        nonlocal last_pull
        if not force and time.monotonic()-last_pull<1800: return
        before=git("rev-parse","HEAD").decode().strip()
        result=subprocess.run(["git","pull","--rebase","origin","main"],cwd=args.repo,
                              stdout=subprocess.PIPE,stderr=subprocess.STDOUT,timeout=120)
        need(result.returncode==0,"actual git pull --rebase")
        after=git("rev-parse","HEAD").decode().strip()
        diff=git("diff",before,after,"--",*RULES).decode()
        blobs={p:git("hash-object",p).decode().strip() for p in RULES}
        receipt={"format":"isp-789f-actual-actions-pull-v1","beforeCommit":before,"remoteCommit":after,
                 "utc":datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC"),
                 "actualPullRebaseSucceeded":True,"rulesUnchanged":not diff and blobs==RULES,
                 "rulesGitBlobs":blobs,"runId":os.environ.get("GITHUB_RUN_ID"),
                 "executionEnvironment":"GitHubActions"}
        if diff: print(diff,flush=True)
        print("ISP_PULL_RECEIPT "+json.dumps(receipt,sort_keys=True),flush=True)
        last_pull=time.monotonic()
        need(receipt["rulesUnchanged"],"README changed; root must read and obey the exact differences")
    pull(True)
    plan_raw=git("show",args.pin+":"+OLD_PLAN)
    need(sha(plan_raw)==OLD_PLAN_SHA,"exact paid original parent request")
    plan=json.loads(plan_raw); need(plan["historicalInputs"]==[],"all parents from original sources")
    steps=plan["steps"][1:8]
    need(len(steps)==7 and steps[-1]["argv"][steps[-1]["argv"].index("--through")+1]=="prepare",
         "parents only; never the paid weight-ten rank or candidate computation")
    pins={}
    for step in steps:
        for d in [{"path":step["script"],"sha256":step["scriptSHA256"]},*step["sources"]]:
            need(d["path"] not in pins or pins[d["path"]]==d["sha256"],"consistent immutable source")
            pins[d["path"]]=d["sha256"]
    pins[NATIVE]=NATIVE_SHA; pins[HEADER]=HEADER_SHA
    for path,h in pins.items():
        raw=git("show",args.pin+":"+path); need(sha(raw)==h,"frozen parent/new source "+path)
        dest=scripts/Path(path).name
        need(not dest.exists(),"unique source basenames")
        dest.write_bytes(raw)
        if dest.suffix==".py": ast.parse(raw.decode("utf8"),filename=str(dest))
    event("frozen-input-sources",count=len(pins),sourceCommit=args.pin,oldRequestSHA256=OLD_PLAN_SHA)
    def subst(s):
        return s.replace("{scripts}",str(scripts)).replace("{work}",str(args.work))
    run_index=0
    def run_child(name,argv,seconds,visible=False):
        nonlocal run_index
        run_index+=1; logfile=args.work/("%02d-%s.log"%(run_index,name))
        begin=time.monotonic(); last_event=begin; position=0; child=None; budget=False
        event("child-start",name=name,maximumSeconds=seconds)
        try:
            with logfile.open("wb") as out:
                child=subprocess.Popen(list(map(str,argv)),stdout=out,stderr=subprocess.STDOUT,start_new_session=True)
                while child.poll() is None:
                    now=time.monotonic()
                    pull()
                    if now-begin>seconds:
                        budget=True;os.killpg(child.pid,signal.SIGTERM)
                        try: child.wait(timeout=3)
                        except subprocess.TimeoutExpired: os.killpg(child.pid,signal.SIGKILL);child.wait()
                        break
                    if now-last_event>=30:
                        if visible:
                            with logfile.open("rb") as f:
                                f.seek(position);data=f.read(65536);position=f.tell()
                            if data: print(data.decode("utf8",errors="replace"),end="",flush=True)
                        event("child-running",name=name,seconds=round(now-begin,3))
                        last_event=now
                    time.sleep(.2)
        finally:
            if child is not None and child.poll() is None:
                os.killpg(child.pid,signal.SIGTERM)
                try: child.wait(timeout=3)
                except subprocess.TimeoutExpired: os.killpg(child.pid,signal.SIGKILL);child.wait()
        rc=child.returncode
        if visible:
            with logfile.open("rb") as f:
                f.seek(position);data=f.read(1048576)
            if data: print(data.decode("utf8",errors="replace"),end="",flush=True)
        summary={"name":name,"exitCode":rc,"outerBudget":budget,
                 "elapsedSeconds":time.monotonic()-begin,"log":identity(logfile)}
        event("child-return",**summary)
        need(not budget,"finite child budget exhausted; no mathematical conclusion")
        return rc,summary,logfile
    parents=[]
    for step in steps:
        argv=[sys.executable,scripts/Path(step["script"]).name,*[subst(s) for s in step["argv"]]]
        attempts=[None]+step.get("budgetResumeSeconds",[])
        for attempt,more in enumerate(attempts):
            seconds=step["timeoutSeconds"]
            if more is not None:
                argv[argv.index("--seconds")+1]=str(more)
                seconds=more+step.get("budgetOuterPaddingSeconds",60)
            rc,record,log=run_child(step["id"]+"-attempt"+str(attempt+1),argv,seconds)
            rp=Path(subst(step["receiptPath"]))
            need(rp.is_file(),"whole actual parent receipt")
            rr=json.loads(rp.read_bytes());record["receipt"]=identity(rp);record["receiptStatus"]=rr["status"]
            parents.append(record)
            if rc==0:
                need(rr["status"] in ("completed","completed-prefix"),"whole completed parent")
                break
            need(rc==75 and more!=attempts[-1] and rr["status"]=="budget-checkpoint"
                 and rr["parameters"].get("continuationEligible") is True
                 and rr["parameters"].get("newCompleteVerificationUnitsThisRun",0)>0,
                 "no retry of failed, empty, or exhausted parent")
        else: raise ValueError("parent did not complete")
    names={"prepared_source":"2026-11-16-r150-original-delta-weight10-runtime-parent127-789f.py",
           "vector_helper":"2026-11-16-r150-shifted-module-weight10-verifier127-789f.py",
           "model_source":"2026-11-16-r150-original-ten-generator-parameter-module-field127-v2-789f.py",
           "chart_source":"2026-11-16-r150-original-rank-four-unexpanded-local-source127-v2-789f.py",
           "producer_source":"2026-11-16-r150-original-two-round-complete210-sources127-v2-789f.py"}
    attrs={k:scripts/v for k,v in names.items()}
    PINS={k:pins[NOTES+v] for k,v in names.items()}
    for k,v in {"prepared_out":"original-delta-weight10-homogeneous127-runtime",
                "model_out":"original-ten-parameter-module127-v2",
                "mean_out":"original-mean-first-frontier127",
                "weight8_out":"original-complete-weight8-frontier127",
                "producer_out":"original-two-round-complete210-sources127-v2"}.items():
        attrs[k]=args.work/v
    a=SimpleNamespace(**attrs)
    input_path=args.work/"original-weight11-input.bin"
    inp=build_input(a,PINS,input_path)
    pull()
    native=args.work/"weight11-projected-rank"
    compiler=subprocess.check_output(["g++","--version"],text=True).splitlines()[0]
    rc,compile_record,compile_log=run_child("compile-new-weight11",
        ["g++","-O3","-march=native","-std=c++17",scripts/Path(NATIVE).name,"-o",native],120)
    need(rc==0,"new weight-eleven compilation")
    pivot_path=args.work/"selected-projected-minor.bin"
    rc,native_record,native_log=run_child("new-weight11-full-augmented-rank",
        [native,input_path,pivot_path,native_seconds],native_seconds+120,visible=True)
    need(rc==0,"complete new matrix required")
    lines=native_log.read_text().splitlines()
    outputs=[json.loads(x) for x in lines if x.startswith("{")]
    final=[z for z in outputs if z.get("kind")=="weight11_projected_augmented_result"]
    need(len(final)==1,"one full final result")
    final=final[0]
    need(final["complete_original_sources"] is True and final["original_source_columns"]==37568,
         "entire original matrix processed")
    raw=pivot_path.read_bytes();need(raw[:8]==b"ISP11U01","whole selected minor protocol")
    rank=struct.unpack_from("<I",raw,8)[0]
    need(len(raw)==12+9*rank and rank==final["augmented_rank_lower_bounds"][-1],"entire selected minor")
    rows=set();cols=set();det=1
    for i in range(rank):
        row,col,factor=struct.unpack_from("<IIB",raw,12+9*i)
        need(row<40000 and col<37572 and row not in rows and col not in cols and 0<factor<127,
             "distinct whole unit row and original source labels")
        rows.add(row);cols.add(col);det=det*factor%127
    need(det==final["selected_projected_minor_det127"]!=0,"complete selected projected unit determinant")
    sr=final["source_rank_lower_bound"];ar=final["augmented_rank_lower_bounds"]
    need(sr<=36782 and len(ar)==4 and all(ar[i] in ((sr if i==0 else ar[i-1]),
         (sr if i==0 else ar[i-1])+1) for i in range(4)),"all exact rank increments")
    need(final["four_class_threshold_reached"]==(ar[-1]>=36786),"independent characteristic-zero threshold")
    receipt={"format":"isp-original-weight11-projected-rank-execution-v1",
             "author":"Astra-ISP-b2a9acde-20261120; AI-assisted GPT-6 Astra Pro",
             "sourceCommit":args.pin,"runId":os.environ.get("GITHUB_RUN_ID"),
             "source":identity(Path(__file__)),"request":identity(args.request),
             "runtime":{"python":sys.version.split()[0],"pythonFlint":flint.__version__,"compiler":compiler},
             "parentExecutions":parents,"input":inp,"compiled":identity(native),
             "compileExecution":compile_record,"nativeExecution":native_record,
             "temporaryMinorIdentity":identity(pivot_path),"result":final,
             "arraysPublished":False,"onlyExactRankLowerBoundUsed":True}
    receipt_path=args.work/"weight11-execution-receipt.json"
    receipt_path.write_bytes(canon(receipt))
    event("complete-weight11-execution",receipt=identity(receipt_path),
          sourceRankLowerBound=sr,augmentedRankLowerBounds=ar,
          fourClassThresholdReached=final["four_class_threshold_reached"],
          nativeLog=native_record["log"],temporaryMinor=identity(pivot_path))
    pull(True)
    return 0

if __name__=="__main__":
    try: raise SystemExit(main())
    except Exception as ex:
        event("weight11-run-failed",errorType=type(ex).__name__,message=str(ex))
        raise
